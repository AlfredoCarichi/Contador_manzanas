import streamlit as st
from ultralytics import YOLO
from ultralytics.solutions import object_counter


import imutils
import os
from os import mkdir
from datetime import date
from datetime import datetime
from getpass import getuser
import supervision as sv
from PIL import Image

import matplotlib.path as mplPath
import matplotlib.pyplot as plt



from PIL import Image

from ultralytics import YOLO
from ultralytics.solutions import object_counter


import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import imutils
import gdown

from functions import *


def main():
    
    st.header('Aplicación para el conteo de manzanas en el árbol')
    st.markdown('Esta aplicación esta desarrollada por el Lic. Brayan Murillo y Yulesli Guillén. Para el conteo de las manzanas en el árbol se utiliza una red neuronal convolucional la cual fue entrenada con una GPU RTX 4060, 1100 imágenes de entrenamiento y 220 de validación. Se hicieron 100 épocas las cuales dieron como resultado un archivo PyTorch el cual es el que hace las detecciones. Todo fue desarrollado en el lenguaje Python. La aplicación puede ser mejorada sustancialmente utilizando una red neuronal mas compleja, pero por cuestiones de tiempo y eficiencia se utilizó la más simple de todas.')
    file_uploader = st.file_uploader('Sube tu imagen en los siguientes formatos: ', type=['jpg', 'png'])

    if file_uploader is not None:
        image = Image.open(file_uploader)
        print(image)
        

        st.image(image)
        datos = deteccion(image)
        st.markdown('La paleta de colores original fue modificada para poder observar las detecciones de mejor manera.')
        st.image(deteccion((image)))

        st.markdown(deteccion2((image)) + ' manzanas detectadas.')

        


if __name__ == "__main__":
    main()
