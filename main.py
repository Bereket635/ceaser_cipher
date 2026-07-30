import string
from pathlib import Path
import os
import time

RED = '\u001B[31m'
GREEN = '\u001B[32m'
ORANGE = '\u001B[33m'
CYAN = '\u001B[36m'
WHITE = '\u001B[37m'

ALPHABET = string.ascii_lowercase
HISTORY_FILE = Path("cipher_history")

def ceaser_shift(text: str, shift: int) -> str:
    
    result = []
    for ch in text:
        if ch.isalpha():
            base = 'a' if ch.islower() else 'A'
            offset = ord(ch) - ord(base)
            new_offset = (offset + shift) % 26
            result.append(chr(ord(base) + new_offset))
            
        else:
             result.append(ch)
     
    return "".join(result)
     
def brute_force_ceaser(ciphertext: str) -> list[str]:
    
    output = []
    
    for shift in range(26):
        plaintext = ceaser_shift(ciphertext, -shift)
        output.append(f"Shift {shift:2d}: {plaintext}")
    return output
    
def save_to_history(ciphertext: str, results: list[str]):

    with HISTORY_FILE.open("a", encoding="utf-8") as f:
        f.write("=" * 60 + "")
        f.write(f"Ciphertext: {ciphertext}")
        for line in results:
            f.write(line + "")
        f.write("")
        
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def banner():
        print(f"{CYAN}♠=========={ORANGE}CAESAR CIPHER BRUTE-FORCER{CYAN}==========♠")
        
def show_history():
   clear_console()
   banner()
   
   if not HISTORY_FILE.exists():
        print(f"{RED}[!] No history found yet.")
        return

   content = HISTORY_FILE.read_text(encoding="utf-8")
   if not content.strip():
        print(f"{RED}[!] No history found yet.")
        return

   print(f"{CYAN}♠====================={ORANGE}CAESAR BRUTE-FORCE HISTORY{CYAN}====================♠")
   print(content)
    

def menu_brute_force():
  clear_console()
  banner()
  
  ciphertext = input(f"{RED}[{WHITE}?{RED}]{ORANGE}Enter ciphertext (word, sentence, anything):  {GREEN}").strip()
  if not ciphertext:
        print(f"{RED}[!] Ciphertext cannot be empty.")
        return

  print(f"{RED}[{WHITE}+{RED}]{GREEN} Brute forcing Ceaser cipher...")
  results = brute_force_ceaser(ciphertext)

  for line in results:
        print(line)

  save_to_history(ciphertext, results)
  print(f"{GREEN}Results saved to history.")
    
def main_menu():
  
    while True:
       banner()
       print(f"{RED}[{WHITE}1{RED}]{ORANGE} Brute force (word, sentence, all in one)")
       print(f"{RED}[{WHITE}2{RED}]{ORANGE} Scan history")
       print(f"{RED}[{WHITE}3{RED}]{ORANGE} Exit")
       print()
       choice = input(f"{RED}[{WHITE}?{RED}]{ORANGE} Enter your choice (1/2/3):  {GREEN}").strip()
       print()

       if choice == "1":
            menu_brute_force()
       elif choice == "2":
            show_history()
       elif choice == "3":
            print(f"{GREEN}Exiting. Goodbye!")
            break
       else:
            print(f"{RED}[!] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()