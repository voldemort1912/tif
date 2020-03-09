from PIL import Image

image = Image.open("test.tiff")
image2 = image.convert('RGB')

image2.save("test.jpg", 'JPEG', quality=100)
