# challenge 1
import os

files = os.listdir("fichiers") #return liiist 
print(files)

for file in files:
    if file.endswith(".txt"):
        print(file)
        
fiile = open("file1.txt","r")
content = fiile.read()
print(content)

with open("file1.txt","r") as file :
        content = file.read()
        print(content)
        
with open("file2.txt", "w") as file :
        file.write("Heeelllloooo agaiiiin ")
        file.write("let's do it ")
        file.write("code agaiiiin")
        
      

with open("file2.txt","r") as file :
        content = file.read()
        print(content)


## challenge 2

print(os.path.exists("fichiers/config.yaml"))

if os.path.exists("fichiers/config.yaml"):
    with open("file1.txt" , "r") as file:
        cnt = file.read()
        print(cnt)
else:
    print("file not fouund")
    
    
    
#  challenge 4
import shutil

#os.mkdir("newfile")
#reps = ["file4.py","file5.txt","file6.txt"]

#for re in reps:
 # os.mkdir(re,exist_ok=True)



# challenge 5

#with open("file1.txt" , "r") as file:
   # if file.endswith(".txt")
   # shutil.copy(file,"newfile/")
   
fichiers = os.listdir("fichiers")
print(fichiers)


for fichier in fichiers:
    if fichier.endswith(".txt"):
            shutil.copy(f"fichiers/{fichier}","newfile/")
            
            
words = ["Hello", "World", "Python", "Fichier", "lets do it"]


with open("fichiers/file1.txt", "w") as file:
    for word in words:
        file.write(word + "\n")


with open("fichiers/file1.txt", "r") as file:
    contenu = file.read()
    print(contenu)