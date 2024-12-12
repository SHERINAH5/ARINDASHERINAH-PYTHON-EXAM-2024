
# 1.(v)
student_info = {
    'name': 'Alice',
    'age' : 20,
    'grade' : 'A'
}
print(f' Student_info is {student_info}')
student_info['city'] = 'Kampala'
print(f' Student_info is {student_info}')


# 1(iii)
number_one = 10
number_two = 5
sum = int(number_one + number_two)
print(f"The sum of  number_one and number_two is")

difference = (number_one - number_two)
print(f"The difference of number_one and number_two is {difference}")

product = (number_one*number_two)
print(f'The product of number_one and number_two {product}')

quotient = int(number_one/number_two)
print(f"The quotient of number_one and number_two is {quotient}")


# 1(i)
import math
pie = math.pi
redius = int(input("Enter the radius of the circle"))
Area_of_a_circle = pie*redius**2
print( f'Area_of_a_circle with radius {redius} is {Area_of_a_circle}')

#Testing with a radius of 4
Area_of_a_circle = pie*4**2
print(f'Area_of_a_circle with radius 4 is {Area_of_a_circle}')



# 1(ii)
numbers = [4, 7, 2, 9, 12, 15]
def odd_numbers():
    odd_numbers = [7, 9, 15]
    for number in numbers:
        return odd_numbers
odd_numbers()
