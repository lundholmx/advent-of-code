from lib import Input


def test_read_single_line():
    def toupper(s: str):
        return s.upper()

    items = Input("tests/testdata/singleline.txt", linetype="single").map(toupper).read()
    assert len(items) == 4
    assert items[0] == "ONE"


def test_read_single_item():
    item = Input("tests/testdata/singleitem.txt", linetype="single").read_single()
    assert item == "one-line-item"


def test_read_multiline():
    items = Input("tests/testdata/multiline.txt").read()
    assert len(items) == 5


def test_read_multiline_maps():
    def trim(s):
        return s.strip()

    items = Input("tests/testdata/multiline.txt").map(trim).map(int).read()
    assert len(items) == 5
    assert items[0] == 1


def test_filter():
    def greater(n):
        return n > 2

    items = Input("tests/testdata/multiline.txt").map(int).filter(greater).read()
    assert len(items) == 3
