import layers as l
from dataset import dataset
import numpy as np
import matplotlib.pyplot as plt
class LeNet():
    def __init__(self):
        self.conv1 = l.Convolution("conv1",3,6,5,1)
        self.conv2 = l.Convolution("conv2",6,16,5,1)
        self.relu = l.ReLU("relu")
        self.pool = l.Maxpooling("pooling",2,2)
        self.dense1 = l.Dense("dense1",16*5*5,120)
        self.dense2 = l.Dense("dense1",120,84)
        self.dense3 = l.Dense("dense1",84,10)
    def forward(self,x):
        print(x.shape)
        x = self.conv1(x)
        self.show("Conv 1 out",x)

        print(x.shape)
        x = self.relu(x)
        self.show("Relu 1 out",x)

        print(x.shape)
        x = self.pool(x)
        self.show("Pool 1 out",x)

        print(x.shape)
        x = self.conv2(x)
        self.show("conv 2 out",x)

        print(x.shape)
        x = self.relu(x)
        self.show("Relu 2 out",x)

        print(x.shape)
        x = self.pool(x)
        self.show("pool 2 out",x,block=True)


        print(x.shape)
        x = x.reshape(-1)

        print(x.shape)
        x = self.dense1(x)
        print(x.shape)
        x = self.relu(x)
        print(x.shape)
        x = self.dense2(x)
        print(x.shape)
        x = self.relu(x)
        print(x.shape)
        x = self.dense3(x)
        print(x.shape)

        return x
    def __call__(self,x):
        return self.forward(x)
    def load_params(self,dict_params):
        self.conv1.load_weight(dict_params['conv1_weight'])
        self.conv1.load_bias(dict_params['conv1_bias'])

        self.conv2.load_weight(dict_params['conv2_weight'])
        self.conv2.load_bias(dict_params['conv2_bias'])

        self.dense1.load_weight(dict_params['dense1_weight'])
        self.dense1.load_bias(dict_params['dense1_bias'])

        self.dense2.load_weight(dict_params['dense2_weight'])
        self.dense2.load_bias(dict_params['dense2_bias'])

        self.dense3.load_weight(dict_params['dense3_weight'])
        self.dense3.load_bias(dict_params['dense3_bias'])
        print('Poids charges')
    def show(self,name,x,col=False,line=False,block=False):
        c,_,_ = x.shape
        if col == False: col = 2 
        if line == False: line = c//col 
        assert col*line >= c, "Wrong col,line"
        plt.figure()
        plt.suptitle(name)
        for i in range(c):
            sub = plt.subplot(line,col,i+1)
            sub.set_title(i)
            sub.axis('off')
            plt.imshow(x[i])
        plt.savefig(name)
        plt.show(block=block)

if __name__ == '__main__':
    data = dataset('cifar-10-batches-bin/test_batch.bin',download=True)
    img, label = data[0]

    net = LeNet()

    params = {
        "conv1_weight" : np.load('params/conv1.weight.save'),
        "conv1_bias" : np.load('params/conv1.bias.save'),

        "conv2_weight" : np.load('params/conv2.weight.save'),
        "conv2_bias" : np.load('params/conv2.bias.save'),

        "dense1_weight" : np.load('params/fc1.weight.save'),
        "dense1_bias" : np.load('params/fc1.bias.save'),

        "dense2_weight" : np.load('params/fc2.weight.save'),
        "dense2_bias" : np.load('params/fc2.bias.save'),

        "dense3_weight" : np.load('params/fc3.weight.save'),
        "dense3_bias" : np.load('params/fc3.bias.save')
    }
    net.load_params(params)

    out = net( ( (img/255) - 0.5) / 0.5 )
    idx_max = np.argmax(out)
    print("Classe predite : {}".format(data.classes[idx_max]))
    print(out)