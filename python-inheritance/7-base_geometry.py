#!/usr/bin/python3
"""Hi"""


class BaseGeometry:
    """Hi"""

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is int:
            if value > 0:
                pass
            else:
                raise ValueError("value must be greater than 0")
        else:
            raise TypeError("value must be an integer")
