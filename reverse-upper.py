from PIL import Image, ImageDraw



for i in range(1,30):

    last = 58

    in_num = "%03d"%i
    out_num = "%03d"%(last-i)

    in_path = "upper/" + in_num + ".png"
    out_path = "upper/" + out_num + ".png"

    img = Image.open(in_path)


    # img.show()
    img.save(out_path, quality=100)

    print(in_path)
    print(out_path)
    print("-")



print("Finish!!")