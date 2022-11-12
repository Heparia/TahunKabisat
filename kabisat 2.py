while True:
    year = int(input("Enter a number : "))
    if year %4 !=0:
        print ("bukan kabisat")
    elif year %100 !=0:
        print ("kabisat")
    elif year %400 !=0:
        print ("bukan kabisat")
    else:
        print ("kabisat")
