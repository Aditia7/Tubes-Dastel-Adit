import streamlit as st
from streamlit_option_menu import option_menu
import math
from PIL import Image

with st.sidebar :
    st.image("download.png")
    selected = option_menu ("Program dibuat oleh Aditia Nugraha Nrp 11-2019-067 Mahasiswa ITENAS.\n      Tugas Dasar Telekomunikasi.\n             Dosen Pengampu : Ir. Rustamanji, M.T.\t  ",
    ["Perhitungan Rasio Daya",
    "Perhitungan Rasio Tegangan",
    "Perhitungan Rasio Arus",
    "Perhitungan Rasio Penguatan",
    "Perhitungan Rasio Redaman",],
    default_index=0)
    
        
if(selected == "Perhitungan Rasio Daya") :
    st.title("Rumus Rasio Daya")
    st.image("dayaa.jpeg")
    st.title("Perhitungan Rasio Daya")
    p1=st.number_input("Masukkan nilai pin/p1(watt) : ",0.000)
    p2=st.number_input("Masukkan nilai pout/p2(watt): ",0.000)
    hitung = st.button ("hitung Rasio Daya")
    if hitung : 
        y=(math.log10(p2/p1))*10
        st.write("nilai rasio daya adalah =",y,"dB")
        st.success(f"nilai rasio daya adalah = {y} dB")

if(selected == "Perhitungan Rasio Tegangan") :
    st.title("Rumus Rasio Tegangan")
    st.image("tega.jpeg")
    st.title("Perhitungan Rasio Tegangan")
    V1=st.number_input("Masukkan nilai Vin/V1(volt) : ",0.000)
    V2=st.number_input("Masukkan nilai Vout/v2(volt): ",0.000)
    hitung = st.button ("hitung Rasio Tegangan")
    if hitung : 
        x=(math.log10(V2/V1))*20
        st.write("nilai rasio tegangan adalah =",x,"dB")
        st.success(f"nilai tegangan adalah = {x} dB")

if(selected == "Perhitungan Rasio Arus") :
    st.title("Rumus Rasio Arus")
    st.image("arus.jpeg")
    st.title("Perhitungan Rasio Arus")
    i1=st.number_input("Masukkan nilai Iin/I1(ampere) : ",0.000)
    i2=st.number_input("Masukkan nilai Iout/I2(ampere): ",0.000)
    hitung = st.button ("hitung Rasio Arus")
    if hitung : 
        x=(math.log10(i2/i1))*20
        st.write("nilai rasio Arus adalah =",x,"dB")
        st.success(f"nilai Arus  adalah = {x} dB")

if(selected == "Perhitungan Rasio Penguatan") :
    st.title("Perhitungan Rasio Penguatan")
    st.title("Rumus Rasio Penguatan")
    st.image("a.jpeg")
    k=st.number_input("Masukkan nilai penguatan : ",0.000)
    hitung = st.button ("hitung Rasio Penguatan")
    if hitung : 
        x=(math.log10(k/1))*10
        st.write("nilai  penguatan adalah =",x,"dB")
        st.success(f"nilai penguatan adalah = {x} dB")

if(selected == "Perhitungan Rasio Redaman") :
    st.title("Perhitungan Rasio Redaman")
    st.title("Rumus Rasio Redaman")
    st.image("b.jpeg")
    k=st.number_input("Masukkan nilai Redaman : ",0.000)
    hitung = st.button ("hitung Rasio Redaman")
    if hitung : 
        x=(math.log10(1/k))*10
        st.write("nilai rasio Redaman atau loss adalah =",x,"dB")
        st.success(f"nilai rasio Redaman atau loss adalah = {x} dB")