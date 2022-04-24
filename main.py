import streamlit as st


st.title("8086 SIMULATOR")

#

OPTIONS = ["ax", "bx", "cx", "dx"]

base_address = int("0000", 16)

register = {"ax": "0000",
            "bx": "0000",
            "cx": "0000",
            "dx": "0000"}

pointers = {"sp": "0000",
            "bp": "0000",
            "si": "0000",
            "dp": "0000"}

ds_segment = {
    "ds": "0100",
    2000: "DA",
    2001: "75"
}


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
    offset = st.text_input("Offset")
    if st.button("COMPILE"):
        if mov_type == "mov":
            register[dst_register] = register[src_register]
        if mov_type == "xchg":
            tmp = register[dst_register]
            register[dst_register] = int(register[src_register], 16)
            register[src_register] = int(tmp, 16)
        if mov_type == "mov" and base_type == "bazowy":
            index = int(ds_segment["ds"]) * 10 + int(register[dst_register], 16)
            if index in ds_segment.keys():
                register[src_register] = f"{ds_segment[index]}{ds_segment[index+1]}"
            else:
                register[src_register] = 0000
st.text_input("output_ax", value=register["ax"], disabled=True)
st.text_input("output_bx", value=register["bx"], disabled=True)
st.text_input("output_cx", value=register["cx"], disabled=True)
st.text_input("output_dx", value=register["dx"], disabled=True)
