import streamlit as st

# STATIC 

REGISTERS = ["ax", "bx", "cx", "dx"]
POINTERS = ["sp", "bp", "si", "dp"]
INSTRUCTIONS = ["mov", "xchg"]
ADDRESSING_TYPE = ["z pamięci do rejestru", "z rejestru do pamięci"]


# FUNCTIONS

def output(title: str, values: dict) -> None:
    st.subheader(title)
    for item, col in zip(values.keys(), st.columns(4)):
        with col:
            values[item] = hex(int(st.text_input(f"{str(item).upper()}: ", value=int(values[item]))))
