# image-downloader-with-threads
# Image Downloader with Threads

Este programa é um exemplo de como baixar várias imagens da internet simultaneamente usando threads em Python.

Como o programa funciona?

O programa cria múltiplas threads, onde cada thread é responsável por baixar uma imagem específica de uma URL fornecida. Cada imagem é salva localmente com o nome especificado. O programa garante que todas as threads terminem antes de prosseguir, utilizando o método `join()`.

Uso de Threads:

A biblioteca `threading` do Python é usada para criar e gerenciar múltiplas threads. Isso permite que os downloads de imagens ocorram em paralelo, o que pode acelerar o processo comparado a baixar as imagens sequencialmente em uma única thread.

Ponto importante!

Certifique-se de ter o Python e a biblioteca `requests` instalada:
   pip install requests

Nome dos integrantes:

João Ricardo - 1134269

Lorenzo Pasa - 1134869
