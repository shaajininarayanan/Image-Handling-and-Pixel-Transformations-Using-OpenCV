
# Image Handling and Pixel Transformations Using OpenCV

## Experiment No. 01

### Aim
To read, display and process images using Python and OpenCV, including brightness and contrast adjustment, color channel separation, geometric transformations, image annotation and bitwise operations.

### Software Requirements
- Python 3
- OpenCV
- NumPy
- Matplotlib
- Jupyter Notebook

### Input Images
- Eagle_in_Flight.jpg
- Apollo-11-launch.jpg
- Boy.jpg

### Algorithm
1. Read and display the Eagle image in grayscale.
2. Display the image dimensions and channel count.
3. Save the grayscale image and convert it into a three-channel image.
4. Crop, resize and flip the image horizontally.
5. Read the Apollo launch image and annotate it with text and a magenta rectangle.
6. Read Boy.jpg and adjust its brightness.
7. Generate lower-contrast and higher-contrast images.
8. Split the image into Blue, Green and Red channels.
9. Merge and display the RGB channels.
10. Split and merge the Hue, Saturation and Value channels.
11. Apply a bitwise AND operation using a mask.
12. Save the processed images in the outputs folder.

### Installation
```bash
python -m pip install -r requirements.txt
```

### How to Run
```bash
python main.py
```

Make sure all three input images are available in the images folder.

### Output
The program displays grayscale images, geometric transformations, annotated images, brightness and contrast variations, color channels and the bitwise AND result.

### Result
Image handling and pixel transformation operations were implemented using Python and OpenCV.
