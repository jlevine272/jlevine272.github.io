from PIL import Image
import os
import sys

def crop_image_to_aspect_ratio(image_path, output_path, aspect_ratio):
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        target_width, target_height = aspect_ratio

        # Calculate the target height to maintain the aspect ratio
        new_height = int(img_width * (target_height / target_width))

        if new_height <= img_height:
            # Crop the image along the height to the new height, centering the crop
            top = (img_height - new_height) // 2
            bottom = top + new_height
            cropped_img = img.crop((0, top, img_width, bottom))
        else:
            # If the calculated height is more than the image height, adjust width instead
            new_width = int(img_height * (target_width / target_height))
            left = (img_width - new_width) // 2
            right = left + new_width
            cropped_img = img.crop((left, 0, right, img_height))

        cropped_img.save(output_path)

def crop_images_in_directory(directory, fnames=None, aspect_ratio=(353, 326)):
    valid_extensions = ('.jpg', '.jpeg', '.JPG', '.png')

    if specific_files:
        files_to_process = fnames
    else:
        files_to_process = [f for f in os.listdir(directory) if f.endswith(valid_extensions)]

    for filename in files_to_process:
        if filename.endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}_cropped{os.path.splitext(filename)[1]}")
            crop_image_to_aspect_ratio(image_path, output_path, aspect_ratio)
            print(f"Cropped image saved to: {output_path}")

# Specify your directory here
if __name__ == "__main__":
    """ Example use:
    >>>python create_tiles.py clevr_sample.jpg
    Cropped image saved to: images\clevr_sample_cropped.jpg
    """
    # If command line arguments are provided, use them as specific file paths
    # The first argument is always the script name, so we skip it
    specific_files = sys.argv[1:]

    # Specify your directory here
    directory = 'images'

    if specific_files:
        # Process only the specified files
        crop_images_in_directory(directory, fnames=specific_files)
    else:
        # Process the entire directory
        crop_images_in_directory(directory)
