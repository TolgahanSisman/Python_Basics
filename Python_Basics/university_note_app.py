# ## ● 2 ödev, 2 kısa sınav, 1 proje,1 vize ve 1 final olmak üzere toplam 7 adet değerlendirme
# ## ● Kısa sınavların her biri 100 puan, ödevlerin her biri 200 puan,proje ve vize sınavı 400’er puan
# ve final sınavı 600 puan değerindedir.
# ## ● Değerlendirme 100 puan üzerinden olması gerektiğinden dönem sonunda her bir öğrencinin topladığı puanın %5’i
# ## alınarak puanlar 100’lük sisteme dönüştürülecektir.
# ## ● BEKLENEN :  öğrencileri ve notlarını bir sözlük (dictionary) yapısı kurarak saklamanız ve
# ## bu sözlükten verileri çekerek öğrencilerin harf notunu hesaplamanızdır.
# ## ● Öğrencilerin ve notlarının tutulduğu sözlüğe yeni bir öğrenci eklenebilir.
# ## ● Öğrencilerin ve notlarının tutulduğu sözlükten bir öğrenci silinebilir.
# ## ● Öğrencilerin notları güncellenebilir.
# ## ● Öğrencilerin ve notlarının tutulduğu sözlük kullanılarak her bir öğrencinin dönem sonu
# ## notu 100’lük sistem olarak hesaplanıp, başka bir sözlüğe kaydedilir.
# ## ● 100’lük sistemdeki notlarla oluşturulan sözlük kullanılarak öğrencilerin harf notları
# ## hesaplanıp yeni bir sözlükte saklanır.
# ● Yeni sözlükte herhangi bir öğrencinin bilgisi girilerek o öğrencinin harf notu ve tüm
# öğrencilerin harf notu görüntülenebilir.


# NOTLARIN TUTULDUĞU SOZLÜK #
ogrenci_notlari = {"Tolgahan": [100, 200, 200, 100, 400, 400, 600],
                   "Burak": [10, 75, 200, 100, 300, 400, 600],
                   "Oguzhan": [100, 100, 200, 100, 100, 300, 250],
                   "Ceyhun": [80, 100, 75, 100, 0, 100, 200]}
harf_notu_sozlugu = {}
yuzluk_not_sozlugu = {}


# OGRENCİ NOTLARI SIRALAMA(GÖRME) #
def ogrenci_notlari_siralama():
    for i in ogrenci_notlari.items():
        print (i)
# ogrenci_notlari_siralama()


# OGRENCİ EKLEME FONKSİYONU #
def yeni_ogrenci_ekleme(yeni_ogrenci,notlari):
    ogrenci_notlari[yeni_ogrenci] = notlari
    print (ogrenci_notlari)
# yeni_ogrenci_ekleme("Ahmet", [90, 75, 170, 200, 190, 340, 475])


# OGRENCİ SİLME FONKSİYONU #
def ogrenci_silme(ogrenci_adi):
    try:
        ogrenci_notlari.pop(ogrenci_adi)
    except KeyError as err:
        print(err, "öğrencisi bulunamadı.")
    else:
        print(ogrenci_adi,"adlı öğrenci silindi!")
# ogrenci_silme("Ceyhun")
# for item in ogrenci_notlari.items():
#     print(item)


# NOT GÜNCELLEME #
def not_guncelleme(isim,not_index,yeni_not):
    print(("Değiştirilmeden önceki not: "),ogrenci_notlari[isim][not_index])
    ogrenci_notlari[isim][not_index]=yeni_not;
    print(("Değiştirilen not: "),ogrenci_notlari[isim][not_index])
    print(("Güncel notlar: "),ogrenci_notlari[isim])
# not_guncelleme(("Oguzhan"),2,20)


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
# print(not_ortalama_hesabi(ogrenci_notlari["Tolgahan"]))


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
# print(harf_notu_hesaplama(ogrenci_notlari["Tolgahan"]))


# 100LÜK SİSTEMDE HESAPLAYIP BAŞKA SÖZLÜĞE KAYDETME FONKSİYONU #
def yuzluk_sistem_sozlugu(ogrenci_adi,ogrenci_notlari):
    not_ort = 0
    for i in ogrenci_notlari:
        not_ort = not_ort + i
    son_note = (not_ort * 5 / 100)
    yuzluk_sozluk={(ogrenci_adi):son_note}
    return (yuzluk_sozluk)
# print(yuzluk_sistem_sozlugu(("Tolgahan"),ogrenci_notlari["Tolgahan"]))


# 100LÜK SİSTEM SÖZLÜĞÜNÜ HARF SİSTEMİNE ÇEVİRİP BAŞKA SÖZLÜĞE KAYDETME FONKSİYONU #
def yuzlukten_harfe_sozlugu(ogrenci_adi,ogrenci_notlari):
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
    harf_notu_sozlugu = {(ogrenci_adi): harf_note}
    return (harf_notu_sozlugu)
# print(yuzlukten_harfe_sozlugu(("Oguzhan"),ogrenci_notlari["Oguzhan"]))


# HARF SÖZLÜĞÜNDE ÖĞRENCİNİN HARF NOTUNU GÖRME
def harf_notu_gorme(ogrenci):
    yuzlukten_harfe_sozlugu(ogrenci)