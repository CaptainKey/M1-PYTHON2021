class Convolution():
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
    def __init__(self):
        pass 
    def __call__(self):
        pass

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


