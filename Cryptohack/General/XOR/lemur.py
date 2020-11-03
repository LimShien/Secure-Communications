#https://stackoverflow.com/questions/45544755/convert-image-into-hexadecimal-format-with-python
""" import binascii
from pwn import xor
filename1= 'flag_7ae18c704272532658c10b5faad06d74.png'
with open(filename1, 'rb') as f:
    content1 = bytearray(f.read())
filename2 = "lemur_ed66878c338e662d3473f0d98eedbd0d.png"
with open(filename2, 'rb') as f:
    content2 = bytearray(f.read())
hint=bytes("crypto{","utf-8")

print(content1)
 """

#https://www.geeksforgeeks.o#rg/python-pil-logical_xor-and-invert-method/
from PIL import Image, ImageChops
from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import xor
im1 = Image.open('flag_7ae18c704272532658c10b5faad06d74.png').convert("1")
img2 = Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png').convert("1")

ImageChops.logical_xor(im1, img2).save("result.png")
ImageChops.logical_and(ImageChops.logical_xor(im1, img2), img2).save("result2.png")



filename1= 'result.png'
with open(filename1, 'rb') as f:
    content1 = bytes(f.read())
filename2= 'flag_7ae18c704272532658c10b5faad06d74.png'
with open(filename2, 'rb') as f:
    content2 = bytes(f.read())
filename3= 'lemur_ed66878c338e662d3473f0d98eedbd0d.png'
with open(filename3, 'rb') as f:
    content3 = bytes(f.read())
