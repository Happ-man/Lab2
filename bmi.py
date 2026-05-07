def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height **2)
    print("Your bmi is: ", bmi)
    if bmi<18.5:
        print("Under Weight")
        return -1
    elif bmi<= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1
        
calculate_bmi(weight=94, height=1.76)

