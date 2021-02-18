import numpy as np

class Convolution():
    """
        args : 
            stride (pas du noyau (kernel))
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

        dim_params = [nb_filtre,nb_channel,kernel_size_y,kernel_size_x]


    img[0] = [1,2,3,4]
          [5,6,7,8]
          [9,10,11,12]
          [13,14,15,16]

    img[1] = [1,2,3,4]
          [5,6,7,8]
          [9,10,11,12]
          [13,14,15,16]

    img[2] = [1,2,3,4]
          [5,6,7,8]
          [9,10,11,12]
          [13,14,15,16]


    weight[0][0] = [1,2]
                   [3,4]

    weight[0][1] = [1,2]
                   [3,4]

    weight[0][2] = [1,2]
                   [3,4]

    weight[1][0] = [1,2]
                   [3,4]

    weight[1][1] = [1,2]
                   [3,4]

    weight[1][2] = [1,2]
                   [3,4]
    self.weight = np.random.rand(2,3,2,2)
             
    """
    def __init__(self,name,in_channels,nb_filtre,kernel_shape,stride):
        self.name = name
        self.stride = stride
        self.kernel_shape = kernel_shape
        
        self.weight = np.random.rand(nb_filtre,in_channels,kernel_shape,kernel_shape)
        self.bias   = np.random.rand(nb_filtre) 
    def __call__(self,x):
        in_c, in_h, in_w = x.shape
        out_h  = int( (in_h - (self.kernel_shape -1) - 1 ) / self.stride) + 1
        out_w  = int( (in_w - (self.kernel_shape -1) - 1 ) / self.stride) + 1
        print(out_h,out_w)
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

    KERNEL_SHAPE = 3
    [0,1,2]
    [5,6,7]
    [10,11,23]

    KERNEL_SHAPE = 1
    [0]

    KERNEL_SHAPE = 4
    [0,1,2,3]
    ...
    ...
    [15,16,17,18]
    """
    def __init__(self,name,kernel_shape,stride):
        self.name = name 
        self.kernel_shape = kernel_shape
        self.stride = stride
    def __call__(self,x):
        channels, height,width = x.shape
        out = []
        out_shape_x = int((width - self.kernel_shape ) / self.stride)+1
        out_shape_y = int((height - self.kernel_shape) / self.stride)+1
        print(out_shape_x,out_shape_y)
        for channel in range(channels):
            for h in range(0,height-self.kernel_shape+1,self.stride):
                for w in range(0,width-self.kernel_shape+1,self.stride):
                    maximum = x[channel][h][w]
                    for m in range(self.kernel_shape):
                        for n in range(self.kernel_shape):
                            if x[channel][h+m][w+n] > maximum : maximum = x[channel][h+m][w+n]
                    out.append(maximum)
        print(len(out))
        out = np.array(out).reshape((channels,out_shape_y,out_shape_x))
        return out

if __name__ == '__main__':
    # Definition de l'operation
    # maxpool1 = Maxpooling('maxpool1',2,2)
    # x = np.random.rand(1,4,4)
    # for line in x:
    #     print(line)
    # print('shape',x.shape)
    # out = maxpool1(x)
    # for line in out:
    #     print(line)
    # print('shape',out.shape)
    conv1 = Convolution('conv1',3,6,5,1)
    x = np.ones((3,32,32))
    conv1(x)
