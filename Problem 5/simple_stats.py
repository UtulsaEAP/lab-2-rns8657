
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''

    print(f'{num1 * num2* num3 * num4:.0f}' + ' ' +  f'{(num1+num2+num3+num4) / 4:.0f}')

    print(f'{num1 * num2* num3 * num4:.3f}' + ' ' +  f'{(num1+num2+num3+num4) / 4:.3f}')
if __name__ == "__main__":
    simple_stats()

    