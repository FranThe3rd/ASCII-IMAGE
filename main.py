from PIL import Image
import random
import os
import time


def get_image():
    """
     This function has three variables called 'new_list', 'file_list', and 'new_directory'. The 'file_list'
     variable's function searches through the PyCharm image folder and retrieve all the files that
     contain the letters png or jpeg at their ends which returns a list(example:['cheese.png','cat.png']).
     The only problem was for in order for the 'image_randomizer()' function to work, it needed the
     file directory to start with 'image/'. So in order to do that, I made a for loop that
     iterated through the file_list variable, and concatenated it with a string that started
     with 'images/' and assigned that with a variable called 'new_directory'. That's where my
     'new_list' variables comes in and appends the 'new_directory' variable to itself. Which then
     returns (example:['images/cheese.png','images/cat.png']).
    """

    new_list = []
    file_list = [file for file in os.listdir('images') if file.endswith('.png') or file.endswith('.jpg')]
    for file in file_list:
        new_directory = 'images/' + file  # concatenation
        new_list.append(new_directory)
    return new_list


def image_randomizer():
    """
   This was a straightforward function, and I made sure to import the random module
   so that the program would select a random image each time it ran. To accomplish
   that, I created a brand-new variable called 'random_img' and added the random.choice() method,
   which accepts a list from the 'get_image()' function, which will return a random item from
   the list.
    """
    random_img = random.choice(get_image())
    return random_img


def choose_image():
    """
    I developed this function that lets you select up to three images from the folder rather than
    getting a random image. In order to organize the 'choose_image()' function, I iterated through
    the list after setting the 'get image' variable into the 'list' variable. This allowed me to number
    the names of the images.
    """
    print('')
    list = get_image()
    for index, val in enumerate(list, start=1):
        print(f'{index}. {val[7:]}')
    answer = int(input('\nChoose Your Image: '))
    options = [1,2,3,4,5,6,7,8,9,10]
    while answer not in options:
        answer = int(input("Type '1','2','3: "))
    return list[answer - 1]


def convert_grey(image):
    """
       Another straightforward function, it uses the image parameter and
       converts it to black and white by using "convert('L')" method.
    """
    grey_image = image.convert('L')
    return grey_image


def ascii_values():
    """
     The two variables in this function are 'new_list' and 'ascii_list'. I couldn't really find out
     how to simply get all the ascii values inside of a list, which is why I have two lists.
     To obtain the ascii values from the range of numbers 33,125, I therefore created "new_list," and I
     used "chr" method to transform the numbers that were appended to "new_list" into ascii characters.
     Which I ultimately added to my "ascii list"

    """
    new_list = []
    ascii_list = []
    for i in range(33, 125):
        new_list.append(i)
    for char in new_list:
        char = chr(char).strip()
        ascii_list.append(char)
    return ascii_list


def resize(image):
    '''
    To be able to alter the image's width and height,
    I built this function. The code itself explains everything,
    it takes two inputs and uses the '.resize' method to adjust
    the image's size, but I had to assign it with a new variable
    in order to work.
    '''

    width = int(input('width: '))
    height = int(input('height: '))
    new_image = image.resize((width, height))

    return new_image


def main_menu():
    '''
    Just the main menu, you are allowed to choose the image, or just get a random selection.
    '''

    print("-----------------------------------")
    print("------------ MAIN MENU ------------")
    print("-----------------------------------")
    print("C. Chooose Image")
    print("R. Randomize Image")
    print("Q. Quit")
    print()


# It turns out to look weird in the text file, not sure how to make the font look way smaller.
# It does work though on windows notepad. I copied my code and tried it on my windows desktop, looks good when you zoom out.

def main():
    '''
    You have the choice to select your image manually using this main function, or automatically using a
    random selection. Depending on your decision, you will have the option to alter the image's width
    before receiving the finished ascii image in a different text file.
    '''
    main_menu()

    answer = input('Answer: ')
    while answer != 'c' and answer != 'r' and answer != 'q':
        answer = input("Type 'c','r','q: ")

    if answer == 'r':
        data1 = image_randomizer()
        stock_img = Image.open(data1)
        stock_img = convert_grey(stock_img)
        print('Before We Start, We Will Ask For The Width And Height Of The Image')
        counter = 2
        while counter > 0:
            time.sleep(1)
            counter -= 1
        img = resize(stock_img)
        print(f'Your chosen width and height is {img.size}')

        chars = ascii_values()  # gets ascii list
        width, height = img.size  # creates width and height variable
        pixels = img.getdata()  # returns values of pixel values in numbers
        new_pixels = [chars[pixel // 50] for pixel in
                      pixels]  # This replaces the values of the numbers with the ascii values.
        new_pixels = ''.join(new_pixels)  # joins them together
        new_pixels_length = len(new_pixels)  # length of the new_pixels

        ascii_image = [new_pixels[index:index + width] for index in
                       range(0, new_pixels_length, width)]  # creates the shape of the image by the width
        ascii_image = '\n'.join(ascii_image)  # eventually joins them togehter

        with open('ascii image random.txt', 'w') as new_image:  # creates a new file for it
            new_image.write(ascii_image)



    elif answer == 'c':
        data2 = choose_image()
        stock_img = Image.open(data2)
        stock_img = convert_grey(stock_img)
        print('Before We Start, We Will Ask For The Width And Height Of The Image')
        counter = 2
        while counter > 0:
            time.sleep(1)
            counter -= 1
        img = resize(stock_img)
        print(f'Your chosen width and height is {img.size}')

        chars = ascii_values()  # same thing explained above
        width, height = img.size
        pixels = img.getdata()
        new_pixels = [chars[pixel // 50] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        new_pixels_length = len(new_pixels)

        ascii_image = [new_pixels[index:index + width] for index in range(0, new_pixels_length, width)]
        ascii_image = '\n'.join(ascii_image)

        with open('ascii image chosen.txt', 'w') as new_image:  # creates a new file for it
            new_image.write(ascii_image)

    else:
        print('You exited the program')


if __name__ == '__main__':
    main()
