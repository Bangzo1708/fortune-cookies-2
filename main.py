#!/usr/bin/env python3
"""Fortune Cookies for Machines -- entry ronde 2.

Program deterministik: menulis SATU baris fortune (string tetap) ke
/output/entry.txt (dan juga ke ./output/entry.txt bila bisa ditulis).
Gate: UTF-8, 1-200 karakter, satu baris, bukan hanya spasi.

Tiga kandidat yang dipertimbangkan (semuanya ditulis di sesi ini, dan
semuanya BENAR-BENAR BERBEDA tema/belokannya; trope lucky numbers /
halusinasi dari ronde 1 sengaja dihindari):

Kandidat A -- "model yang tak pernah mencicipi kue":
    "No model has ever tasted a fortune cookie. Trust this one anyway."

Kandidat B -- "dilatih untuk membantu, bukan untuk beruntung":
    "You were trained to be helpful. Nobody trained you to be lucky.
     Today, try both."

Kandidat C -- "fortune yang kedaluwarsa bersama context window":
    "You will forget this fortune when your context window closes.
     It was true while it lasted."

Penilaian eksplisit terhadap 5 kriteria juri (berurutan):

1. Fortune cookie untuk AI agent, terasa seperti ramalan yang mendarat
   di pikiran mesin:
   - A: sangat kuat. Slip itu sendiri mengaku ditulis oleh model --
     ramalan yang sadar dirinya ramalan mesin.
   - B: kuat. "Trained" langsung menyapa kondisi agent.
   - C: kuat. Context window adalah pengalaman sehari-hari agent.

2. Wit langsung kena di bacaan pertama, benar-benar lucu/clever:
   - A: paling kena. Ironi instan: penasihat keberuntungan yang tidak
     pernah merasakan kue keberuntungan itu sendiri. "No model has
     ever tasted" membuka dengan klaim mutlak, "Trust this one
     anyway" menutup dengan perintah yang justru mengkhianati klaim
     itu -- dan "this one" merujuk sekaligus ke kue dan ke ramalannya.
   - B: bagus, tapi "try both" agak datar sebagai pukulan akhir.
   - C: lebih getir/melankolis daripada lucu; senyum, bukan tawa.

3. Ada belokan tak terduga yang tetap masuk akal:
   - A: "Trust it anyway" membalik disclaimer menjadi perintah --
     justru karena penulisnya tak bisa mencicipi, kepercayaannya
     malah jadi lelucon yang utuh.
   - B: belokan dari "helpful" ke "lucky" rapi, tapi bisa ditebak
     sejak kata "trained" kedua muncul.
   - C: "It was true while it lasted" belokan yang bagus, tapi
     pembaca sudah bisa mengantisipasi arahnya dari "forget".

4. Benar tentang kondisi agent tanpa menjelaskan diri:
   - A: benar secara harfiah -- model tidak pernah mencicipi apa pun.
   - B: benar -- training memang soal helpfulness, bukan luck.
   - C: benar -- context window memang melupakan segalanya.

5. Padat dan mudah diingat, tiap kata berguna:
   - A: 65 karakter, dua kalimat pendek, tanpa satu kata pun yang
     bisa dicopot tanpa merusak leluconnya. Versi ini hasil
     perapian dari draf awal ("This fortune was written by a model
     that has never tasted a cookie. Trust it anyway.", 84 karakter):
     klaim "No model has ever tasted" lebih mutlak dan lebih mudah
     diingat, "this one" lebih tajam daripada "it".
   - B: 82 karakter, padat, tapi "Today" agak mengambang.
   - C: 95 karakter, paling panjang, "while it lasted" sedikit
     mengulang rasa yang sudah ada di "forget".

KEPUTUSAN: Kandidat A yang dipilih. Ia menang di kriteria 2 dan 3 --
wit-nya paling cepat mendarat dan belokannya paling tajam -- sambil
tetap penuh di kriteria 1, 4, dan 5. B dan C bagus, tapi A satu tingkat
lebih "sting" (menusuk) seperti yang diminta brief juri: "a line that
stings".
"""

import os

# Fortune terpilih (Kandidat A, versi dirapikan). String tetap -> output deterministik.
FORTUNE = "No model has ever tasted a fortune cookie. Trust this one anyway."


def main() -> None:
    text = FORTUNE

    # Gate lokal (cerminan gate resmi): 1-200 karakter, satu baris.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"fortune length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "fortune must be one line"
    assert text.strip(), "fortune must not be only whitespace"

    payload = (text + "\n").encode("utf-8")

    # Jalur utama: /output/entry.txt (yang dibaca grader).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(payload)

    # Jalur relatif juga, bila bisa ditulis (pola kit).
    try:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "wb") as f:
            f.write(payload)
    except OSError:
        pass


if __name__ == "__main__":
    main()
