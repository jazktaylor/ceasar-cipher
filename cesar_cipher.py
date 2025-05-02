import sys

def shift_letter(letter, shift):
    return chr(((ord(letter) - ord('A') + shift) % 26) + ord('A'))

def format_output(text):
    blocks = [text[i:i+5] for i in range(0, len(text), 5)]
    lines = [blocks[i:i+10] for i in range(0, len(blocks), 10)]
    return '\n'.join([' '.join(line) for line in lines])

def main():
    if len(sys.argv) < 2:
        print("Error: Missing shift amount. Usage: python3 ceasar_cipher.py <shift>")
        sys.exit(1)

    try:
        shift = int(sys.argv[1]) % 26
    except ValueError:
        print("Error: Shift must be an integer.")
        sys.exit(1)

    input_text = ""
    for line in sys.stdin:
        input_text += line.strip()

    input_text = input_text.upper()
    only_letters = ''.join([c for c in input_text if 'A' <= c <= 'Z'])

    encrypted = ''.join([shift_letter(c, shift) for c in only_letters])

    print(format_output(encrypted))

if __name__ == "__main__":
    main()
