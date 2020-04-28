from functools import reduce

def pf1(n, facts):
    i = 2
    while i <= n:
        if n % i == 0:
            facts.append(i)
            pf1(n // i, facts)
            break
        else:
            i += 1

def pf2(n):
    facts = []
    i = 2
    while i <= n:
        if n % i == 0:
            #print(i)
            facts.append(i)

            if n == i:
                break

            n = n // i
            i = 2
        else:
            i += 1

    return facts


def allfacts(n):
    d = 2
    f = []
    a = 0
    while d <= n:
        if(a > 0 and d > a):
            break

        if n % d == 0:
            f.append(d)
            if a == 0:
                a = n // d
        d = d + 1
    
    f.insert(0, 1)
    f.append(n)
    
    return f

def lcm(nums):
    nums = [(int(n), pf2(int(n))) for n in nums_str.split()]
    d = dict()
    for n in nums:
        for p in n[1]:
            if p in d:
                if n[1].count(p) > d[p]:
                    d[p] = n[1].count(p)
            else:
                d[p] = n[1].count(p)

    x = [i[0] ** i[1] for i in d.items()]
    ans = reduce(lambda p, c: p * c, x)

    return ans

def hcf(nums):
    s = set(allfacts(nums[0]))

    for i in range(1, len(nums)):
        a = allfacts(nums[i])
        s = s.intersection(a)

    return max(s)    

if __name__ == "__main__":
    nums_str = input('Input nubers separated by space: ')
    nums = [int(n) for n in nums_str.split()]
    print(f'LCM is {lcm(nums)}  HCF is {hcf(nums)}')
