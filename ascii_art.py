from PIL import Image

filePath = "./flagMorrocco.png"
img = Image.open(filePath)
img = img.convert("L")
img = img.convert("L")
img = img.resize((50,16)) #resize the img

# userVersion = 1 #version1 --> replace darker areas with whiter
userVersion = 2 #version1 --> replace whiter areas with darker

# chars = ['@', '#', '8', '&', '%', '$', '*', 'W',
#            '?', '+', '=', '~', '-', 
#          '_', ':', ';', ',', '.', ' ']

chars = list("@%#*+=-:. ")


if userVersion == 1:
    chars = chars[:]
elif userVersion == 2:
    chars = chars[:][::-1]
    

pixels = list(img.getdata())
width, height = img.size

ascii_img = ""
for j in range(height):
    for i in range(width):
        pixel = pixels[i + width * j]
        index = int(pixel / 255 * (len(chars) - 1)) #return the index value of the coresponded assci char based on the len of the list of chars i define earlier
        # exampl if the pixel is 255 (white) it means we are returning the asscii char in the last index of ascii chars list (.)
        ascii_img += chars[index]
            
            
    ascii_img += "\n"

print(ascii_img)