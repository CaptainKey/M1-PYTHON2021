class dataset:
    def __init__(self,name):
        file = open(name,'rb').read()
        self.imgs, self.labels = lire_les_imgs(file)
        
        # Initialisation de la base de données
    def __len__(self):
        # Retourne la taille de la base de données
    def __getitem__(self,idx):
        # Récupération d'un élement de la base de données
        return self.imgs[idx],labels[idx]
    def show(self,idx):
        # Afficher via matplotlib l element X de la base de données

    def download_base(self):
        # Télécharger la base de données si non existante

db_test1 = dataset('test_batch.bin')
db_test1.show(40)

for i,(img,label) in enumerate(db_test1):
    print(label)
    plt.imshow(img)


img, label = db_test1[0]
