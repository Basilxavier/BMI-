def calculate_bmi(weight, height):
  """Calculates the BMI.

  Args:
    weight: The weight in kilograms.
    height: The height in meters.

  Returns:
    The BMI.
  """

  bmi = weight/(height ** 2)
  return bmi


def interpret_bmi(bmi):
  """Interprets the BMI.

  Args:
    bmi: The BMI.

  Returns:
    A string describing the BMI category.
  """

  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Normal weight"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"


# Get the weight and height from the user.
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI.
bmi = calculate_bmi(weight, height)

# Interpret the BMI.
category = interpret_bmi(bmi)

# Print the results.
print("Your BMI is:", bmi)
print("You are:", category)
