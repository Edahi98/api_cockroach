from argon2 import PasswordHasher

class HasherPWD:

    ph = PasswordHasher()

    @staticmethod
    def encode(pwd) -> str:
        return HasherPWD.ph.hash(pwd)

    @staticmethod
    def check(hash, pwd):
        return HasherPWD.ph.verify(hash, pwd)