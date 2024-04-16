# Radius Utility

The `Radius` utility is a simple tool for calculating the area of a circle given its radius..

## Usage
To use the Radius utility, you need to have Python version 3 or higher installed.

1. Installation: First, install the utility by executing the following command:

pip install -e git+https://github.com/shokorev25/radius.git

2. Import: After successful installation, you can import the utility and use it in your code:

from radius import calculate_circle_area

3. Calculating Circle Area: Call the calculate_circle_area function with the radius of the circle to calculate its area:

radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print("The area of the circle with radius", radius, "is", area)
This code allows you to easily and quickly calculate the area of a circle given its radius, providing simplicity and convenience in usage.

### Testing
To ensure the correctness of the utility's functionality, a testing module is provided. You can run the tests using pytest: 

pytest

#### License
This project is licensed under the MIT License - see the LICENSE file for details.
