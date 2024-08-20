print("Hello, welcome to the Imc calculator")
height = float(input("Put here your height. Example: 1.75 \n "));
weight = float(input("Now, put yoy weight here. Example: 80 \n "));

imc = weight / (height ** 2)




print("you Imc is: " + str(int(imc)))

if imc < 18.5:
    print("Underweight")
    print("Inadequate body weight can result in lower energy levels, fatigue, and decreased physical and mental performance. \n")
    print("A low body weight can increase the risk of osteoporosis and fractures due to insufficient bone density. \n")
    print("Being underweight can lead to deficiencies in essential nutrients, which may affect your overall health and immune system.")

elif 18.5 <= imc < 25:
    print("Healthy weight")
    print("A healthy weight is associated with a lower risk of chronic diseases such as heart disease, diabetes, and hypertension. \n")
    print("Maintaining a healthy weight can help sustain good energy levels and overall vitality. \n")
    print("A healthy weight supports normal bodily functions, including efficient digestion, hormonal balance, and cognitive performance. \n")

elif 25 <= imc < 30:
    print("Overweight")
    print("Being overweight increases the risk of developing chronic conditions such as type 2 diabetes, heart disease, and high blood pressure. \n")
    print(" Overweight individuals are at higher risk for sleep apnea and other sleep-related disorders. \n")
    print("Overweight can affect mental health, leading to issues such as low self-esteem and depression. \n")

else:
    print("Obesity significantly increases the risk of developing serious health conditions such as heart disease, stroke, type 2 diabetes, and certain cancers. \n")
    print("Excess weight can impact mobility and physical activity, leading to reduced quality of life and physical discomfort. \n")
    print("Obesity is associated with metabolic syndrome, which includes conditions like high blood pressure, high blood sugar, and abnormal cholesterol levels. \n")
