import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def enhance_image_quality(image_path, output_path, strength=1.5):
    try:
        # Carregar a imagem
        img = cv2.imread(image_path)

        if img is None:
            raise Exception(f"Error: Unable to load the image from {image_path}")

        # Aplicar um filtro de nitidez para cada canal de cor
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

        # Separar os canais de cor
        b, g, r = cv2.split(img)

        # Aplicar o filtro de nitidez a cada canal
        sharpened_b = cv2.filter2D(b, -1, kernel)
        sharpened_g = cv2.filter2D(g, -1, kernel)
        sharpened_r = cv2.filter2D(r, -1, kernel)

        # Mesclar os canais nítidos para formar a imagem melhorada
        enhanced = cv2.merge([sharpened_b, sharpened_g, sharpened_r])

        # Salvar a imagem de saída
        cv2.imwrite(output_path, enhanced)

        # Exibir as imagens (opcional)
        cv2.imshow('Original', img)
        cv2.imshow('Enhanced', enhanced)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")

def select_image():
    # Criar uma janela root para o Tkinter
    root = Tk()
    root.withdraw()  # Esconder a janela principal

    # Abrir uma caixa de diálogo para selecionar o arquivo
    image_path = askopenfilename(title="Selecione uma imagem", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])

    # Se o usuário selecionar um arquivo, prosseguir com o aprimoramento
    if image_path:
        output_path = "imagem_melhorada.png"
        enhance_image_quality(image_path, output_path)
    else:
        print("Nenhuma imagem selecionada.")

# Executar o seletor de imagem
select_image()