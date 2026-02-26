# input = "pong-ping-pong-ping-pong-dong-tang-bing-pong-pong-ping-pong-tink-donk-donk-donk"

# input = input.split("-")

# for prev, next in zip(input, input[1:]):
#     print(prev, next)

# from collections import Counter
# from itertools import groupby

# io = str.maketrans("oi", "io")
# print("piong".translate(io))

# print(Counter(input.split('-')))
# print(Counter(input.split('-')).most_common(2))

# turns = [[*v] for k,v in groupby(input.split("-"), lambda x: x in ("ping","pong")) if k]
# print(turns)

# ==================================== ^ping walrus:= v generator in join ====================================


# squares = [(sq := i * i) for i in range(4)]
# print(sq)

# w = 'abc darad aood'
# inside_out=lambda s:' '.join(
#     w[:(l:=len(w)//2)][::-1]
#     +w[l:-l]
#     +w[-l:][::-1]
#     for w in s.split(' '))


# print(inside_out(w))

# ==================================== lambda ====================================

# a = [1, 2, 3, 4, 5]

# sum_of_evens = [  l:= n for n in a if n%2 ==0]

# print(l)
# power = lambda s, p: [n**p for n in s]

# print(power(a, 2))

# foo = (lambda nums: (lambda doubles: ([double + 1 for double in doubles]))([num**2 for num in nums]))(a)
# foo2 = lambda nums: (lambda doubles: ([double + 1 for double in doubles]))([num**2 for num in nums])
# result = list(map(lambda n: n + 1, map(lambda n: n**2, a)))

# print(foo2(a))
# print(result)
# print(foo)