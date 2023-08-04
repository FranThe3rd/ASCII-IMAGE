# ASCII Image Converter 

This repository contains a Python script that allows you to generate ASCII art images from PNG and JPEG files. The script utilizes the Python Imaging Library (PIL) to process images and convert them into ASCII representations. Below is a breakdown of the main functions and their functionalities:

## `get_image()`

This function retrieves a list of image file paths from the 'images' directory. It scans through the directory and filters files that have '.png' or '.jpg' extensions. The function then constructs a new list containing the formatted image paths, starting with 'images/'.

## `image_randomizer()`

This function randomly selects an image file path from the list obtained using the `get_image()` function. It imports the `random` module to ensure a random image is chosen each time the function is called.

## `choose_image()`

This function allows the user to manually select an image from the 'images' directory. It calls the `get_image()` function to retrieve the list of image paths and presents a numbered list of options for the user to choose from. The user's input is validated to ensure a valid choice.

## `convert_grey(image)`

This function converts a given input image to grayscale using the 'convert' method from PIL. The resulting grayscale image is returned.

## `ascii_values()`

This function generates a list of ASCII characters corresponding to numeric values in the range 33 to 124. It uses a loop to populate the `new_list` with integer values and then converts each value to its ASCII character using the `chr()` method. The ASCII characters are stored in the `ascii_list`.

## `resize(image)`

This function allows the user to resize an input image. The user is prompted to provide the desired width and height. The function then resizes the image using the 'resize' method from PIL and returns the resized image.

## `main_menu()`

Displays the main menu options for the program, including selecting an image, generating a random image, and quitting the program.

## `main()`

The main function that orchestrates the program's functionality. It presents the user with the main menu and prompts them to choose an option. Depending on the user's choice, the function either generates a random ASCII image or allows the user to select an image. It then converts the chosen image to grayscale, resizes it, converts pixel values to ASCII characters using the `ascii_values()` function, and arranges the ASCII characters into an image-like format. Finally, it writes the ASCII representation to a text file.

Please note that the code assumes the existence of an 'images' directory containing the image files. Make sure you have the required images in this directory before running the script.

To run the program, execute the `main()` function at the bottom of the script. Follow the on-screen instructions to choose an image and customize the ASCII output. The resulting ASCII art will be saved in a text file.


