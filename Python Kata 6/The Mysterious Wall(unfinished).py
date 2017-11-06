def build_a_wall(x, y):

    if not isinstance(x, int) or isinstance(y, int):
        return "None"
    else:
        if x + y < 10000:

            r = ""
            for row in range(0, y):

                if row % 2 == 0:
                    r += "■|■" * x
                    r += "\n"
                else:
                    r += "■■|" * x
                    r += "\n"
            return r


        else:
            return "Naah, too much...here's my resignation."



print(build_a_wall(5, "dupa"))
