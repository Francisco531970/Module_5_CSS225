# Francisco Sanchez
# 10/28/23

counter = 1
while counter <= 50:
    if counter % 3 == 0 and counter % 5 == 0:
        print("Divisible by both")
    elif counter % 3 == 0:
        print("Divisible by three")
    elif counter % 5 == 0:
        print("Divisible by five")
    else:
        print(counter)

    counter += 1