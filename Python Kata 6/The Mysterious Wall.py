def build_a_wall(x=0, y=0):

    if not isinstance(x, int) or not isinstance(y, int):

        return None

    elif x + y >= 1000:

        return "Naah, too much...here's my resignation."

    elif x <= 0 or y <= 0:

        return None

    else:

        wall = ""
        for row in range(0, x):
            if row % 2 == 0:
                wall += "■|■" * y
                wall += "\n"

            elif row % 2 == 1:
                wall += "■■|" * (y - 1)
                wall += "■■"
                wall += "\n"


        return str(wall[:-1])




print(build_a_wall(4,5))
