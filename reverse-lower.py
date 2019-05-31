from PIL import Image, ImageDraw



for i in range(1,28):

    last = 56

    in_num = "%03d"%i
    out_num = "%03d"%(last-i)

    in_path = "lower/" + in_num + ".png"
    out_path = "lower/" + out_num + ".png"

    img = Image.open(in_path)


    # img.show()
    img.save(out_path, quality=100)

    print(in_path)
    print(out_path)
    print("-")



print("Finish!!")