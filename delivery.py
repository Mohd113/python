if __name__ == '__main__':
    with open("delivery.txt", "r") as f:
        cases = int(next(f))
        for i in range(cases):
            lines = int(next(f))
            time = sum(int(next(f)) for _ in range(lines)) * 2
            print("{}. {}".format(i+1, time))

