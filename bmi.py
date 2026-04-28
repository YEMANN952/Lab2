def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Wight =" + str(weight))
    
    bmi=weight/(height*height)
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("Classification: Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Classification: Normal Weight")
    else:
        print("Classification: Overweight")
calculate_bmi(weight=57, height=1.73)