def input_int(prompt_message, error_message):
    int_number = 0
    while True:
        try:
            int_number = int(input(prompt_message))
        except ValueError:
            print(error_message)
            continue
        else:
            break
    return int_number
