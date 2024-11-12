import os
from time import sleep
def save_bmi_to_file(hasil: str):
    file_path = "bmi/database/data.txt"
    with open(file_path, "a", encoding='utf-8') as file:
        file.write(f"{hasil}\n")
def bmi_kurus(hasil_bmi) -> float:
    print("")
    hasil = f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori KURUS"
    print(hasil)
    save_bmi_to_file(hasil)
    sleep(5)
    os.system('cls')
def bmi_normal(hasil_bmi) -> float:
    print("")
    hasil = f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori NORMAL✨"
    print(hasil)
    save_bmi_to_file(hasil)
    sleep(5)
    os.system('cls')
def bmi_gemuk(hasil_bmi) -> float:
    print("")
    hasil = f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori GEMUK"
    print(hasil)
    save_bmi_to_file(hasil)
    sleep(5)
    os.system('cls')
def bmi_obesitas(hasil_bmi) -> float:
    print("")
    hasil = f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori OBESITAS"
    print(hasil)
    save_bmi_to_file(hasil)
    sleep(5)
    os.system('cls')