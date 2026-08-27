#| Karakter | Açıklama                              | Örnek          |                  |
#| -------- | ------------------------------------- | -------------- | ---------------- |
#| `[]`     | Belirli karakterler                   | `[a-d]`        |                  |
#| `\`      | Özel karakterler                      | `\d`           |                  |
#| `.`      | Satırbaşı hariç herhangi bir karakter | `"he..o"`      |                  |
#| `^`      | ... ile başlayan                      | `"^hello"`     |                  |
#| `$`      | ... ile biten                         | `"planet$"`    |                  |
#| `*`      | Sıfır ve üzeri sayıda eşleşme         | `"he.*o"`      |                  |
#| `+`      | Bir ve üzeri sayıda eşleşme           | `"he.+o"`      |                  |
#| `?`      | Sıfır ya da bir eşleşme               | `"he.?o"`      |                  |
#| `{}`     | Karakter adeti                        | `"he.{2}o"`    |                  |
#| `        | `                                     | İkisinden biri | `"falls\|stays"` |

#| -------- | ------------------------------------------------- | ------------------------ |
#| `\A`     | Aranan kelime yazının başındaysa                  | `"\AThe"`                |
#| `\b`     | Başında veya sonundaysa (r harfi metin dışında!)  | `r"\bain"`<br>`r"ain\b"` |
#| `\B`     | Başında veya sonunda değilse                      | `r"\Bain"`<br>`r"ain\B"` |
#| `\d`     | Eğer sayı/sayılar içeriyorsa                      | `"\d"`                   |
#| `\D`     | Eğer sayı içermiyorsa                             | `"\D"`                   |
#| `\s`     | Eğer boşluk içeriyorsa                            | `"\s"`                   |
#| `\S`     | Eğer boşluk içermiyorsa                           | `"\S"`                   |
#| `\w`     | Eğer a-z, A-Z, sayı (0-9) ve alt çizgi içeriyorsa | `"\w"`                   |
#| `\W`     | `\w`'nin tam tersi                                | `"\W"`                   |
#| `\Z`     | Aranan kelime yazının sonundaysa                  | `"Spain\Z"`              |


import re

text = "BTK Akademi Python Dersleri"
pattern = "BTK"

match = re.search(pattern, text)

sonuc = match
sonuc = match.start()
sonuc = match.end()

match = re.findall (pattern, text)

sonuc = match

print(sonuc)
