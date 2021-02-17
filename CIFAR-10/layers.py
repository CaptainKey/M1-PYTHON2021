import numpy as np

class Convolution():
    """
        args : 
            stride (pas du noyau (kernel))
            padding 
            nombre de filtres (nb_filtre) 
            nombre de canaux  (nb_channel)
            kernel_size_x 
            kernel_size_y

            dim_params = [nb_filtre,nb_channel,kernel_size_y,kernel_size_x]

            X_out_dim = [ (X_in_dim + 2*padding - (kernel_size_x -1) -1)/stride  +1 ]
            Y_out_dim = [ (Y_in_dim + 2*padding - (kernel_size_y -1) -1)/stride  +1 ]

            Ex : CHANNEL = 1
            Image dim = [32,32]
            kernel_shape = 5 (x et y)
            stride = 1
            padding = 0

            => X_out = ( (32 + 2*0 - (5-1) -1)/1 +1 ) = 28
               Y_out = *** = 28

            Image_entree_dim = [28,28]
            Image_sortie_dim = [28,28]

            Ex : CHANNEL = 3

            Image dim = [32,32,3]
            nb_filtre = 3
            nb_channel = 64
            kernel_shape = 5 (x et y)
            stride = 1
            padding = 0

            => X_out = ( (32 + 2*0 - (5-1) -1)/1 +1 ) = 28
               Y_out = *** = 28

            Image_entree_dim = [64,28,28]
            Image_sortie_dim = [64,28,28]

        Ex :
            Padding = 2

        img = [2,1] => img_with_pad = [0,0,0,0]
              [3,2]                   [0,2,1,0]
                                      [0,3,2,0]
                                      [0,0,0,0]

        STRIDE = 1:
        [0,0] => [0,0] => [0,0] ..etc...
        [0,2]    [2,1]    [1,0]


    """
    def __init__(self):
        pass 
    def __call__(self):
        pass
    def load_weight(self):
        pass 
    def load_bias(self):
        pass
    def load_params(self):
        pass

class Dense():
    """
    Calcul matriciel 

    Exemple avec les dimensions :
        x.shape      = 4096
        params.shape = 4096,1000
        y = 1000

        y_j = x_i*w_i_j + b_j

        x.shape = n
        params.shape = m*n
        m < n
        x*weight => Taille m
    """ 
    def __init__(self):
        self.weight = []
        pass 
    def __call__(self):
        pass
    def load_weight(self,new_weight):
        pass 
    def load_bias(self,new_bias):
        pass
    def load_params(self,dict_params):
        pass

class ReLU():
    """
        y = Relu(x)

        y = x si x > 0
        y = 0 si x < 0

        ex : 

        relu1 = ReLU()
        x = [0,1,-10,4,2]
        relu1(x) => [0,1,0,4,2]
    """
    def __init__(self,name):
        self.name = name
    def __call__(self,x):
        x[x<0] = 0 
        return x

class Maxpooling():
    """
    x= [0,1,2,3,4]
       [5,6,7,8,9]
       [10,11,12,13,14]
       [15,16,17,18,19]

    args : 
        - stride 
        - kernel_shape

    AVEC STRIDE 1 :
    [X,X] [0, 1] -> [1,2] -> [2,3] ->  [3,4]
    [X,X] [5, 6]    [6,7] -> [7,8] ->  [8,9]

    => [5,6]
       [10,11] ..etc...

    AVEC STRIDE 2 : 
    [X,X] [0, 1] -> [2,3] 
    [X,X] [5, 6]    [7,8] 

    OPERATION MAX POOLING: 
    [1,2]
    [6,7]
    MAX = 7

    """
    def __init__(self):
        pass 
    def __call__(self):
        pass

if __name__ == '__main__':
    relu1 = ReLU('relu1')
    print('name',relu1)

    x = np.array([-1,0,2,-2])
    print(x)
    out = relu1(x)
    print(out)