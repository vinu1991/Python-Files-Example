import os
for root, folders, files in os.walk("."):
    for filename in files:
        print (root, filename)