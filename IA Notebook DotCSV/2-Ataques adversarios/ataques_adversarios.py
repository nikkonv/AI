#! python 3
"""
* ataques adversarios, consisten en intentar romper una IA
* y en este caso sera la inseption v3 de google
* es un clasificador de imagenes de google 
* clasifica en unas 1000 categorias
* la idea es pasarle una imagen y que se equivoque
* 	1. descargar el modelo
* 	2. generar imagen adversaria que engane a la red
"""
import tensorflow as tf
