import numpy as np
from tqdm import tqdm
import tarfile
import requests 
import os 
class dataset:
    def __init__(self,file_name):
        # Initialisation de la base de données
        self.url = "http://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz"
        self.file_name = file_name
        self.imgs = []
        self.labels = []
        # self.read_dataset()
        self.download_base()

    def __len__(self):
        # Retourne la taille de la base de données
        pass
    def __getitem__(self,idx):
        # Récupération d'un élement de la base de données
        return self.imgs[idx],labels[idx]
    def show(self,idx):
        # Afficher via matplotlib l element X de la base de données
        pass
    def read_dataset(self):
        with open(self.file_name,'rb') as file:
            for i in range(10000):
                byte = file.read(1)
                self.labels.append(int.from_bytes(byte,byteorder='big'))
                byte_array = file.read(3072)
                img = [byte for byte in byte_array]
                self.imgs.append( np.array(img,'uint8').reshape(3,32,32) )
    
    def download_base(self):
        # Télécharger la base de données si non existante
        req = requests.get(self.url, stream=True)
        total_size = int(req.headers.get('content-length'))
        tar_gz = 'base.tar.gz'

        if not os.path.isfile(tar_gz):
            with open(tar_gz,'wb') as file:
                with tqdm(total=total_size, unit='it', unit_scale=True,desc=tar_gz,initial=0,ascii=True) as pbar:
                    for chunk in req.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            pbar.update(len(chunk))

        archive = tarfile.open(tar_gz,"r:gz")
        archive.extractall()
        archive.close()
        os.remove(tar_gz)

if __name__ == '__main__':
    db = dataset('test_batch.bin')


