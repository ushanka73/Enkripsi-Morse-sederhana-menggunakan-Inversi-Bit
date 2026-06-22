# ==========================================================
# SISTEM KOMUNIKASI MORSE + ASCII + BITWISE NOT + MESIN TURING
# ==========================================================

# Dictionary alfabet ke sandi Morse
MORSE_CODE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

# Dictionary kebalikan Morse ke alfabet
TEXT_CODE = {value: key for key, value in MORSE_CODE.items()}


# ==========================================================
# 1. KONVERSI TEKS KE MORSE
# ==========================================================

def text_to_morse(text):
    """
    Mengubah teks alfabet menjadi sandi Morse.
    Spasi antar kata ditandai dengan simbol '/'.
    """
    text = text.upper()
    morse_result = []

    for char in text:
        if char == " ":
            morse_result.append("/")
        elif char in MORSE_CODE:
            morse_result.append(MORSE_CODE[char])
        else:
            raise ValueError(f"Karakter '{char}' tidak tersedia dalam kode Morse.")

    return " ".join(morse_result)


# ==========================================================
# 2. KONVERSI MORSE KE ASCII BINER
# ==========================================================

def morse_to_ascii_binary(morse):
    """
    Mengubah string Morse menjadi biner ASCII 8-bit.

    Contoh:
    '.'  -> ASCII 46 -> 00101110
    '-'  -> ASCII 45 -> 00101101
    ' '  -> ASCII 32 -> 00100000
    '/'  -> ASCII 47 -> 00101111
    """
    binary_result = ""

    for char in morse:
        ascii_value = ord(char)
        binary_char = format(ascii_value, "08b")
        binary_result += binary_char

    return binary_result


# ==========================================================
# 3. ENKRIPSI BITWISE NOT
# ==========================================================

def bitwise_not(binary_data):
    """
    Membalik bit:
    1 menjadi 0
    0 menjadi 1
    """
    result = ""

    for bit in binary_data:
        if bit == "1":
            result += "0"
        elif bit == "0":
            result += "1"
        else:
            raise ValueError("Data biner hanya boleh berisi 0 dan 1.")

    return result


# ==========================================================
# 4. MESIN TURING UNTUK DEKRIPSI BIT INVERTER
# ==========================================================

class TuringMachineBitInverter:
    """
    Mesin Turing membaca pita berisi data terenkripsi.
    Mesin membalik setiap bit:
    0 -> 1
    1 -> 0

    Mesin berhenti ketika membaca simbol blank B.
    """

    def __init__(self, tape):
        self.tape = list(tape) + ["B"]
        self.head = 0
        self.state = "q0"

    def step(self):
        current_symbol = self.tape[self.head]

        if self.state == "q0":
            if current_symbol == "0":
                self.tape[self.head] = "1"
                self.head += 1

            elif current_symbol == "1":
                self.tape[self.head] = "0"
                self.head += 1

            elif current_symbol == "B":
                self.head += 1
                self.state = "q_accept"

    def run(self):
        while self.state != "q_accept":
            self.step()

        return "".join(self.tape).replace("B", "")


# ==========================================================
# 5. KONVERSI ASCII BINER KE MORSE
# ==========================================================

def ascii_binary_to_morse(binary_data):
    """
    Mengubah biner ASCII 8-bit kembali menjadi string Morse.
    """
    if len(binary_data) % 8 != 0:
        raise ValueError("Panjang data biner ASCII harus kelipatan 8.")

    morse_result = ""

    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        ascii_value = int(byte, 2)
        char = chr(ascii_value)
        morse_result += char

    return morse_result


# ==========================================================
# 6. KONVERSI MORSE KE TEKS
# ==========================================================

def morse_to_text(morse):
    """
    Mengubah sandi Morse kembali menjadi teks alfabet.
    """
    words = morse.split(" / ")
    text_words = []

    for word in words:
        letters = word.split()
        text = ""

        for letter in letters:
            if letter in TEXT_CODE:
                text += TEXT_CODE[letter]
            else:
                raise ValueError(f"Kode Morse '{letter}' tidak dikenali.")

        text_words.append(text)

    return " ".join(text_words)


# ==========================================================
# 7. PROGRAM UTAMA
# ==========================================================

def main():
    print("=" * 70)
    print("SISTEM KOMUNIKASI MORSE + ASCII + DEKRIPSI MESIN TURING")
    print("=" * 70)

    pesan = input("Masukkan pesan teks: ").strip()

    if pesan == "":
        print("Input tidak valid! Pesan tidak boleh kosong.")
        return

    print("\n=== PROSES PENGIRIM ===")

    morse = text_to_morse(pesan)
    print("1. Teks ke Morse:")
    print(morse)

    ascii_binary = morse_to_ascii_binary(morse)
    print("\n2. Morse ke ASCII Biner:")
    print(ascii_binary)

    encrypted_data = bitwise_not(ascii_binary)
    print("\n3. Enkripsi Bitwise NOT:")
    print(encrypted_data)

    print("\n=== DATA DIKIRIM KE PENERIMA ===")
    print(encrypted_data)

    print("\n=== PROSES PENERIMA ===")

    tm = TuringMachineBitInverter(encrypted_data)
    decrypted_binary = tm.run()
    print("4. Dekripsi menggunakan Mesin Turing:")
    print(decrypted_binary)

    restored_morse = ascii_binary_to_morse(decrypted_binary)
    print("\n5. ASCII Biner ke Morse:")
    print(restored_morse)

    restored_text = morse_to_text(restored_morse)
    print("\n6. Morse ke Teks:")
    print(restored_text)

    print("\n=== HASIL AKHIR ===")
    print(f"Pesan asli      : {pesan.upper()}")
    print(f"Pesan diterima  : {restored_text}")

if __name__ == "__main__":
    main()
