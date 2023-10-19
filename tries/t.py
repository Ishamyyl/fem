from types import SimpleNamespace


# class Node:
class Node(SimpleNamespace):
    _terminus = False


class Trie:
    def insert(self, s: str):
        if s:
            n = self
            for c in s:
                n = n.__dict__.setdefault(c, Node())
            n._terminus = True

    def __contains__(self, other: str):
        if not other:
            return False
        n = self
        for c in other:
            if not hasattr(n, c):
                return False
            n = getattr(n, c)
        return n._terminus

    def __iter__(self):
        cur = list(self.__dict__.items())
        word = []

        def walk():
            k, v = cur.pop()
            print(k, v)
            word.append(k)
            cur.extend(v.__dict__.items())
            if v._terminus:
                yield "".join(word)
                cur.pop()
            yield from walk()

        yield from walk()


if __name__ == "__main__":
    t = Trie()
    t.insert("")
    t.insert("asdf")
    t.insert("ask")
    t.insert("cat")
    t.insert("calf")
    t.insert("doggers")
    t.insert("dog")
    for w in t:
        print(w)
