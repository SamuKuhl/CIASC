import streamlit as st

def calculator():
    st.title("Calculadora")

    num1 = st.number_input("Digite o primeiro número:")
    operation = st.selectbox("Selecione a operação:", ["+", "-", "*", "/"])
    num2 = st.number_input("Digite o segundo número:")

    result = 0

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Erro: Divisão por zero!")

    st.write(f"Resultado: {result}")

if __name__ == "__main__":
    calculator()

