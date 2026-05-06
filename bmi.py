def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height **2)
    print("Your bmi is: ", bmi)
    if bmi<18.5:
        print("Under Weight")
    elif bmi<= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")
        
    return 0
calculate_bmi(weight=94, height=1.76)

