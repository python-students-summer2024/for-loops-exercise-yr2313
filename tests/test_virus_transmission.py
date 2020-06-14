
from virus_transmission import *

class Tests:

  def test_calculate_infections(self, capsys, monkeypatch):
    """
    Test that the method returns the correct values in a variety of cases.
    """
    assert calculate_infections(10, 1.2, 5) == 25
    assert calculate_infections(50, 1.1, 14) == 190
    assert calculate_infections(2, 1.5, 31) == 575253
    assert calculate_infections(2, 1.1, 62) == 737
    
