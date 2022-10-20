'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía GR 1

Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
'''

#Python Imports
import numpy as np
import random
from sympy import Matrix

#Local imports
import algorythmUtils


#CONSTANTS

#Alphabets for the algorythm

ENCRYPT_ALPHA : dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
            '0':26, '1': 27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, '.': 36, ',': 37, ':': 38, '?': 39 , ' ': 40}

DECRYPT_ALPHA : dict = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M',
            '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0',
            '27': '1', '28': '2', '29': '3', '30': '4', '31': '5', '32' : '6', '33' : '7', '34' : '8', '35' : '9', '36' : '.', '37' : ',', '38' : ':', '39' : '?', '40' : ' '}

#In this case N is going to be 40.
N = len(ENCRYPT_ALPHA)



#K Algorythm for generating the key
def generateKey(succesionLength : int):
    '''
    '''
    randomSuccession = []

    #Generate the random succesion for (succesionLength * succesionLength)
    for character in range(0 , succesionLength * succesionLength):
        #This will add the corresponding char code in ENCRYPT_ALPHA
        randomSuccession.append(random.randint(0,N))
    
    keyMatrix = np.array(randomSuccession).reshape(succesionLength, succesionLength)

    return keyMatrix





def main():
    generateKey(3)

main()

