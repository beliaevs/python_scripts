class Indexer(object):
    def __getitem__(self, idx):
        return 2 * idx


def main():
    a = Indexer()
    print(a[0], a[1], a[2])


if __name__=='__main__':
    main()