import random
import threading

subs = ["maths", "social", "science", "language", "english"]
extra = ["art", "PT", "music"]
main_lock = threading.Lock()


def generate():
    timetable = [["" for i in range(6)] for j in range(5)]
    for i in range(5):
        dup = [0] * 6
        for j in range(6):
            while True:
                sub = random.choice(subs + extra)
                if sub in subs:
                    sub_ind = subs.index(sub)
                    if not (any(ele >= 2 for ele in dup) and dup[sub_ind] >= 1):
                        timetable[i][j] = sub
                        dup[sub_ind] += 1
                        break

                else:
                    if not (
                        any(period in extra for period in timetable[i])
                        or any(sub in row for row in timetable)
                    ):
                        timetable[i][j] = sub
                        break
    return timetable


def stress_test():
    def check(t):
        for row in t:
            if len(set(row)) <= len(row) - 2:
                raise RuntimeError
        print("done")

    i = 0
    while True:
        if i % 100000 == 0:
            print(i)

        gen = generate()
        c = 0
        for row in gen:
            if any(ex in row for ex in extra):
                c += 1
        if c < 2:
            print("count:", c, "iteration:", i)
            print(*gen, sep="\n")
            print("-" * 20)
        if c == 0:
            print(i)
            break
        i += 1
