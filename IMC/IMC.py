def categorize_weight(imc):
    if imc < 18.5:
        category = "Your body composition is: Underweight"
    elif imc < 25:
        category = "Your body composition is: Normal weight"
    elif imc < 30:
        category = "Your body composition is: Overweight"
    elif imc < 35:
        category = "Your body composition is: Obesity Class 1"
    elif imc < 40:
        category = "Your body composition is: Obesity Class 2"
    else:
        category = "Your body composition is: Obesity Class 3"
    print(category)

def calculate_IMC(weight, height):
    imc = weight / ((height / 100) ** 2)
    print("Your Body Mass Index is:", imc)
    categorize_weight(imc)

def main():
    print("Let's calculate the Body Mass Index.")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
    calculate_IMC(weight, height)

if __name__ == "__main__":
    main()
