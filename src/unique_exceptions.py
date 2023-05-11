class DateInputCharacterError(Exception):
  def __init__(self, val):
    super().__init__("That is not a valid date format. Please enter numbers only.")

class DateFormatError(Exception):
  def __init__(self, val):
    super().__init__("That is not a valid date format. Please enter '/' as separator ")

class LengthError(Exception):
  def __init__(self, val):
    super().__init__("This is not a valid date length. Please enter according to format MM/DD/YYYY")
                     
# catches both # and a inputs
class InputError(Exception):
  def __init__(self,val):
    super().__init__("You have entered an invalid character. Please enter a number from 1 to 10.")

# for Y & N answers
class InvalidInputError(Exception):
  def __init__(self,val):
    super().__init__("Please enter Y or N.")

