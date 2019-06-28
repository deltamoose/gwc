from PIL import Image

import filters
def main():
    pass

if __name__ == "__main__":
    main()

picture = input("Please choose a photo to edit.  Type stitch, thanos, or obama to edit a picture.  ")

if picture == "stitch" or picture == "Stitch":
    img = Image.open("stitch.jpg")
    show_img("stitch.jpg")
    print(img.filename)
    print(img.size)
elif picture == "thanos" or picture == "Thanos":
    img = Image.open("thanos.jpg")
    show_img("thanos.jpg")
    print(img.filename)
    print(img.size)
elif picture == "obama" or picture == "Obama":
    img = Image.open("obama.jpg")
    show_img("obama.jpg")
    print(img.filename)
    print(img.size)
else:
    print("Please input a valid string.  ")
    quit()









