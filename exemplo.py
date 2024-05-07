import cv2

# Carregar uma imagem
image = cv2.imread("fiap.jpeg")

# Exibir a imagem
cv2.imshow("Image Title", image)
cv2.waitKey(0)  # Espera até que uma tecla seja pressionada
cv2.destroyAllWindows()

# Salvar imagem
cv2.imwrite("imagem_salva.jpg", image)