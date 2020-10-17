from PIL import Image

g_scale1 = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "
g_scale_map = []

for i in range(1, len(g_scale1)+1):
    g_scale_map.append(g_scale1[-i])



def path_check():
    try:
        path = input("Input the path of the image you would like to convert:\n")
    except FileNotFoundError:
        print("Could not locate image.")
    else:
        return path


# Open original image and convert to grayscale.
o_img = Image.open('roadster.jpg').convert('RGB')          # change to path_check()
W, H = o_img.size
data = o_img.load

pixel_data = o_img.getcolors(W * H)

average_gs = []

for ipc in pixel_data:
    average_gs.append(round(sum(ipc[1]) / len(ipc[1])))

for


