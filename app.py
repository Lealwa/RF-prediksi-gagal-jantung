import streamlit as st
import pandas as pd
import joblib

# Load model
loaded_model = joblib.load('random_forest_model.pkl')

def main():
    st.set_page_config(page_title="Prediksi Gagal Jantung", page_icon="❤️", layout="wide")
    
    # Title and description
    st.title("Prediksi Gagal Jantung Menggunakan Model Random Forest")
    st.markdown("""
        Aplikasi ini memprediksi kemungkinan terjadinya gagal jantung berdasarkan input data pasien.
        Harap isi data dengan benar dan klik 'Prediksi' untuk mendapatkan hasil.
    """)
    
    # Input data section
    st.header("Masukkan Data Pasien")
    
    # Input fields with better design and descriptions
    age = st.number_input("Umur (Tahun)", min_value=0, value=50, help="Masukkan umur pasien dalam tahun.")
    anemia = st.selectbox("Apakah pasien memiliki anemia?", options=["No", "Yes"], help="Pilih apakah pasien memiliki anemia.")
    anemia_numeric = 1 if anemia == "Yes" else 0
    
    cpk = st.number_input("Creatinine Phosphokinase (CPK)", min_value=0.0, value=100.0, help="Masukkan nilai CPK pasien.")
    
    diabetes = st.selectbox("Apakah pasien memiliki diabetes?", options=["No", "Yes"], help="Pilih apakah pasien memiliki diabetes.")
    diabetes_numeric = 1 if diabetes == "Yes" else 0
    
    ef = st.number_input("Ejection Fraction (EF)", min_value=0.0, value=60.0, help="Masukkan nilai EF pasien.")
    
    dt = st.selectbox("Apakah pasien memiliki Darah Tinggi?", options=["No", "Yes"], help="Pilih apakah pasien memiliki darah tinggi.")
    dt_numeric = 1 if dt == "Yes" else 0
    
    trombosit = st.number_input("Trombosit", min_value=0.0, value=200.0, help="Masukkan nilai trombosit pasien.")
    sc = st.number_input("Serum Creatinine", min_value=0.0, value=1.0, help="Masukkan nilai serum creatinine pasien.")
    sd = st.number_input("Serum Sodium", min_value=0.0, value=140.0, help="Masukkan nilai serum sodium pasien.")
    
    sex = st.selectbox("Jenis Kelamin", options=["Pria", "Wanita"], help="Pilih jenis kelamin pasien.")
    sex_numeric = 1 if sex == "Pria" else 0
    
    perokok = st.selectbox("Apakah pasien perokok aktif?", options=["Yes", "No"], help="Pilih apakah pasien perokok aktif.")
    perokok_numeric = 1 if perokok == "Yes" else 0
    
    time = st.number_input("Waktu Diagnosa (Hari)", min_value=0, value=0, help="Masukkan waktu sejak diagnosa dilakukan.")

    # Prediction button
    if st.button("Prediksi", use_container_width=True):
        # Prediction
        predictions = loaded_model.predict([[age, anemia_numeric, cpk, diabetes_numeric, ef, dt_numeric, trombosit, sc, sd, sex_numeric, perokok_numeric, time]])
        
        # Display the result
        if int(predictions) == 1:
            label = "Terkena Gagal Jantung"
            color = "red"
        else:
            label = "Tidak Gagal Jantung"
            color = "green"
        
        # Show result with enhanced styling
        st.markdown(f"<h3 style='color: {color}; text-align: center;'>Hasil Prediksi: {label}</h3>", unsafe_allow_html=True)
        
        # Additional result details (optional)
        st.markdown(f"**Detail Prediksi**: Pasien dengan usia {age} tahun, yang {['tidak', 'memiliki'][anemia_numeric]} anemia, {['tidak', 'memiliki'][diabetes_numeric]} diabetes, dan sebagainya.")
    
    # Footer (optional)
    st.markdown("""
        <br><br>
        <div style="text-align: center;">
            <p>Model ini menggunakan Random Forest untuk prediksi gagal jantung.</p>
            <p>© 2024 Prediksi Gagal Jantung</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
