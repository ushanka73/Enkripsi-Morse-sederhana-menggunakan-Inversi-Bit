MORSE_TO_TEXT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

# ==========================================
# 2. FUNGSI-FUNGSI KONVERSI
# ==========================================
def morse_to_text(morse_str):
    huruf_morse = morse_str.split(" ")
    decoded_text = ""
    for huruf in huruf_morse:
        if huruf in MORSE_TO_TEXT:
            decoded_text += MORSE_TO_TEXT[huruf]
    return decoded_text

def text_to_ascii_binary(text):
    """Mengubah Teks menjadi array biner ASCII (8-bit per karakter)"""
    binary_tape = []
    for char in text:
        bin_str = format(ord(char), '08b')
        for bit in bin_str:
            binary_tape.append(int(bit))
    return binary_tape

def ascii_binary_to_text(binary_tape):
    """Membaca array biner ASCII dan menerjemahkannya kembali ke teks"""
    decoded_text = ""
    for i in range(0, len(binary_tape), 8):
        byte_array = binary_tape[i:i+8]
        byte_str = "".join(str(bit) for bit in byte_array)
        decoded_text += chr(int(byte_str, 2))
    return decoded_text

# ==========================================
# 3. FUNGSI MESIN TURING (INVERSI BIT)
# ==========================================
def turing_inverter(tape):
    """Mesin Turing membalik bit (1 ke 0, 0 ke 1)"""
    inverted_tape = []
    for bit in tape:
        inverted_tape.append(1 if bit == 0 else 0)
    return inverted_tape

# ==========================================
# PROGRAM UTAMA (SIMULASI ALUR GABUNGAN)
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("SIMULASI MESIN TURING: KRIPTOGRAFI MORSE -> ASCII")
    print("="*60)
    
    # 1. Input Morse
    input_morse = input("1. Masukkan Sandi Morse (pisahkan dgn spasi) : ")
    
    # 2. Morse -> Teks
    teks_awal = morse_to_text(input_morse)
    print(f"   [Diterjemahkan ke Teks] : {teks_awal}")
    
    # 3. Teks -> Biner ASCII
    biner_normal = text_to_ascii_binary(teks_awal)
    print("\n2. Konversi ke Biner ASCII (Normal) :")
    print("   ", biner_normal)
    
    # 4. Enkripsi (Inversi)
    biner_enkripsi = turing_inverter(biner_normal)
    print("\n3. Hasil Inversi (Biner Terenkripsi / Rahasia) :")
    print("   ", biner_enkripsi)
    
    # 5. Mesin Turing Bekerja (Dekripsi)
    print("\n   [Mesin Turing Penerima Sedang Mendekripsi...]")
    biner_dekripsi = turing_inverter(biner_enkripsi)
    
    # 6. Biner ASCII -> Teks
    hasil_teks = ascii_binary_to_text(biner_dekripsi)
    print("\n4. Hasil Terjemahan Akhir (Pesan Diterima) :")
    print("   ", hasil_teks)
    print("="*60)
