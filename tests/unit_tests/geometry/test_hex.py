
from catan.geometry.hex import Hex, Direction


class TestHex:
    def test_s(self):
        assert Hex(1, 2).s == -3

    def test_neighbors(self):
        assert Hex(0, 0).neighbors == {
            Hex(1, -1),
            Hex(1, 0),
            Hex(0, 1),
            Hex(-1, 1),
            Hex(-1, 0),
            Hex(0, -1),
        }

    def test_add(self):
        assert Hex(1, 2) + Hex(3, 4) == Hex(4, 6)

    def test_sub(self):
        assert Hex(1, 2) - Hex(3, 4) == Hex(-2, -2)


class TestDirection:
    def test_north_east(self):
        assert Direction.NORTH_EAST == Hex(1, -1)

    def test_east(self):
        assert Direction.EAST == Hex(1, 0)

    def test_south_east(self):
        assert Direction.SOUTH_EAST == Hex(0, 1)

    def test_south_west(self):
        assert Direction.SOUTH_WEST == Hex(-1, 1)

    def test_west(self):
        assert Direction.WEST == Hex(-1, 0)

    def test_north_west(self):
        assert Direction.NORTH_WEST == Hex(0, -1)






