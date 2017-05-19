# HeatIndexCalculator.py
# Your job is to write a function in HeatIndexCalculator.py (call
# it **calculateHeatIndex()** that calculates the heat index
# factor based on the Heat Index Calculator from
# Calculator.net (http://www.calculator.net/heat-index-calculator.html)

# Define Function below
# be sure to return an integer
import math
def calculateHeatIndex(relHumidity, temp):
    heatIndex = -42.379 + (2.04901523*temp) + (10.141333127*relHumidity)-(.22475541*temp*relHumidity) - (.00683783*temp*temp)-(.05481717*relHumidity*relHumidity)+(.00122874*temp*temp*relHumidity)+ (.00085282*temp*relHumidity*relHumidity) - (.00000199*temp*temp*relHumidity*relHumidity)
    return round(heatIndex, 0)

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
