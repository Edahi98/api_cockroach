from argon2 import PasswordHasher

class HasherPWD:

    ph = PasswordHasher()

    @staticmethod
    def encode(pwd) -> str:
        return HasherPWD.ph.hash(pwd)

    @staticmethod
    def check(hash, pwd):
        print(f"CHECK JWT: HASH {hash}")
        print(f"CHECK JWT: PWD {pwd}")
        return HasherPWD.ph.verify(hash, pwd)