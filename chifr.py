def chiffrer_avec_cle(text, key):
    encrypted_text = []
    for char in text:
        if char in key:
            encrypted_text.append(key[char])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)
