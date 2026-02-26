def inside_out(strng: str) -> str:
    words = strng.split()
    result = []
    for word in words:
        if word.__len__() % 2 == 0:
            result.append(
                word[: word.__len__() // 2][::-1]
                + word[word.__len__() // 2 :][::-1]
            )
            continue
    
        result.append(
            word[: word.__len__() // 2][::-1]
            + word[word.__len__() // 2]
            + word[word.__len__() // 2 + 1 :][::-1]
        )

    return " ".join(result)


def main():
    print(inside_out("ubud"))


if __name__ == "__main__":
    main()


#inside_out=lambda s:' '.join(w[:(l:=len(w)//2)][::-1]+w[l:-l]+w[-l:][::-1]for w in s.split(' '))
