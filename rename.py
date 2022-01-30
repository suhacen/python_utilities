import os
for file in os.listdir("."):
    if file.endswith(".ncm"):
        my_file = file
        base = os.path.splitext(my_file)[0]
        os.rename(my_file, base + '.mp3')
        print(os.path.join(".", file))