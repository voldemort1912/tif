from PIL import Image

image = Image.open("6010_0_0_A.tif")
image2 = image.convert('RGB')

image2.save("test.jpg", 'JPEG', quality=100)
