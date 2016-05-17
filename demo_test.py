import pytest

import demo_src as src


class TestDemo:
    def test_check(self):
        x_wins = [["x", "x", "o"],
                  ["x", "o", "o"],
                  ["x", "o", ""]]

        o_wins = [["x", "o", "x"],
                  ["o", "o", "o"],
                  ["x", "x", "o"]]

        draw = [["x", "o", "x"],
                ["o", "x", "x"],
                ["o", "x", "o"]]

        assert src.check(x_wins) == "x"
        assert src.check(o_wins) == "o"
        assert src.check(draw) == "draw"

    def test_validate(self):
        good = [["x", "x", "o"],
                ["x", "o", "o"],
                ["x", "o", ""]]

        bad = [["x", "o", "y"],
               ["pig", 5, lambda x: x + 5],
               ["o", RuntimeError, "k"]]

        with pytest.raises(ValueError):
            assert src.validate(bad)

        assert src.validate(good) == good

    def test_row_status(self):
        pass

    def test_check_for_winner(self):
        pass

    def test_parse_aoa_to_array(self):
        pass
