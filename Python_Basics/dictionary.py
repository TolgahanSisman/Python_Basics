# NOTLARIN TUTULDUĞU SOZLÜK #
ogrenci_notlari = {"191216018": [100, 200, 200, 100, 400, 400, 600],
                   "191216006": [10, 75, 200, 100, 300, 400, 600],
                   "191216015": [100, 100, 200, 100, 100, 300, 250],
                   "191216050": [80, 100, 75, 100, 0, 100, 200]}


# OGRENCİ NOTLARI SIRALAMA(GÖRME) #
def ogrenci_notlari_siralama():
    for i in ogrenci_notlari.items():
        print (i)
# ogrenci_notlari_siralama()


# OGRENCİ EKLEME FONKSİYONU #
def yeni_ogrenci_ekleme(yeni_ogrenci,notlari):
    ogrenci_notlari[yeni_ogrenci] = notlari
    print (ogrenci_notlari)
# yeni_ogrenci_ekleme("191216001", [90, 75, 170, 200, 190, 340, 475])


# OGRENCİ SİLME FONKSİYONU #
def ogrenci_silme(ogrenci_no):
    try:
        ogrenci_notlari.pop(ogrenci_no)
    except KeyError as err:
        print(err, "öğrencisi bulunamadı.")
    else:
        print(ogrenci_no,"numaralı öğrenci silindi!")
# ogrenci_silme("191216050")
# for item in ogrenci_notlari.items():
#     print(item)


# NOT GÜNCELLEME #
def not_guncelleme(okul_no,not_index,yeni_not):
    print(("Değiştirilmeden önceki not: "),ogrenci_notlari[okul_no][not_index])
    ogrenci_notlari[okul_no][not_index]=yeni_not;
    print(("Değiştirilen not: "),ogrenci_notlari[okul_no][not_index])
    print(("Güncel notlar: "),ogrenci_notlari[okul_no])
# not_guncelleme(("191216015"),2,20)


# SÖZLÜĞÜN KOPYASINI OLUŞTURMAK #
def not_sozlugu_kopyalama():
    ogrenci_notlari_2 = ogrenci_notlari.copy()
    print(ogrenci_notlari_2)
# not_sozlugu_kopyalama()


# OGRENCİ YÜZLÜK ORTALAMA HESAPLAMA FONKSİYONU #
def not_ortalama_hesabi(ogrenci):
    not_ort = 0
    for i in ogrenci:
        not_ort = not_ort + i
    son_note = (not_ort * 5 / 100)
    return (son_note)
# print(not_ortalama_hesabi(ogrenci_notlari["191216015"]))


# HARF NOTU HESAPLAMA #
def harf_notu_hesaplama(ogrenci):
    not_ort = 0
    for i in ogrenci:
        not_ort = not_ort + i
    son_note = (not_ort * 5 / 100)

    if 00 <= son_note <= 19:
        return("FF")
    elif 20 <= son_note <= 39:
        return("DD")
    elif 40 <= son_note <= 49:
        return("DC")
    elif 50 <= son_note <= 59:
        return("CC")
    elif 60 <= son_note <= 69:
        return("CB")
    elif 70 <= son_note <= 79:
        return("BB")
    elif 80 <= son_note <= 89:
        return("BA")
    elif 90 <= son_note <= 100:
        return("AA")
# print(harf_notu_hesaplama(ogrenci_notlari["191216018"]))


# 100LÜK SİSTEMDE HESAPLAYIP BAŞKA SÖZLÜĞE KAYDETME FONKSİYONU #
def yuzluk_sistem_sozlugu(ogrenci_no,ogrenci_notlari):
    not_ort = 0
    for i in ogrenci_notlari:
        not_ort = not_ort + i
    son_note = (not_ort * 5 / 100)
    yuzluk_sozluk={(ogrenci_no):son_note}
    return (yuzluk_sozluk)
# print(yuzluk_sistem_sozlugu(("191216018"),ogrenci_notlari["191216018"]))


# 100LÜK SİSTEM SÖZLÜĞÜNÜ HARF SİSTEMİNE ÇEVİRİP BAŞKA SÖZLÜĞE KAYDETME FONKSİYONU #
def yuzlukten_harfe_sozlugu(ogrenci_no,ogrenci_notlari):
    not_ort = 0
    for i in ogrenci_notlari:
        not_ort = not_ort + i
    son_note = (not_ort * 5 / 100)
    harf_note = son_note
    if 00 <= son_note <= 19:
        harf_note=("FF")
    elif 20 <= son_note <= 39:
        harf_note=("DD")
    elif 40 <= son_note <= 49:
        harf_note=("DC")
    elif 50 <= son_note <= 59:
        harf_note=("CC")
    elif 60 <= son_note <= 69:
        harf_note=("CB")
    elif 70 <= son_note <= 79:
        harf_note=("BB")
    elif 80 <= son_note <= 89:
        harf_note=("BA")
    elif 90 <= son_note <= 100:
        harf_note=("AA")
    harf_notu_sozlugu = {(ogrenci_no): harf_note}
    return (harf_notu_sozlugu)
# print(yuzlukten_harfe_sozlugu(("191216050"),ogrenci_notlari["191216050"]))