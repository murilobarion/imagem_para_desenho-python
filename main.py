import cv2
import os 

def imagem_tratada(arquivo, qtd_filtro):
	img = cv2.imread(f'img/{arquivo}')
	img_pb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_invertida = cv2.bitwise_not(img_pb)
	img_blur = cv2.GaussianBlur(img_invertida, (qtd_filtro, qtd_filtro), 0)
	img_blur_invertida = img_invertida = cv2.bitwise_not(img_blur)
	img_final = cv2.divide(img_pb, img_blur_invertida, scale=256.0)

	cv2.imwrite(f'img_tratado/{arquivo}', img_final)

lista_arquivos = os.listdir('img')

for arquivo in lista_arquivos:
	imagem_tratada(arquivo, 97)