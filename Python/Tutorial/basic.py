nama = "Rizki"  # print dasar
umur = 20
ipk = 3.17
text = "joni,pria,25"
data = text.split(",")
print(data, "\n")
# ============================================================================================================

print("joni" in text, "\n")  #search yang ada di text
# ============================================================================================================

print(nama[2], "\n")
print(nama[2:5], "\n")  # string yang di array 2 sampe 5, index 5 tidak di print
print(nama[-4:-1], "\n")  # baca string dari kanan, index 4 tidak di print
# ============================================================================================================

print("nama saya", nama, "dan umur saya", umur, "dan ipk saya ", ipk, "\n")
print(type(nama), "\n")  # cek tipe datanya
# ============================================================================================================

a = 2 + 6j + 9 + 8j  # j itu untuk tipe data complex
print(a, "\n")
# ============================================================================================================

paragraph = """Lorem ipsum dolor sit amet,   
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  # string yaang multi line

print(paragraph, "\n")
# ============================================================================================================

