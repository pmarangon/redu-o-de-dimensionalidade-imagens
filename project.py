import cv2
import matplotlib.pyplot as plt

# Carregar a imagem colorida
image_path = "paula_color.jpg"  # Substitua pelo caminho da sua imagem
color_image = cv2.imread(image_path)

# Converter a imagem de BGR para RGB (porque o OpenCV usa BGR por padrão)
color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

# Converter para tons de cinza
gray_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2GRAY)

# Binarizar a imagem usando um limiar (threshold)
threshold = 128  # Ajuste o valor do limiar conforme necessário
_, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

# Mostrar as imagens usando Matplotlib
plt.figure(figsize=(15, 5))

# Imagem original
plt.subplot(1, 3, 1)
plt.imshow(color_image)
plt.title("Imagem Colorida")
plt.axis("off")

# Imagem em tons de cinza
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Níveis de Cinza")
plt.axis("off")

# Imagem binarizada
plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap="gray")
plt.title("Preto e Branco")
plt.axis("off")

# Exibir as imagens
plt.tight_layout()
plt.show()
