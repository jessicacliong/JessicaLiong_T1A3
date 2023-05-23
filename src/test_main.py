import pytest
from main import user_input

def mock_input(monkeypatch, user_input):
  test_input = user_input
  monkeypatch.setattr("builtins.input",lambda _: next(test_input))

class TestUserInput:
  def user_input(self, monkeypatch):
    mock_input(monkeypatch,["##/##/####", ""])
    
class TestUserInput:
  def user_input(self, monkeypatch):
    mock_input(monkeypatch,[""])