"""
Name: Ryan Smith

Lab Time: Thursday @2pm

"""
def caffeine():
    caffeine_mg = float(input())

    first_line =  "After 6 hours: " + f'{caffeine_mg / 2:.2f}' + ' mg'
    middle_line = 'After 12 hours: ' + f'{caffeine_mg / 4:.2f}'+ ' mg' 
    last_line = "After 24 hours: " + f'{caffeine_mg / 16:.2f}' + ' mg'

    print(first_line)
    print(middle_line)
    print(last_line)
    
if __name__ == "__main__":
    caffeine()