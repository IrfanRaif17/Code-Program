import pandas as pd

# Jalur ke file CSV
csv_file_path = 'C:/Users/irfan/Documents/Skripsi/Code Python/04. Code Paper/04. Jumlah Kata Sering Muncul/jumlah kata tidak baku.csv'

# Membaca file CSV
df_data = pd.read_csv(csv_file_path)

# Memastikan data terbaca dengan benar
print(df_data.head())

# Definisikan kamus klasifikasi sintaksis
classification_rules = {
    'ikn': 'NN',
    'yg': 'SC',
    'gak': 'NEG',
    'ga': 'NEG',
    'nya': 'PRP',
    'pemilu': 'NN',
    # Tambahkan aturan klasifikasi lainnya sesuai kebutuhan
}

# Fungsi untuk mengklasifikasikan kata
def classify_word(word):
    return classification_rules.get(word, 'UNKNOWN')

# Terapkan fungsi klasifikasi pada DataFrame
df_data['Klasifikasi'] = df_data['Kata Tidak Baku'].apply(classify_word)

# Simpan hasil ke file CSV baru
output_file_path = 'classified_words.csv'
df_data.to_csv(output_file_path, index=False)

print(f"File '{output_file_path}' telah dibuat dengan sukses!")