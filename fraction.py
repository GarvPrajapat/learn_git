class Fraction:
    def __int__(self, num ,den):
        self.num = num
        if den == 0:
            raise ValueError("Can't set the value 0 of Denominator")
        self.den = den 

    def __str__(self):
        return f"{self.num}/{self.den}"