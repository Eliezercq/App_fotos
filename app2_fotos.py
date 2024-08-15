import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def enhance_image_quality(image_path, output_path, strength=1.5):
    try:
        img = cv2.imread(image_path)

        if img is None:
            raise Exception(f"Error: Unable to load the image from {image_path}")

        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

        b, g, r = cv2.split(img)

        sharpened_b = cv2.filter2D(b, -1, kernel)
        sharpened_g = cv2.filter2D(g, -1, kernel)
        sharpened_r = cv2.filter2D(r, -1, kernel)

        enhanced = cv2.merge([sharpened_b, sharpened_g, sharpened_r])

        cv2.imwrite(output_path, enhanced)

        cv2.imshow('Original', img)
        cv2.imshow('Enhanced', enhanced)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")

def select_image():
    root = Tk()
    root.withdraw()  # Esconder a janela principal

    image_path = askopenfilename(title="Selecione uma imagem", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])

    if image_path:
        output_path = "imagem_melhorada.png"
        enhance_image_quality(image_path, output_path)
    else:
        print("Nenhuma imagem selecionada.")

select_image()
