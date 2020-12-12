import pytest

"""
dynamic connectivity- Union Find

union(pt_a: int, pt_b: int) -> None
connected(pt_a: int, pt_b: int): -> bool
"""

# when connecting i1 to i2, all connected components of a index now matches b
class QuickFindUnionFind:
    """quick find (eager approach)"""

    def __init__(self, n: int):
        self.id = list(range(n))

    def connected(self, i1: int, i2: int) -> bool:
        return self.id[i1] == self.id[i2]

    def union(self, i1: int, i2: int) -> None:
        id_i1 = self.id[i1]
        id_i2 = self.id[i2]

        for i in range(len(self.id)):
            if self.id[i] == id_i1:
                self.id[i] = id_i2


class QuickUnionUnionFind:
    """quick union (lazy approach)
    list of lists where id[i] is the parent of i up to where
    the root being i is the same is id[i]

    find - check if i1 / i2 have same root
    union - merge components containing i1 / i2 and set id of
    i1 root to i2 root (i1 tree becomes child of i2 root)
    """

    def __init__(self, n: int):
        self.id = list(range(n))

    def connected(self, i1: int, i2: int) -> bool:
        return self.id[i1] == self.id[i2]

    def union(self, i1: int, i2: int) -> None:
        id_i1 = self.id[i1]
        id_i2 = self.id[i2]

        for i in range(len(self.id)):
            if self.id[i] == id_i1:
                self.id[i] = id_i2


def cases_uf(uf_class):
    instance = uf_class(n=10)
    instance.union(1, 2)
    instance.union(3, 4)
    instance.union(5, 6)
    instance.union(0, 5)
    instance.union(7, 8)
    instance.union(9, 7)
    instance.union(4, 8)
    """
    0 1 2 3 4 5 6 7 8 9
    6 2 2 8 8 6 6 8 8 8
    {0-5-6} {1-2} {3-4-7-8-9}
    """
    assert instance.connected(0, 6) is True
    assert instance.connected(0, 9) is False
    assert instance.connected(3, 7) is True
    assert instance.connected(3, 5) is False
    assert instance.connected(1, 4) is False


def test_cases_uf():
    cases_uf(QuickFindUnionFind)


# python -m pytest -rsa misc/union_find.py
# pytest.main()
