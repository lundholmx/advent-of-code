from lib import Input


def test_read_single_line():
    def toupper(s: str):
        return s.upper()

    items = (
        Input("tests/testdata/singleline.txt", linetype="single")
        .add_map(toupper)
        .read()
    )
    assert len(items) == 4
    assert items[0] == "ONE"


def test_read_single_item():
    item = Input("tests/testdata/singleitem.txt", linetype="single").read_single()
    assert item == "one-line-item"


def test_read_multiline():
    item = Input("tests/testdata/multiline.txt").read()
    assert len(item) == 5


def test_read_multiline_maps():
    def trim(s):
        return s.strip()

    item = Input("tests/testdata/multiline.txt").add_map(trim).add_map(int).read()
    assert len(item) == 5
    assert item[0] == 1
