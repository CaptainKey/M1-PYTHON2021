import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--test',help='Un arg de test',action='store_true')
parser.add_argument('--val',help='Une valeur',type=int,default=0,required=True)

args = parser.parse_args()

print(args)
# print(dir(args)=