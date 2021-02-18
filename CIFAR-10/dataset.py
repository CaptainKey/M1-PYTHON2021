import numpy as np
from tqdm import tqdm
import tarfile
import requests 
import os 
import matplotlib.pyplot as plt
import logging

class dataset:
    def __init__(self,file_name='test_batch.bin',classes_file='batches.meta.txt',nb_imgs=10000,download=False):
        # Construction de la base de données
        self.tar_name = 'cifar-10-binary.tar.gz'
        self.url = "http://www.cs.toronto.edu/~kriz/{}".format(self.tar_name)
        # Dossier de décompression 
        self.folder = 'cifar-10-batches-bin'
        # Fichier texte qui comprend les noms des classes
        self.classes_file = classes_file
        # Fichier binaire à lire pour la base de données
        self.file_name = file_name
        
        # Nombre d'image à lire
        self.nb_imgs = nb_imgs

        # On regarde si le dossier cifar-10-batches-bin existe, si ce n'est pas le cas alors on télécharge l'archive
        if not os.path.exists(self.folder): 
            logging.info('{}/ folder not found'.format(self.folder))
            download = True
        else:
            logging.info('{}/ folder found'.format(self.folder))

        if download:
            logging.info('Downloading {}'.format(self.tar_name))
            self.download_base()
        
        # Tableaux pour stocker les images, les labels, les classes
        self.imgs = []
        self.labels = []
        self.classes = []

        # Lecture de la base de données
        self.read_dataset()

        # Lecture des classes
        self.read_classes()

    def __len__(self):
        # Retourne la taille de la base de données
        return len(self.imgs)
    def __getitem__(self,idx):
        # Récupération de l'élement idx la base de données
        assert idx <= len(self), logging.critical('{} does not exist in dataset (Should be between {} and {})'.format(idx,0,self.nb_imgs))
        return self.imgs[idx],self.labels[idx]

    def show(self,idx):  
        assert idx < len(self), logging.critical('{} does not exist in dataset (Should be between {} and {})'.format(idx,0,len(self)))
        logging.info('Display picture {}'.format(idx))
        
        # Chargement de l'image que l'on souhaite afficher
        img = self.imgs[idx]
        
        # Création d'un titre pour le graphique
        plt.suptitle(" CIFAR-10 : image {} - classe : {}".format(idx,self.classes[self.labels[idx]]))
        
        # Changement de la position des axes
        # Passage de l'image en dimension (Hauteur, Largeur, Canaux) en (Canaux,Hauteur, Largeur)
        flip_channel = np.moveaxis(self.imgs[idx],0,2)

        # Definition d'un sous graphique pour afficher l'image en RGB
        """ 
            plt.subplot(A,B,C)
            A = Nombre de lignes dans le graphique
            B = Nombre de colonne 
            C = Position du graphique courant 
        """
        sub1  = plt.subplot(1,4,1)
        sub1.set_title('RGB') # Définition d'un sous-titre pour le sous graphique
        sub1.axis('off') # Désactivation de l'affichage des axes
        plt.imshow(flip_channel) # Affichage de l'image dans le graphique

        sub2  = plt.subplot(1,4,2)
        sub2.set_title('Rouge')
        sub2.axis('off')
        plt.imshow(img[0],cmap='Reds')

        sub3  = plt.subplot(1,4,3)
        sub3.set_title('Vert')
        sub3.axis('off')
        plt.imshow(img[1],cmap='Greens')

        sub4  = plt.subplot(1,4,4)
        sub4.set_title('Bleue')
        sub4.axis('off')
        plt.imshow(img[2],cmap='Blues')

        logging.info('Saving current figure as display{}.png'.format(idx))
        plt.savefig('display{}.png'.format(idx)) # Sauvegarde du graphique sous le nom display{idx}.png

    def read_dataset(self):
        # Définition du chemin vers le fichier de données
        path = '{}/{}'.format(self.folder,self.file_name)
        # On test si le chemin vers le fichier existe
        assert os.path.exists(path), logging.critical('{} does not exist'.format(path))
        logging.info('Starting reading dataset at {}'.format(path))

        # Lecture du fichier
        with open(path,'rb') as file:
            for i in tqdm(range(self.nb_imgs),desc='Reading {}'.format(path),ascii=True):
                # Lecture de 1 byte = Label 
                byte = file.read(1)
                self.labels.append(int.from_bytes(byte,byteorder='big'))
                # Lecture de 3072 bytes - 1024 bytes pour le channel rouge,1024 bytes pour le channel vert,1024 bytes pour le channel bleue
                byte_array = file.read(3072)
                # Convertion des valeurs Hexa en int
                img = [byte for byte in byte_array]
                # Les pixels sont sur 8bits de 0 à 255 on peut donc les coder sur des entiers position sur 8 bits soit uint8
                # Enfin converstion de la liste des pixels en tableaux numpy redimensionné sous forme d'image [CHANNEL,HEIGHT,WIDTH]
                self.imgs.append( np.array(img,'uint8').reshape(3,32,32) )
        logging.info('Dataset file read')
    def read_classes(self):
        # Définition du chemin vers le fichier de données
        path = '{}/{}'.format(self.folder,self.classes_file)
        # On test si le chemin vers le fichier existe
        assert os.path.exists(path), logging.critical('{} does not exist'.format(path))
        logging.info('Starting reading classes file at {}'.format(path))
        file = open(path,'r')
        # Lecture du fichier et on créer une liste avec comme sélecteur entre chaque element \n (=Retour à la ligne)
        classes = file.read().split('\n')
        # Utilisation d'un filtre pour enlever les valeurs vide de la liste ''
        classes = list(filter(lambda classe: classe != '',classes))
        file.close() #Fermeture du fichier
        self.classes = classes
        logging.info('Classes file read')
    
    def uncompress_tar_gz(self):
        # Ouverture de l'archive
        archive = tarfile.open(self.tar_name,"r:gz")
        # Décompression
        logging.info("Extracting {}".format(self.tar_name))
        archive.extractall()
        # Fermture de l'archive
        archive.close()
        logging.info('Removing {}'.format(self.tar_name))
        # Suppression de l'archive car inutile
        os.remove(self.tar_name)

    def download_base(self):
        # Lancement d'une requête HTTP de type GET pour récupérer l'archive de données
        logging.info('Launching HTTP GET Request to {}'.format(self.url))
        try:
            req = requests.get(self.url, stream=True)
        except e:
            logging.critical('Could not get {}'.format(self.url))
            exit(0)
        # Récupération de la taille du fichier à travers les headers de la requête
        total_size = int(req.headers.get('content-length'))
        logging.info("File size : {}".format(total_size))

        # On regarde si l'archive n'existe pas dans le dossier courant
        if not os.path.isfile(self.tar_name):
            logging.info('Downloading file {}'.format(self.tar_name))
            with open(self.tar_name,'wb') as file:
                with tqdm(total=total_size, unit='it', unit_scale=True,desc=self.tar_name,initial=0,ascii=True) as pbar:
                    for chunk in req.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            pbar.update(len(chunk))
        else:
            logging.info('{} already exist'.format(self.tar_name))

        self.uncompress_tar_gz()

