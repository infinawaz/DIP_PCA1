import os
from PIL import Image

def open_show_save_image(image_path, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    with Image.open(image_path) as img:
        img.show()
        img.save(save_path)
    print(f"Image opened from {image_path} and saved to {save_path}")


if __name__ == "__main__":
    input_image_path = "E:/DIP_PCA1/inputImage/Lenna.png"
    save_image_path = "E:/DIP_PCA1/savedImage/savedOne.jpg"

    open_show_save_image(input_image_path, save_image_path)
