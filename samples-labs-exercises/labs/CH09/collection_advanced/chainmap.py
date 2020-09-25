from typing import Any, Dict, Hashable, Optional

class ChainMap:
    def __init__(self, *tulp: Dict) -> None:
        self.dictLt = list(tulp)

    def lookup(self, key: Hashable) -> Optional[Dict]:
        for m in self.dictLt:
            if key in m:
                return m
        return None

    def __getitem__(self, key: Hashable) -> Any:
        if m := self.lookup(key):
            return m[key]
        else:
            raise KeyError(key)

    def __setitem__(self, key: Hashable, value: Any):
        if m := self.lookup(key):
             m[key] = value
        else:
            self.dictLt.append({key: value})

    def __delitem__(self, key: Hashable):
        if m := self.lookup(key):
            del m[key]
            if len(m) == 0:
                self.dictLt.remove(m)
        else:
            raise KeyError(key)


c = ChainMap({'A' : 'Justin'}, {'A' : 'Monica', 'B' : 'Irene'})
print(c.dictLt)

print(c['A'])

c['A'] = 'caterpillar'
print(c.dictLt)

del c['A']
print(c.dictLt)