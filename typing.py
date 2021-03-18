from time import sleep, perf_counter


class txt:
    list_txt_f = ['سیاست‌های اصلاحی دولت در روستاها از طریق برنامه‌های اقتصادی و اجتماعی متنوعی به‌طور مستمر افزایش '
                  'یافت. ازجمله اجرای اصلاحات ارضی در سال 1341 بود که تغییراتی در ساختار مالکیت اراضی و به‌تبع آن '
                  'دگرگونی‌هایی در ساخت طبقات اجتماعی – اقتصادی روستایی ایجاد کرد. مقاله حاضر با رویکرد توصیفی – '
                  'تحلیلی درصدد پاسخ به این پرسش است که تحولات جمعیتی پس از اصلاحات ارضی در ایلام چه پیامدهای اجتماعی '
                  'و اقتصادی داشت؟ نتایج آن حاکی از این است، درحالی‌که هدف از اصلاحات ارضی ایجاد تعادل در مالکیت ارضی '
                  'و بهره مندی منطقی روستائیان از مالکیت بود، اما نتیجه متفاوت بوده و اکثر دهقانان به علت کمبود '
                  'اعتبار، سرمایه، نبود زمین مناسب، استقلال خود را از دست دادند و نه تنها نفوذ مالکین کاهش نیافت بلکه '
                  'شرایط اقتصادی آنان به‌تدریج ضعیف‌تر نیز شد. این وضعیت آرزوهای روستائیان را خواه درباره اصلاحات '
                  'ارضی و خواه دیگر سیاست‌های کشاورزی دولت تا حد زیادی نابود کرد. همین مسئله در استان ایلام نیز رخ '
                  'داد و باعث مهاجرت روستائیان به شهر، افزایش جمعیت و حاشیه‌نشینی در شهر ایلام گردید. حاشیه‌نشینی در '
                  'این شهر باعث گسترش آسیب‌های اجتماعی، تخریب زمین‌های کشاورزی ، توسعه فیزیکی شهر در زمین‌های نامناسب '
                  'و ایجاد محله های فقیر نشین شد.']
    list_txt_e = ['the policies of the government constantly increased in villages through various economic and '
                  'social plans. \nImplementation of land reformations was one of these plans in 1963 which lead to '
                  'some changes in the ownership framework of lands that, as a consequence, altered the framework of '
                  'the village’s socio-economic classes. \nDue to the fact that no separate research study has ever '
                  'dealt with of land reformations in Ilam, it seems essential to conduct a systematic research in '
                  'this regard. \nTherefore, the present research is an attempt to find an answer for this question '
                  'that “what socio-economic consequences, if any, these land reformations have had in Ilam? \n'
                  'following a descriptive – analytical approach. The results obtained reveal that while the main '
                  'goal of land reformations was to create a group of independent and autonomous peasants, '
                  'the results were completely reverse. \nNot only did most of the peasants lose their independence '
                  'due '
                  'to lack of the required credit, property, and sufficient and appropriate land, but on the '
                  'contrary, the influence of the owners was not decreased at all, and their economic situation has '
                  'even deteriorated in the forthcoming years. \nThis blackened all the bright wishes of the villagers '
                  'either with regard to the land reformation policies or the other agricultural policies of the '
                  'government to a large extent. \nA similar situation has also been experienced in Ilam and lead to '
                  'the emigration of the villagers to cities and expansion of marginalization in Ilam.']

    def farsi(self):
        return self.list_txt_f[0]

    def en(self):
        return self.list_txt_e[0]


a = txt()

try:
    asq = input('enter your language form fa and en')
    if asq == 'fa':
        b = a.farsi()  # persian text
        from show_farsi import show_farsi

        sh = show_farsi(b)
        sh.show()

    if asq == 'en':
        b = a.en()  # English text
        print(b)

    else:
        assert ValueError, 'your languages is not define'

except Exception as error:
    print(error, 'please try again')

start = perf_counter()
c = input('enter your txt for test :\n')
end = perf_counter()

T_L_A = []
number = 0


def Analyzer(x, number1=1000000000,qustion=False):  # for Analyzer the text in the pieces of text
    number2 = 0
    x = '{} '.format(x[::])
    global number
    counter = 0
    counter2 = []
    n = 0
    for i in x:
        counter += 1
        if i == ' ':
            counter2.append(counter)
            T_L_A.append(x[n:counter2[0] + n:])
            if qustion:
                number += 1
            number2 += 1
            counter = 0
            n = counter2[0] + n
            del counter2[0]
            if number1 == number2:
                return


Analyzer(c, qustion=True)
bb = T_L_A.copy()
T_L_A.clear()

Analyzer(b, number)
aa = T_L_A.copy()


cont = -1
counter10 = 0


def check(x, y):
    global counter10, start, end , cont
    d = 0
    for ii in x:
        for iii in ii:
            d += 1
    e = len(x)
    for i in x:
        cont += 1
        if i != y[cont]:
            counter10 += 1

        if cont == d:
            break

    print('your typing {} character in {} second and your mistake is {}  from {}'.format(d, (end - start), counter10 , e))


check(aa, bb)