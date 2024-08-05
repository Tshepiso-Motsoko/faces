def main():
    # Prompt the user for input
    in_put = input("Enter a string: ")

    # Call the convert function to replace :) and :(
    convert_in_put = convert(in_put)

    # Print the converted string
    print(convert_in_put)

def convert(input_str):
    # Replace :) with 🙂 and :( with 🙁
    convert_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return convert_str

main()