import numpy as np

class dataset:
    def __init__(self,file_name):
        # Initialisation de la base de données
        self.file_name = file_name
        self.imgs = []
        self.labels = []
        self.read_dataset()

    def __len__(self):
        # Retourne la taille de la base de données
        pass
    def __getitem__(self,idx):
        # Récupération d'un élement de la base de données
        return self.imgs[idx],labels[idx]
    def show(self,idx):
        # Afficher via matplotlib l element X de la base de données
        pass
    def download_base(self):
        # Télécharger la base de données si non existante
        pass
    def read_dataset(self):
        with open(self.file_name,'rb') as file:
            for i in range(10000):
                byte = file.read(1)
                self.labels.append(int.from_bytes(byte,byteorder='big'))
                byte_array = file.read(3072)
                img = [byte for byte in byte_array]
                self.imgs.append( np.array(img,'uint8').reshape(3,32,32) )
if __name__ == '__main__':
    db = dataset('test_batch.bin')


