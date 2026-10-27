# Image-Handling-and-Pixel-Transformations-Using-OpenCV

## AIM:
Write a Python program using OpenCV that performs the following tasks:

- Read and Display an Image.
- Adjust the brightness of an image.
- Modify the image contrast.
- Generate a third image using bitwise operations.

## Software Required:
- Anaconda - Python 3.7
- Jupyter Notebook (for interactive development and execution)

## Algorithm:

**Step 1:**  
Load an image from your local directory and display it.

**Step 2:**  
Create a matrix of ones (with data type float64) to adjust brightness.

**Step 3:**  
Create brighter and darker images by adding and subtracting the matrix from the original image. Display the original, brighter, and darker images.

**Step 4:**  
Modify the image contrast by creating two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix). Display the original, lower contrast, and higher contrast images.

**Step 5:**  
Split the image (`Boy.jpg`) into B, G, R components and display the channels.

## Program Developed By:

**Name:** Shaajini N

**Register Number:** 212225040395

## Ex. No. 01

### 1. Read the image (`Eagle_in_Flight.jpg`) using OpenCV `imread()` as a grayscale image.
```python
# YOUR CODE HERE
```

### 2. Print the image width, height & channel.
```python
# YOUR CODE HERE
```

### 3. Display the image using Matplotlib `imshow()`.
```python
# YOUR CODE HERE
```

### 4. Save the image as a PNG file using OpenCV `imwrite()`.
```python
# YOUR CODE HERE
```

### 5. Read the saved image above as a color image using `cv2.cvtColor()`.
```python
# YOUR CODE HERE
```

### 6. Display the colour image using Matplotlib `imshow()` and print the image width, height & channel.
```python
# YOUR CODE HERE
```

### 7. Crop the image to extract any specific object (Eagle alone) from the image.
```python
# YOUR CODE HERE
```

### 8. Resize the image up by a factor of 2x.
```python
# YOUR CODE HERE
```

### 9. Flip the cropped/resized image horizontally.
```python
# YOUR CODE HERE
```

### 10. Read in the image (`Apollo-11-launch.jpg`).
```python
# YOUR CODE HERE
```

### 11. Add the following text to the dark area at the bottom of the image (centered on the image).
```python
text = 'Apollo 11 Saturn V Launch, July 16, 1969'
font_face = cv2.FONT_HERSHEY_PLAIN

# YOUR CODE HERE: use putText()
```

### 12. Draw a magenta rectangle that encompasses the launch tower and the rocket.
```python
rect_color = (255, 0, 255)  # Magenta in BGR format

# YOUR CODE HERE
```

### 13. Display the final annotated image.
```python
# YOUR CODE HERE
```

### 14. Read the image (`Boy.jpg`).
```python
# YOUR CODE HERE
```

### 15. Adjust the brightness of the image. Create a matrix of ones with data type `float64`.
```python
# matrix_ones =

# YOUR CODE HERE
```

### 16. Create brighter and darker images.
```python
img_brighter = cv2.add(img, matrix)
img_darker = cv2.subtract(img, matrix)

# YOUR CODE HERE
```

### 17. Display the images (Original Image, Darker Image, Brighter Image).
```python
# YOUR CODE HERE
```

### 18. Modify the image contrast. Create two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix).
```python
matrix1 = 
matrix2 = 

# img_higher1 =
# img_higher2 =

# YOUR CODE HERE
```

### 19. Display the images (Original, Lower Contrast, Higher Contrast).
```python
# YOUR CODE HERE
```

### 20. Split the image (`Boy.jpg`) into B, G, R components and display the channels.
```python
# YOUR CODE HERE
```

### 21. Merge the R, G, B channels and display them along with the original image.
```python
# YOUR CODE HERE
```

### 22. Split the image into H, S, V components and display the channels.
```python
# YOUR CODE HERE
```

### 23. Merge the H, S, V channels and display them along with the original image.
```python
# YOUR CODE HERE
```

## Output:

i) Read and Display an Image.

ii) Adjust Image Brightness.

iii) Modify Image Contrast.

iv) Generate Third Image Using Bitwise Operations.

## Result:

Thus, the images were read, displayed, brightness and contrast adjustments were made, and bitwise operations were performed successfully using the Python program.
