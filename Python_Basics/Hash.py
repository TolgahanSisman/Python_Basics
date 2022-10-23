
ogrenciler = [{191216060: "Mehmet Ali AYDIN"}, {191216061: "Ayşe GÜNDÜZ"},
              {191216062: "Cem YILMAZ"}, {191216063: "Halime GERÇEK"}, {191216064: "Sevim COŞKUN"},
              {191216065: "Musa ÇİĞDEM"}, {191216066: "Selim DESTAN"},
              {191216067: "Canan TAKIM"}, {191216068: "Güldünya CAMBAZ"}, {191216069: "Mesut SALKIM"}]

hash_tablo = [None] * 17                                    # 17 GÖZLÜ HASH TABLOSU OLUŞTURDUK.


def hashing_func(key):                                      # LINEAR PROBING METODU FONKSİYONU.
    return key % len(hash_tablo)


def hash_insert(T, key, value):                                  # HASH_INSERT FONKSİYONU
    hash_key = hashing_func(key)
    T[hash_key] = value


print("\n=============== HASH TABLOSU  ===============\n")
hash_insert(hash_tablo, 191216060, 'Mehmet Ali AYDIN')
hash_insert(hash_tablo, 191216061, 'Ayşe Gündüz')
hash_insert(hash_tablo, 191216062, 'Cem Yılmaz')
hash_insert(hash_tablo, 191216063, 'Halime GERÇEK')
hash_insert(hash_tablo, 191216064, 'Sevim COŞKUN')
hash_insert(hash_tablo, 191216065, 'Musa ÇİĞDEM')
hash_insert(hash_tablo, 191216066, 'Selim DESTAN')
hash_insert(hash_tablo, 191216067, 'Canan TAKIM')
hash_insert(hash_tablo, 191216068, 'Güldünya CAMBAZ')
hash_insert(hash_tablo, 191216069, 'Mesut SALKIM')
print(hash_tablo)

print("\n==================================================")

def hash_search(T, key):                                # HASH SEARCH FONKSİYONU
    value = hashing_func(key)
    print("\nAranilan numara: ",T[value])

hash_search(hash_tablo, 191216063)
