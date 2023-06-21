from array import array

# https://codeforces.com/blog/entry/89629
def smallest_rotation(s):
    prev = None
    rep = 0
    ds = array("u", 2 * s)
    lens = len(s)
    lends = 2 * lens
    oldk = 0
    k = 0
    w = ""
    while k < lends:
        i = k
        j = k + 1
        while j < lends and ds[i] <= ds[j]:
            i = (ds[i] == ds[j]) and i + 1 or k
            j += 1
        while k < i + 1:
            k += j - i
            prev = w
            w = ds[oldk:k]
            oldk = k
            if w == prev:
                rep += 1
            else:
                prev = w
                rep = 1
            if len(w) * rep == lens:
                return "".join(w * rep)


def min_rotation(s):
    a = 0
    n = len(s)
    s=s+s
    b = 0
    while b < n:
        for i in range(n):
            print(".", end="")
            if a + i == b or s[a+i] < s[b+i]:
                if i > 1:
                    b += i - 1
                break
            if s[a+i] > s[b+i]:
                a = b
                break
        b += 1
    return a

smallest_rotation("acgaacgaaacgaaaacg")
print()
min_rotation("acgaacgaaacgaaaacg")
