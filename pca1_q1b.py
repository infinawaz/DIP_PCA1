from PIL import Image
import os

def crop_rotate_resize_image(image_path, crop_area, rotation_angle, resize_dimensions, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    with Image.open(image_path) as img:
        cropped_img = img.crop(crop_area)
        rotated_img = cropped_img.rotate(rotation_angle)
        resized_img = rotated_img.resize(resize_dimensions)
        resized_img.save(save_path)
    print(f"Image cropped, rotated, resized, and saved to {save_path}")

if __name__ == "__main__":
    input_image_path = "E:/DIP_PCA1/q1_inputImage/Lenna.png"
    save_image_path = "E:/DIP_PCA1/q1b_rotatedImage/rotatedOne.png"

    crop_area = (100, 100, 500, 500)
    rotation_angle = -45
    resize_dimensions = (150, 150)
    
    crop_rotate_resize_image(input_image_path, crop_area, rotation_angle, resize_dimensions, save_image_path)
