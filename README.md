## Overview
Simple script to rapidly resize a directory of images to a specified size. Uses multiprocessing for performance.

## Usage
Install required dependencies in requirements.txt, options are passed as arguments:
```
usage: main.py [-h] -i INPUT_FOLDER -o OUTPUT_FOLDER -s width height

Resize images in a folder.

options:
  -h, --help            show this help message and exit
  -i INPUT_FOLDER, --input_folder INPUT_FOLDER
                        Path to the input folder containing images.
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Path to the output folder for resized images.
  -s width height, --new_size width height
                        New size for the images (width height).
```

## Example
Resize images to 512x512:

`python resizer.py -i "/data/input" -o "data/output" -s 512 512`