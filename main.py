import streamlit as st


st.title("8086 SIMULATOR")

#

OPTIONS = ["ax", "bx", "cx", "dx"]


register = {"ax": "0000",
            "bx": "0000",
            "cx": "0000",
            "dx": "0000"}

pointers = {"sp": "0000",
            "bp": "0000",
            "si": "0000",
            "dp": "0000"}


def output(title: str, values: dict) -> None:
    st.subheader(title)
    for item, col in zip(values.keys(), st.columns(4)):
        with col:
            values[item] = st.text_input(f"{str(item).upper()}: ", value=values[item])


output("Rejestry", register)

output("Rejestry wskaźnikowe", pointers)


with st.sidebar:
    mov_type = st.radio("TYPE: ", options=["mov", "xchg"])

    base_type = st.radio("TYPE: ", options=["bazowy", "indeksowy", "bazowo-indeksowy"])

    dst_register = st.selectbox("From", OPTIONS)
    src_register = st.selectbox("To", [register for register in OPTIONS if register != dst_register])
    if st.button("COMPILE"):
        if mov_type == "mov":
            register[dst_register] = register[src_register]
        if mov_type == "xchg":
            tmp = register[dst_register]
            register[dst_register] = register[src_register]
            register[src_register] = tmp
