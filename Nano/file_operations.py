# OPEN AND CLOSE FILES 
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
print(file_data)
f.close()

# WRITING TO FILES
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

# OPEN FILES WITH AUTO-CLOSE FEATURE
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

    