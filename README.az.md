# Turbo.az Scraper

Bu, Azərbaycanın ən populyar avtomobil alış-veriş saytlarından biri olan Turbo.az-dan avtomobil məlumatlarını çıxarmaq üçün hazırlanmış Python veb-sayt tarayıcısıdır.

## Xüsusiyyətlər

- Marka, model, il, qiymət və yer daxil olmaqla avtomobil təfərrüatlarını çıxarır.
- Məlumatlar CSV formatında saxlanılır.
- Veb-saytın HTML etiketlərində dəyişiklik ola biləcəyindən kod yenilənməsi tələb oluna bilər.
- Veb-skripinq üçün Selenium və Beautiful Soup kitabxanaları istifadə olunmuşdur.

## Quraşdırılma

1. Bu repozitorini klon edin.
2. Terminalınızda `pip install -r requirements.txt` əmrini işlədərək lazımi tələbatları yükleyin.

## Pypi Üzerində Quraşdırılma

turbo2csv-ni pip vasitəsilə quraşdıra bilərsiniz:

```bash
pip install turbo2csv
```

## İstifadə

```python
from turbo2csv import TurboScraper

scraper = TurboScraper()
scraper.scrape(output_file='turbo.csv')
```

## Sınaq

turbo2csv, qənaətbəxş və dəqiqliyi təmin etmək üçün ətraflı sınaq qapsamına malikdir. Sınaqları işlətmək üçün pytest-i istifadə edə bilərsiniz:

```bash
pip install pytest
pytest
```

## Feragat

Bu tətbiq etmə, təhsil məqsədləri üçün nəzərdə tutulmuşdur və ticari məqsədlər üçün istifadə edilməməlidir. Müəllif, bu alətin səhv istifadəsinin yaradabilecəyi hüquqi məsələlərdən məsuliyyəti daşımayacaq.

## Lisenziya

Bu layihə MIT Lisenziyası ilə lisenziyalanmışdır - ətraflı məlumat üçün LICENSE faylını baxın.