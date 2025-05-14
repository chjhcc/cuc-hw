class HeightOutOfRangeError(Exception):
    pass

def weight_status(height, weight):
    try:
        if not 30 <= height <= 250:
            raise HeightOutOfRangeError('Height should be between 30 and 250 cm.')
        standard_weight = height - 100
        lower_bound = standard_weight * 0.95
        upper_bound = standard_weight * 1.05
        if lower_bound <= weight <= upper_bound:
            return '体重正常'
        elif weight > upper_bound:
            return '体重超标'
        else:
            return '体重不达标'
    except HeightOutOfRangeError as e:
        return str(e)
    except Exception as e:
        return 'Invalid input: ' + str(e)

# Example usage:
# You can replace these values with user input
user_height = 181
user_weight = 70

print(weight_status(user_height, user_weight))