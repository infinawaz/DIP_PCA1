from PIL import Image
import os

def crop_rotate_resize_image(image_path, crop_area, rotation_angle, resize_dimensions, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    with Image.open(image_path) as img:
        cropped_img = img.crop(crop_area)
        # Rotate the image
        rotated_img = cropped_img.rotate(rotation_angle)
        # Resize the image
        resized_img = rotated_img.resize(resize_dimensions)
        # Save the manipulated image
        resized_img.save(save_path)
    print(f"Image cropped, rotated, resized, and saved to {save_path}")

# Example usage:
if __name__ == "__main__":
    # Paths to the image files
    input_image_path = "E:/DIP PCA1/inputImage/inputOne.jpg"
    save_image_path = "E:/DIP PCA1/savedImage/savedOne.jpg"

    crop_area = (100, 100, 500, 500)
    # Rotation angle in degrees
    rotation_angle = -45
    # Resize dimensions (width, height)
    resize_dimensions = (150, 150)

    # Crop, Rotate, Resize an image
    crop_rotate_resize_image(input_image_path, crop_area, rotation_angle, resize_dimensions, save_image_path)
