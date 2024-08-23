import tkinter as tk

def collect_inputs():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        imc = weight / (height ** 2)
        
        print(f"Your imc is: {imc:.2f}")
        imc_element.config(text=" You're underweight")
          
      
        if imc < 18.5:
            print("You are underweight")
            imc_element.config(text="You're underweight")
            imc_element2.config(text="Inadequate body weight\n can result in lower energy levels,\n fatigue, and decreased\n physical and mental performance. ")
            imc_element3.config(text="A low body weight\n can increase the risk\n of osteoporosis and fractures \ndue to insufficient bone density. ")
        elif 18.5 <= imc < 25:
            print("healthy, congratulations")
            imc_element.config(text="You're healthy, keep going!")
            imc_element2.config(text="Maintaining a healthy BMI reduces \n the risk of cardiovascular diseases\n like heart attacks and strokes.")
            imc_element3.config(text="Maintaining a healthy BMI can lead\n to improved sleep quality\n and overall restfulness.")
        elif 25 <= imc < 30:
          imc_element.config(text="Overweight")
          imc_element2.config(text=" Excess weight is a significant risk \nfactor for sleep apnea\n, a condition where\n breathing stops and starts during sleep.")
          imc_element3.config(text="Being overweight can \n negatively impact self-esteem and \nbody image, which can affect overall mental well-being.")
        else:
            imc_element.config(text="You're obese")
            imc_element2.config(text="Extra weight puts significant\n stress on joints, particularly in weight-bearing\n areas like the knees and hips, \nleading to osteoarthritis.")
            imc_element3.config(text="Obesity can lead to poor sleep\n quality and increase the likelihood of\n sleep disturbances.")


    except ValueError:
        print("Invalid input. Please enter numeric values.")

root = tk.Tk()

root.title("Imc calculator")
root.geometry("500x500")

text1 = tk.Label(root, text="Put here your height (Example: 1.70)", font=("Yu Gothic UI", 20))
text1.pack(pady=20)

entry_height = tk.Entry(root, font=("Yu Gothic UI", 15))
entry_height.pack(pady=20)

text2 = tk.Label(root, text="Put here your weight (Example: 80)", font=("Yu Gothic UI", 15))
text2.pack(pady=20)

entry_weight = tk.Entry(root, font=("Yu Gothic UI", 15))
entry_weight.pack(pady=20)

button1 = tk.Button(root, text="Submit", command=collect_inputs, font=("Yu Gothic UI", 15))
button1.pack(pady=20)

imc_element = tk.Label(root, text="", font=("Yu Gothic UI", 18))
imc_element.pack(pady=20)

imc_element2 = tk.Label(root, text="", font=("Yu Gothic UI", 18))
imc_element2.pack(pady=20)

imc_element3 = tk.Label(root, text="", font=("Yu Gothic UI", 18))
imc_element3.pack(pady=20)

root.mainloop()
