import tracemalloc


def f(n):
    tracemalloc.start()
    s = 0
    for k in range(n):
        s += k

    
    print(f'f({n}): ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    tracemalloc.reset_peak()
    return s


def g(n):
    tracemalloc.start()
    s = 0
    for k in (p for p in range(n)):
        s += k

    print(f'g({n}): ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    tracemalloc.reset_peak()
    return s


def h(n):
    tracemalloc.start()
    s = 0
    for k in [p for p in range(n)]:
        s += k

    print(f'h({n}): ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    tracemalloc.reset_peak()
    return s

def main():
    N = 1000000
    f(N)
    g(N)
    h(N)


if __name__=='__main__':
    main()