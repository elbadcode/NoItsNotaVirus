import os

with open(os.path.join(os.getcwd(), "helloworld.txt"), "w") as f:
	f.write("Hello World")
	f.seek(0)
	f.close()