def leetspeak_to_text(message: str) -> str:
    # Mapping of leetspeak characters to normal text
    replacements = {
        '@': 'a',
        '4': 'a',
        '8': 'b',
        '3': 'e',
        '1': 'l',
        '0': 'o',  
        '$': 's',
        '5': 's',
        '7': 't',
        '+': 't',
    }

    result = []

    for ch in message:
        # Replace if we have a mapping, otherwise keep the character
        if ch in replacements:
            result.append(replacements[ch])
        else:
            result.append(ch)

    return ''.join(result)


def main():
    # Assume only one input is taken
    leet_input = input("Enter leetspeak message: ")
    converted = leetspeak_to_text(leet_input)
    print("Converted message:", converted)


if __name__ == "__main__":
    main()