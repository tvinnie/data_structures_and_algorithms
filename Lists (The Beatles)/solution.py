# step 1
beatles = []

#step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

#step 3
new = ["Stu Sutcliffe","Pete Best"]
for n in new:
    beatles.append(new)
#step 4   
del beatles[-1]
del beatles[-1]

# step 5
beatles.insert(0,'Ringo Starr')

print("The Fab:", beatles)
