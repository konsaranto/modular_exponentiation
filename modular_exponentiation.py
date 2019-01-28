#!/usr/bin/python3

'''
Copyright © 2018-2019 Konstantinos Sarantopoulos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys

#parse the arguments
expo = sys.argv[1].split('mod')[0]
base = int(expo.split('^')[0])
exponent = int(expo.split('^')[1])
mod = int(sys.argv[1].split('mod')[1])

#variables
result_list = []
power_list = []

#function
def calculate(exponent):
    global base
    if exponent == 1:
        result = base % mod
        #print(str(base) + "^1mod" + str(mod) + "=" + str(result))
        two_power = 1
    for i in range(2, exponent + 1):
        #calculate the base^2mod which will be needed to calculate base^4mod (modular multiplication)
        if i == 2:
            result = (base ** i) % mod #** is power in python
            #print(str(base) + "^" + str(i) + "mod" + str(mod) + "=" + str(result))
            two_power = i
        #calculate only the powers of 2 (base^4mod base^8mod base^16mod) using the previous power of 2 (modular multiplication)
        elif i % (2 * two_power) == 0:
            result = (result * result) % mod
            #print(str(base) + "^" + str(i) + "mod" + str(mod) + "=" + str(result))
            two_power = i
    return result, two_power

#repeat until all powers of 2 have been calculated
while True:
    #reset max_power
    max_power = 0
    #make max_power equal to the max power of 2 calculated
    for i in power_list:
        max_power += int(i)
    #print("max_power=" + str(max_power))
    #substract max_power from exponent to calculate the remaining powers of 2
    exponent1 = exponent - max_power
    if exponent1 > 0:
        result, two_power = calculate(exponent1)
    #when exponent1=0 all powers have been calculated so exit
    else:
        break
    #append the result which corresponds to the power of 2 calculated to result_list
    result_list.append(result)
    #append two_power to power_list to know until which power of 2 is calculated
    power_list.append(two_power)
    #print("result_list=" + str(result_list))
    #print("power_list=" + str(power_list) + "\n")

result = result_list[0]
if len(result_list) == 1:
    result = result % mod
else:
    #multiply all results which are in powers of 2 using modular multiplication
    for i in range(0, len(result_list) - 1):
        result = (result * result_list[i+1]) % mod
print(str(base) + "^" + str(exponent) + "mod" + str(mod) + "=" + str(result))
