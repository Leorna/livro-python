import os


total_size = 0


for file_name in os.listdir("/home/gabriel"):
    total_size += os.path.getsize(os.path.join("/home/gabriel", file_name))


print("{} bytes".format(total_size))
