import streamlit as st

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
        elif char.isdigit():
            encrypted_text += str((int(char) + key) % 10)
        else:
            encrypted_text += char
    return encrypted_text

def encryption_app():
    st.title("Criptografia Simples")

    text = st.text_input("Digite a palavra ou número:")
    key = st.slider("Escolha a chave de criptografia:", min_value=1, max_value=25, value=3)

    if st.button("Criptografar"):
        encrypted_result = encrypt(text, key)
        st.success(f"Texto Criptografado: {encrypted_result}")

if __name__ == "__main__":
    encryption_app()
