class MySequence(object):
    def __init__(self, a):
        self._seq = a[:]

    def __len__(self):
        return len(self._seq)

    def __contains__(self, a):
        return a in self._seq
        
        
def main():
    s = MySequence([2, 4, 5])
    print(f'1 in s? {1 in s}')
    print(f'2 in s? {2 in s}')
    print(f'len(s) = {len(s)}')

if __name__=='__main__':
    main() 