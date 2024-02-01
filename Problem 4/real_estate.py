
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here

    first_line = "This house is $" + str(current_price) + '. ' + "The change is $" + str(current_price - last_month_price) \
     + " since last month."
    
    second_line = "The estimated monthly mortgage is $" +f'{(current_price * 0.051) / 12:.2f}' + "."

    print(first_line)
    print(second_line)
if __name__ == "__main__":
    real_estate()