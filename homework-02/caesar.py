import typing as tp
import string


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    shift = shift % 26
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    table = str.maketrans(lower + upper, lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift])
    return plaintext.translate(table)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    return encrypt_caesar(ciphertext, -shift)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    max_matches = 0
    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)
        matches = sum(1 for word in decrypted.split() if word.lower() in dictionary)
        if matches > max_matches:
            max_matches = matches
            best_shift = shift
    return best_shift
    
