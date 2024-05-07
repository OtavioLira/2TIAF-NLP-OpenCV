import cv2

# Carregar imagem original
image = cv2.imread("pessoa.jpg")

# Convertendo para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar thresholding para obter uma imagem binária
_, thresh_image = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY_INV)

# Suavização para remover ruído
blurred_image = cv2.GaussianBlur(thresh_image, (3,3), 0)

# Detecção de bordas Canny
canny_edges = cv2.Canny(blurred_image, 100, 200)

# Exibir e salvar imagens
cv2.imshow("Prepared Image", gray_image)
cv2.waitKey(0)
cv2.imshow("Prepared Image", thresh_image)
cv2.waitKey(0)
cv2.imshow("Prepared Image", blurred_image)
cv2.waitKey(0)
cv2.imshow("Prepared Image", canny_edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imwrite("processed_image.jpg", blurred_image)
