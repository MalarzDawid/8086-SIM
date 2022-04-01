import streamlit as st


st.title("8086 SIMULATOR")

col1, col2, col3, col4 = st.columns(4)

OPTIONS = ["ax", "bx", "cx", "dx"]


register = {"ax": 0000,
            "bx": 0000,
            "cx": 0000,
            "dx": 0000}


with st.sidebar:
    register["ax"] = col1.text_input("AX: ")
    register["bx"] = col2.text_input("BX: ")
    register["cx"] = col3.text_input("CX: ")
    register["dx"] = col4.text_input("DX: ")

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
            
        col1.text_input(label="OUTPUT AX", disabled=True, placeholder=register["ax"])
        col2.text_input(label="OUTPUT BX", disabled=True, placeholder=register["bx"])
        col3.text_input(label="OUTPUT CX", disabled=True, placeholder=register["cx"])
        col4.text_input(label="OUTPUT DX", disabled=True, placeholder=register["dx"])
