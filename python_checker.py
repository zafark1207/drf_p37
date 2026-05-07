from base64 import b64encode, b64decode


# with open('image.jpg', 'rb') as f, open('rasm.txt', 'w') as f2:
#
#     # print(b64encode(f.read()).decode())
#
#     f2.write(b64encode(f.read()).decode())


with open('yangi_rasm.jpg', 'wb') as f, open('rasm.txt', 'r') as f2:
    f.write(b64decode(f2.read().encode()))
