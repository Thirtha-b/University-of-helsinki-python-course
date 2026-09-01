course=int(input("How many students on the course?"))
size=int(input("Desired group size?"))
print(f"Number of groups formed: {(course+size-1)//size}")
