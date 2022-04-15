from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
print(img.size)
img.thumbnail((400,400)) #width height (maximum 400)
img.save("thumbnail.jpg")
print(img.size)


# filtered_img = img.convert('L')
# box=(100,100,400,400)
# region = filtered_img.crop(box)
# # crooked = filtered_img.resize((300,300))
# region.save("face.png",'png')
