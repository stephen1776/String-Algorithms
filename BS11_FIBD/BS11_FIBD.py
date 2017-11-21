'''
Mortal Fibonacci Rabbits.
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the nth month if all rabbits live for m months.
'''

def fibD(n,m):
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 2] + f[i - 1] - f[i - m - 1]

    return f[n] + f[n - 1]

def main():
    filename = '../data/rosalind_fibd.txt'
    with open(filename) as f:
        line = f.read().split()
        n = int(line[0])
        m = int(line[1])
        print(fibD(n,m))



if __name__ == '__main__':
    main()
