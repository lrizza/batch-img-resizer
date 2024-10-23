from PIL import Image
from tqdm import tqdm
import os
import argparse
from multiprocessing import Pool, cpu_count


def process_image(args):
    filename, input_folder, output_folder, new_size = args
    input_path = os.path.join(input_folder, filename)
    output_filename = f"{filename}"
    output_path = os.path.join(output_folder, output_filename)
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize(new_size, resample=Image.BILINEAR)
            resized_img.save(output_path)
    except Exception as e:
        print(f"Error processing {filename}: {e}")


def main(input_folder, output_folder, new_size):
    print(output_folder)

    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    filenames = [
        filename
        for filename in os.listdir(input_folder)
        if filename.lower().endswith(image_extensions)
    ]

    num_workers = cpu_count()
    # Prepare the arguments for each image
    args_list = [
        (filename, input_folder, output_folder, new_size) for filename in filenames
    ]

    with Pool(processes=num_workers) as pool:
        list(tqdm(pool.imap_unordered(process_image, args_list), total=len(args_list)))

    print("All images resized successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images in a folder.")
    parser.add_argument(
        "-i",
        "--input_folder",
        type=str,
        required=True,
        help="Path to the input folder containing images.",
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        required=True,
        help="Path to the output folder for resized images.",
    )
    parser.add_argument(
        "-s",
        "--new_size",
        type=int,
        nargs=2,
        metavar=("width", "height"),
        required=True,
        help="New size for the images (width height).",
    )
    args = parser.parse_args()
    os.makedirs(args.output_folder, exist_ok=True)

    if not os.path.isdir(args.input_folder) and not os.path.exists(args.input_folder):
        print(f"Input folder {args.input_folder} does not exist.")
        exit(1)
    if not os.path.isdir(args.output_folder) and not os.path.exists(args.output_folder):
        print(f"Output folder {args.output_folder} does not exist.")
        exit(1)

    main(args.input_folder, args.output_folder, tuple(args.new_size))
