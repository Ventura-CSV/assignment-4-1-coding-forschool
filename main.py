def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if not (start.isalpha() and end.isalpha()):
            print("Error: Both inputs muist be single alphabetic characters.")
            continue
        
        start = start.lower()
        end = end.lower()
        
        if ord(start) > ord(end):
            print("Error: The starting value can't be smaller than ending value")
            continue
        for i in range(ord(start), ord(end)+1):
            result.append(chr(i))
        
        break
    

    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
