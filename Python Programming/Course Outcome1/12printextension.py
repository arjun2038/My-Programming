filename = input("Enter a filename : ")
position = filename.rfind(".")
extension = filename[position:]
print("The extension of the file is ",extension[1:])
