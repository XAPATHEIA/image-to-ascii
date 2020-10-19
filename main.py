from PIL import Image

g_scale1 = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "
g_scale_map = g_scale1[::-1]


# Open image and convert to grayscale.
def grayscale():
    return Image.open('roadster.jpg').convert('L')  # change to path_check()


# Check path eligibility.
def path_check():
    try:
        path = input("Input the path of the image you would like to convert:\n")
    except FileNotFoundError:
        print("Could not locate image.")
    else:
        return path


def resize(image):
    try:
        new_width = int(input("Width of ASCII image: "))
    except ValueError as V:
        print(V)
    else:
        original_width, original_height = image.size
        aspect_ratio = original_width / original_height
        new_height = aspect_ratio * new_width
        new_dimensions = (new_width, new_height)
        return image.resize(new_dimensions)




pixel_data = o_img.getdata()
