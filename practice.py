# AB, Reading and Writting to Files

with open("practice.txt", "r") as file:
    content= file.read()
    content= content + "/nWinnie the Pooh"
    print(content)

with open("practice test", "w") as file:
    file.write("Winnie the Pooh and the Blustering Day ")
    