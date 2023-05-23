class DateInputCharacterError(Exception):
  """"""
  
  def __init__(self):
    super().__init__("That is not a valid date format. Please enter numbers only.")

class DateFormatError(Exception):
  def __init__(self):
    super().__init__("Please enter '-' as date separators")

class DateLengthError(Exception):
  def __init__(self):
    super().__init__("Please enter the date according to format MM/DD/YYYY.")
                     
# catches both symbols and alphabet character inputs
class NumberInputError(Exception):
  def __init__(self):
    super().__init__("You have entered an invalid character. Please enter a number from 1 to 10.")

# for Y & N answers
class InvalidInputError(Exception):
  def __init__(self):
    super().__init__("Please type either 'Y' or 'N'.")

