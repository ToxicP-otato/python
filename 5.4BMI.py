#Asking for height and weight, then calculate your BMI.
h=float(input('Please enter your height in meter:'))
w=float(input('Plese enter your weight in kg:'))

bmi=round(w/(h**2),1) #round to 1 decimal place.

if bmi<18.5:
    print('your BMI is ' , bmi , ', you are too light')
elif bmi<=25: #already filter lower weight.
    print('your BMI is ' + str(bmi) + ', you are normal.' )#use , , or + to combine string.
elif bmi<=28:
    print('your BMI is ' , bmi , ', you are overweight.')
elif bmi<=32:
    print('your BMI is ' , bmi , ', you are obese.')
else:
    print('your BMI is ' , bmi , ', you are severely obese.')