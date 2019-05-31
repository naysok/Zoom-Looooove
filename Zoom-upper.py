from PIL import Image, ImageDraw

set_window = 1080
set_size = 950
set_position = int(set_window/2 - set_size/2)



for i in range(1, 29):

    set_size = 950 + i*35
    set_position = int(set_window/2 - set_size/2)

    in_path = "upper/" + "%03d"%(i-1) + ".png"
    out_path = "upper/"+ "%03d"%i + ".png"

    img = Image.open(in_path)


    paste_img = Image.open("src/Love.png")
    paste_img_resize = paste_img.resize((set_size, set_size), Image.LANCZOS)
    mask = paste_img_resize.split()[3]



    img.paste(paste_img_resize, (set_position, set_position), mask)


    # img.show()
    print("save :", i)
    img.save(out_path, quality=100)
