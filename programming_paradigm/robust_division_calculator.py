def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Only numeric values allowed.")