import cv2
import pytesseract
from PIL import Image
import os

# Segmentção da Imagem - region of interest (ROI)

# Carregar pasta de imagens
folder = "assets/images"

# Reconhecer todas as imagens da pasta
for image in os.listdir(folder):
    # Extrair o nome de cada imagem
    name, extension = os.path.splitext(image)

    print(f"Imagem: {image} \n")

    image = cv2.imread(f"{folder}/{image}")

    # Convertendo para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar a limiarização
    ret, thresholded = cv2.threshold(gray_image, 115, 255, cv2.THRESH_BINARY)

    # Suavização para remover ruido
    blurred_image = cv2.GaussianBlur(thresholded, (3, 3), 0)

    # Definir coordenadas e dimensões do ROI
    x = 225 # posição x do canto superior esquerdo do ROI
    y = 60 # posição y do canto superior esquerdo do ROI
    w = 300 # largura da roi
    h = 50 # altura da roi

    roi = blurred_image[y:y+h, x: x+w]

    # Desenhar retângulo na imagem original
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 5) # Verde
    cv2.rectangle(image, (x, y+50), (x + w, (y+50) + (h-25)), (175, 12, 255), 5) # Verde

    # Mostrar a imagem orignial com o roi destacado
    cv2.imshow("Imagem oringial com ROI", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Mostrar a imagem segmentada
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Salvar imagens
    cv2.imwrite(f"assets/images/ROI/{name}-blurred-image{extension}", blurred_image) # suavização
    cv2.imwrite(f"assets/images/ROI/{name}-gray{extension}", gray_image) # escala de cinza

    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    # blurred image
    texto = pytesseract.image_to_string(blurred_image)
    f = open(f"assets/extracted-info/{name}-blurred-image.txt", "w+")
    f.write(texto)
    f.close()

    # escala de cinza
    texto = pytesseract.image_to_string(gray_image)
    f = open(f"assets/extracted-info/{name}-gray-image.txt", "w+")
    f.write(texto)
    f.close()
