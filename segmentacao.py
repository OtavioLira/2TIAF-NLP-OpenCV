import cv2

# Segmentção da Imagem - region of interest (ROI)

# Carregar a imagem
image = cv2.imread("/assets/images/test/carro.jpg")

# Aplicar a limiarização
ret, thresholded = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

# Suavização para remover ruido
blurred_image = cv2.GaussianBlur(thresholded, (3, 3), 0)

# Definir coordenadas e dimensões do ROI
x = 460 # posição x do canto superior esquerdo do ROI
y = 470 # posição y do canto superior esquerdo do ROI
w = 150 # largura da roi
h = 50 # altura da roi

roi = blurred_image[y:y+h, x: x+w]

# Mostrar a imagem segmentada
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Desenhar retângulo na imagem original
cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 5) # Verde

# Mostrar a imagem orignial com o roi destacado
cv2.imshow("Imagem oringial com ROI", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detecção de bordas

# Convertendo para escala de cinza
gray_image = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# Aplicar thresholding para obter uma imagem binária
_, thresh_image = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY)

# Suavização para remover ruído
blurred_image = cv2.GaussianBlur(thresh_image, (3,3), 0)

# Detecção de bordas Canny
canny_edges = cv2.Canny(roi, 100, 255)
cv2.imshow("Imagem segmentada", canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Utilizando o tesseract para extrair texto
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Salvar o ROI como uma nova imagem
cv2.imwrite("/assets/images/teste/roi_carro.jpg", roi)

# Usa o pytesseract para realizar OCR na imagem
imagem = Image.open("/assets/images/teste/roi_carro.jpg")

texto = pytesseract.image_to_string(imagem)

print(texto)
