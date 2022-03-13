import random
import threading

lower_std_subs = ["maths", "social", "science", "language", "english"]
lower_std_extra = ["art", "PT", "music"]
higher_std_subs = [
    "English",
    "Language",
    "Maths",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Civics",
    "Geography",
]
higher_std_extra = ["PT"]
main_lock = threading.Lock()


def generate(prev_gen=None, ishighschool=False):
    subs = higher_std_subs if ishighschool else lower_std_subs
    extra = higher_std_extra if ishighschool else lower_std_extra
    timetable = [["" for i in range(6)] for j in range(5)]
    for i in range(5):
        dup = [0] * 6
        for j in range(6):
            while True:
                sub = random.choice(subs + extra)
                if prev_gen and prev_gen[i][j] == sub:
                    break
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


if __name__ == "__main__":
    print(*generate(), sep="\n")