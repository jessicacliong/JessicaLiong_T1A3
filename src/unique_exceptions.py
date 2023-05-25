class NegativeError(Exception):
  """An error raised when a negative number is given as an input.
  """
  def __init__(self):
    super().__init__(
      "Please do not enter a negative number."
    )

class DateFormatError(Exception):
  """An error raised when date entry is not separated by a "-" symbol.
  """
  def __init__(self):
    super().__init__(
      "There is a foreign symbol(s) in the input. Please enter '-' as date separators"
    )

class InvalidYearError(Exception):
  """An error raised when date entry exceeds current year range. 
  """
  def __init__(self):
    super().__init__(
      "An invalid entry has been made. Please enter a number within 2023 and the current year"
    )

class InvalidMonthError(Exception):
  """An error raised when date entry exceeds current month range. 
  """
  def __init__(self):
    super().__init__(
      "Month entry must not exceed the current month of year. Please enter a valid month."
    )

class InvalidDateError(Exception):
  """An error raised when date entry exceeds current month range. 
  """
  def __init__(self):
    super().__init__(
      "Date entry must not exceed the current date of the calendar year. Please enter a valid date."
    )

class RangeError(Exception):
  """An error raised when month range exceeds calendar format.
  """
  def __init__(self):
    super().__init__(
      "Entries must be within normal calendar format"
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
      "You have entered an invalid character. Please type either 'Y' or 'N'."
    )

class SleepTimeError(Exception):
  """An error raised when duration of sleep exceeds hours in a day."""
  def __init__(self):
    super().__init__(
      "Are you a rare species of a bear? Please enter a sensible number of hours slept."
    )

class UnavailableInputError(Exception):
  """An error raised when search date could not be found in the file"""
  def __init__(self):
    super().__init__(
      "This date entry doesn't exist in the system. Please enter another search date."
    )