class NegativeError(Exception):
  """An error raised when a negative number is given as an input.
  """
  def __init__(self):
    super().__init__(
      "Please do not enter a negative number."
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
      "Date entry must not exceed the current date of the calendar year. Please re-enter a valid date."
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

class EmptyDataError(Exception):
  """An error raised when pandas dataframe returns empty."""
  def __init__(self):
      super().__init__(
        "DataFrame search returned empty. Please enter a search date that is available in our records."
      )

class DateExistsError(Exception):
  """An error raised when date entry is available in user_information.csv file"""
  def __init__(self):
    super().__init__(
      "Date already exists. Please enter a different date for the sleep log."
    )