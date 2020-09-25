from typing import overload

@overload
def account(name: str) -> tuple[str, float]:
    pass

@overload
def account(name: str, balance: float) -> tuple[str, float]:
    pass

def account(name, balance = 0):
    return (name, balance)

acct1 = account('Justin')
acct2 = account('Monica', 1000)

print(acct1)
print(acct2)