def calculate_bmi(height, weight):
   

    # Calculate BMI
    bmi = weight / (height * height)

    # Display the calculated BMI
    print("BMI = " + str(bmi))

    # Determine weight classification
    weight_classification = ""
    if bmi < 18.5:
        weight_classification = "Under Weight"
    elif 18.5 <= bmi <= 25.0:
        weight_classification = "Normal Weight"
    else:
        weight_classification = "Over Weight"

    # Determine weight classification code
    weight_classification_code = -1
    if bmi < 18.5:
        weight_classification_code = 0
    elif 18.5 <= bmi <= 25.0:
        weight_classification_code = 1



    # Return the BMI, weight classification, weight classification code, and health risk
    return bmi, weight_classification, weight_classification_code

bmi, weight_classification, weight_classification_code,  = calculate_bmi(weight=57, height=1.73)

print("BMI:", bmi)
print("Weight classification:", weight_classification)
print("Weight classification code:", weight_classification_code)