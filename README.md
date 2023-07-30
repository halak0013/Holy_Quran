# ﷽
## Kuran-I_Kerim_app
It is Holy Quran app

# some screenshots
<img src="data/img/logo.png" width="100">


<img src="data/img/test/main_v2.png" width="500">

.

<img src="data/img/test/db_surah.png" width="500">

.

<img src="data/img/test/db_ayats.png" width="500">

.

<img src="data/img/test/db_imams.png" width="500">

.

<img src="data/img/test/txt.png" width="500">


It uses [Presidency of the Republic of Türkiye
Presidency of Religious Affairs Noble Quran file](https://kuran.diyanet.gov.tr/Yayinlar)

# Running

`python3 main.py`

# Building

```console
sudo apt install devscripts git-buildpackage
sudo mk-build-deps -ir
gbp buildpackage --git-export-dir=/tmp/build/Holy_Quran -us -uc --git-ignore-branch --git-ignore-new


## InshAllah Now it has
- Sperate Noble Quran ayats and generate data base.**
- Playing ayats with a lot of Imams
- Choosing page or ayats
- Searching surah and ayat
- Surah view improvement

** you can generate same data base with jupiter nootbok and Kuran.txt but i take page numbers and secde ayats info another database

## InshAllah it will have
- Searching Keyword, word and senetence
- Meal
- Translation
