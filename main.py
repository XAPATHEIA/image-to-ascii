from PIL import Image

g_scale1 = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "
g_scale_map = g_scale1[::-1]


# Check path eligibility.
def path_check():
    return input("Input the path of the image you would like to convert:\n")

# Open image and convert to grayscale.
def grayscale():
    try:
        return Image.open(path_check()).convert('L')
    except FileNotFoundError:
        print("Invalid Input.")
        exit()


def resize(image):
    try:
        new_width = int(input("Width of ASCII image: "))
    except ValueError as V:
        print(V)
    else:
        original_width, original_height = image.size
        aspect_ratio = original_height / original_width
        new_height = aspect_ratio * new_width
        new_dimensions = (int(new_width), int(new_height))
        return image.resize(new_dimensions), new_width


def pixel_to_ASCII(image):
    pixel_data = list(image.getdata())
    new_pixel_data = [g_scale_map[int(pixel_value // 4)] for pixel_value in pixel_data]
    return ''.join(new_pixel_data)


def main():
    grayscale_image, user_width = resize(grayscale())
    gray_pixels = pixel_to_ASCII(grayscale_image)
    new_image = [gray_pixels[index:index + user_width] for index in range(0, len(gray_pixels), user_width)]

    print('\n'.join(new_image))
    input("Press 'ENTER' to exit.")


main()