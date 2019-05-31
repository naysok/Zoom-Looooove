from PIL import Image, ImageDraw

set_window = 1080
set_size = 950
set_position = int(set_window/2 - set_size/2)

img = Image.new("RGBA", (set_window, set_window), (255, 255, 255, 255))


paste_img = Image.open("src/Love.png")
paste_img_resize = paste_img.resize((set_size, set_size), Image.LANCZOS)
mask = paste_img_resize.split()[3]



img.paste(paste_img_resize, (set_position, set_position), mask)


# img.show()

out_path = "upper/000.png"
# out_path = "lower/000.png"

img.save(out_path, quality=100)
