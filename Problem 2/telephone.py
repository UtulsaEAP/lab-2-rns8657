def telephone():
    phone_number = int(input())
    first_three_digits = phone_number // 10000000
    last_four_digits = phone_number % 10000
    middle_three_digits = ((phone_number // 100) % 100000) // 100

  
    print('(' + str(first_three_digits) + ') ' + str(middle_three_digits) + '-' + str(last_four_digits))

    
if __name__ == "__main__":
    telephone()