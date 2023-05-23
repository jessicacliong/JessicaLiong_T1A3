class DateCharacterError(Exception):
  """An error raised when a foreign character or symbol is entered in a date entry.
  """
  def __init__(self):
    super().__init__(
      "There is an invalid character in the entry. Please enter numbers only."
    )

class DateFormatError(Exception):
  """An error raised when date entry is not separated by a "-" symbol.
  """
  def __init__(self):
    super().__init__(
      "There is a foreign symbol(s) in the input. Please enter '-' as date separators"
    )

class YearLengthError(Exception):
  """An error raised when the length of characters in a date entry exceeds above the required length."""
  def __init__(self):
    super().__init__(
      "The length of year characters exceeds the required length. Please enter a date entry according to format YYYY-MM-DD."
    )
                     
class ShortYearError(Exception):
  """An error raised when the length of characters in a date entry falls below the required length.
  """
  def __init__(self):
    super().__init__(
      "The length of uear characters falls below the required length. Please enter a date entry according to format YYYY-MM-DD."
    )

class DateLengthError(Exception):
  """An error raised when the date format is not according to required length.
  """
  def __init__(self):
    super().__init__(
      "The format of the date characters falls below the required length. Please enter a date entry according to format YYYY-MM-DD."
    )

class ShortDateError(Exception):
  """An error raised when the date format falls short of the required length.
  """
  def __init__(self):
    super().__init__(
      "The length of date characters falls below the required length. Please enter a date entry according to format YYYY-MM-DD."
    )

class DateLengthError(Exception):
  """An error raised when the date format is not according to required length.
  """
  def __init__(self):
    super().__init__(
      "The format of the date characters falls below the required length. Please enter a date entry according to format YYYY-MM-DD."
    )

class ShortDateError(Exception):
  """An error raised when the date format falls short of the required length.
  """
  def __init__(self):
    super().__init__(
      "The length of date characters falls below the required length. Please enter a date entry according to format YYYY-MM-DD."
    )    

class NumberInputError(Exception):
  """An error raised when foreign symbol(s) and alphabet character(s) is detected in an integer input prompt.
  """
  def __init__(self):
    super().__init__(
      "You have entered an invalid character. Please enter a number from 1 to 10."
    )

class InvalidInputError(Exception):
  """An error raised when a foreign character or symbol is given as an entry for a Y or N entry.
  """
  def __init__(self):
    super().__init__(
      "You have entered an invalide character. Please type either 'Y' or 'N'."
    )