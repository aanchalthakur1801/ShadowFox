def format_example(num, specifier):
    try:
        formatted_string = format(num, specifier)
        print("Formatted string:", formatted_string)
    except ValueError:
        print(f"Error: '{specifier}' is not a valid format specifier for an integer.")

format_example(145, 'o')
