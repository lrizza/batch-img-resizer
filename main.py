from PIL import Image
from tqdm import tqdm
import os
from multiprocessing import Pool, cpu_count

# Paths to input and output folders
input_folder = "/home/lrizza/Documents/Datasets/montauk/camera_panos_common"
output_folder = "/home/lrizza/Documents/Datasets/montauk/A"
new_size = (512, 512)  # Define the new size (width, height)

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get list of image files
image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
filenames = [
    filename
    for filename in os.listdir(input_folder)
    if filename.lower().endswith(image_extensions)
]


def process_image(filename):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)
    try:
        with Image.open(input_path) as img:
            # Optionally, you can specify a faster resampling filter
            resized_img = img.resize(new_size, resample=Image.BILINEAR)
            resized_img.save(output_path)
    except Exception as e:
        print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    # Use all available CPU cores
    num_workers = cpu_count()
    with Pool(processes=num_workers) as pool:
        # Use tqdm to display the progress bar
        list(tqdm(pool.imap_unordered(process_image, filenames), total=len(filenames)))

    print("All images resized successfully.")
