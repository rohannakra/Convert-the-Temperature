# https://leetcode.com/problems/convert-the-temperature/

def convert_temperature(celsius):
    return [celsius + 273.15, celsius * 1.8 + 32.0]

print(convert_temperature(36.5))
print(convert_temperature(122.11))

# --------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32.0]
