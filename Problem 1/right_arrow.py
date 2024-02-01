def right_arrow():
    base_char = input()
    head_char = input()

    row1 = '      ' + head_char
    row2 = str(6*base_char) + str(2*head_char)
    row3 = str(6*base_char) + str(3*head_char)

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()