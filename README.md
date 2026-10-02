# مصروفي | Masroofi

دفتر مصاريف شخصي بسيط يعمل من سطر الأوامر ودون إنترنت أو حزم خارجية. يمكنك تسجيل المصاريف، عرضها حسب الشهر، معرفة الإجمالي لكل تصنيف، وتصديرها إلى CSV لفتحه في برنامج جداول.

## المتطلبات

Python 3.9 أو أحدث.

## البداية السريعة

من داخل مجلد المشروع:

```bash
python3 expenses.py add 12.50 طعام --note "غداء"
python3 expenses.py add 8.00 مواصلات --date 2026-10-02
python3 expenses.py list
python3 expenses.py summary --month 2026-10
python3 expenses.py export expenses.csv --month 2026-10
python3 expenses.py remove 1
```

يُحفظ الملف افتراضيًا في `~/.morningstar/expenses.json`. لتجربة المشروع دون استخدام بياناتك المعتادة، ضع `--data` **قبل** اسم الأمر:

```bash
python3 expenses.py --data /tmp/my-expenses.json add 4.75 قهوة
python3 expenses.py --data /tmp/my-expenses.json summary
```

استخدم عملة واحدة في ملف البيانات نفسه، لأن التطبيق لا يحوّل العملات. المبالغ تقبل حتى منزلتين عشريتين. ملف CSV يُكتب بترميز يناسب النص العربي في برامج الجداول.

## الاختبارات

```bash
python3 -m unittest discover -s tests -v
```

المشروع تعليمي ومفتوح للتطوير. أفكار بسيطة للمساهمة: إضافة ميزانية شهرية، أو البحث في الملاحظات، أو واجهة رسومية صغيرة.
