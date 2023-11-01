from virus_transmission import *


class Tests:
    def test_calculate_infections(self, capsys, monkeypatch):
        """
        Test that the method returns the correct values in a variety of cases.
        """
        expecteds = [25, 190, 575253, 737]

        actuals = [
            calculate_infections(10, 1.2, 5),
            calculate_infections(50, 1.1, 14),
            calculate_infections(2, 1.5, 31),
            calculate_infections(2, 1.1, 62),
        ]
        for actual, expected in zip(actuals, expecteds):
            assert (
                actual == expected
            ), f"Expected calculate_infections to return {expected} with test data; instead, it returned {actual}"
