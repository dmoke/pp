"""
map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

"""


class Cipher:
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, string):
        return "".join([self.map2[i] if v in self.map2 else v for i, v in [(self.map1.find(v), v) for _, v in enumerate(string)]])

    def decode(self, string):
        return "".join([self.map1[i] if v in self.map1 else v for i, v in [(self.map2.find(v), v) for _, v in enumerate(string)]])


map1 = "abcdefghijklmnopqrstuvwxyz"
map2 = "tfozcivbsjhengarudlkpwqxmy"


def main():
    c = Cipher(map1, map2)
    print(c.encode("a_bc&*83"))

    print(c.decode("wyp"))


if __name__ == "__main__":
    main()
