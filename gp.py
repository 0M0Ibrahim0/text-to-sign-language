# -*- coding: utf-8 -*-
from ISIR import ISRIStemmer
import re


class MorphologicalAnalysis:
    def __init__(self):
        self.stemmer = ISRIStemmer()
        self.prefix = None
        self.suffix = None
        self.stem = None
        self.root = None
        self.non_standerd_words = [u"طاقة",
                                   u"وطاقة",
                                   u"كهربائي",
                                   u"كهرباء",
                                   u"تلميذ",
                                   u"تلميذة",
                                   u"كيميائية",
                                   u"كيمياء",
                                   u"تكنولوجيا",
                                   u"تكنولوجية",
                                   u"كهربيا",
                                   u"مواد",
                                   u"مادة",
                                   u"كهربى",
                                   u"كهربية",
                                   u"التى",
                                   u"الات",
                                   u"الة",
                                   u"ماذا",
                                   u"ميكانيكية",
                                   u"ميكانيكي",
                                   u"ميكانيكا",
                                   u"حرارية",
                                   u"حراري",
                                   u"حراريا",
                                   u"نووية",
                                   u"نووي",
                                   u"نوويا",
                                   u"مياه",
                                   u"ارضى",
                                   u"ارضي",
                                   u"ارض",
                                   u"هكذا",
                                   u"عندما",
                                   u"اثناء",
                                   u"لديك",
                                   u"الصف",
                                   u"امتار",
                                   u"متر",
                                   u"كيلومتر",
                                   u"سنتيمتر",
                                   u"نيوتن",
                                   u"الحل",
                                   u"نموذجا",
                                   u"نموذج",
                                   u"مثلا",
                                   u"مكواة",
                                   u"بندولا",
                                   u"بندول",
                                   u"اليد",
                                   u"ارجوحة",
                                   u"ليمونة",
                                   u"نحاسي",
                                   u"نحاس",
                                   u"بطاطس",
                                   u"فولت",
                                   u"كاسيت",
                                   u"الله",
                                   u"ترمومتر",
                                   u"مئوى",
                                   u"مئة",
                                   u"بلاستيك",
                                   u"كرات",
                                   u"كرة",
                                   u"انبوبة",
                                   u"مرات",
                                   u"مرة",
                                   u"فرامل",
                                   u"ايام",
                                   u"بترولى",
                                   u"بترول",
                                   u"فترة",
                                   u"جدول",
                                   u"منضدة",
                                   u"فيشة",
                                   u"قابس",
                                   u"الخارصين",
                                   u"ليمون",
                                   u"بطارية",
                                   u"زجاج",
                                   u"تربة",
                                   u"صامولة",
                                   u"اطار",
                                   u"لوحة",
                                   ]

        self.numbers = {
            503: [u'0', u'\u0660', u'صفر', u'الصفر', u'صفرا'],
            504: [u'1', u'\u0661', u'اولا', u'واحد', u'أحد', u'أحدي', u'أحادي',u'اول',u'واحدة'],
            505: [u'2', u'\u0662', u'ثانيا', u'اثنين', u'اثنان', u'ثاني', u'ثنائي', u'اثنتان'],
            506: [u'3', u'\u0663', u'ثالثا', u'ثلاث', u'ثلاثة', u'ثلاثي',u'ثالث'],
            507: [u'4', u'\u0664', u'رباعي', u'رابع', u'رابعا', u'اربع', u'اربعة'],
            508: [u'5', u'\u0665', u'خمسة', u'خامس', u'خامسا', u'خمس', u'خماسي'],
            509: [u'6', u'\u0666', u'ست', u'سادسا', u'سادس', u'ستة'],
            510: [u'7', u'\u0667', u'سابعا', u'سبعة', u'سبع', u'سابع'],
            511: [u'8', u'\u0668', u'ثمانية', u'ثمان', u'ثماني', u'ثامن'],
            512: [u'9', u'\u0669', u'تسعة', u'تسع', u'تاسع', u'تاسعة']}

    def is_number(self, token):
        for key, value in self.numbers.items():
            if token in value:
                return key

    def get_stem(self, word):
        word=self.stemmer.norm(word,num=2)
        token=word
        token = self.remove_prefix(token)
        number=self.is_number(token)
        if word not in self.stemmer.stop_words and word not in self.non_standerd_words :
            word = self.stemmer.norm(word, num=1)
            if number!=None:
                self.stem=number
                return  self.stem
            word = self.remove_prefix(word)
            word = self.remove_suffix(word)
            word = self.stemmer.waw(word)
            word = self.stemmer.norm(word, num=2)
        self.stem = word
        return self.stem

    def remove_prefix(self, word):
        new_word = self.stemmer.pre32(word)
        prefix_len = len(word) - len(new_word)
        self.prefix = word[0:prefix_len]
        return new_word

    def remove_suffix(self, word):
        new_word = self.stemmer.suf32(word)
        self.suffix = word[len(new_word):]
        return new_word

    def norm_hmza(self, word):
        re_hamza = re.compile(r"[\u0623\u0624\u0626]")
        word = re_hamza.sub("\u0621", word)
        return word

    def get_root(self, word):
        token=word
        word = self.get_stem(word)
        if word in self.numbers.keys():
            self.root=word
            return self.root,'',''
        # if word was not stop word or non standerd
        if word not in self.stemmer.stop_words and word not in self.non_standerd_words:

            if len(word) == 4:  # length 4 word
                self.stemmer.pre = ''
                self.stemmer.suf = ''
                word,pre,suf = self.stemmer.pro_w4(word)
                self.prefix+=pre
                self.suffix=suf+self.suffix

            elif len(word) == 5:  # length 5 word
                self.stemmer.pre = ''
                self.stemmer.suf = ''
                word, pre, suf = self.stemmer.pro_w53(word)
                self.prefix += pre
                self.suffix = suf + self.suffix
                self.stemmer.pre = ''
                self.stemmer.suf = ''
                word, pre, suf = self.stemmer.end_w5(word)
                self.prefix += pre
                self.suffix = suf + self.suffix

            elif len(word) == 6:  # length 6 word
                self.stemmer.pre=''
                self.stemmer.suf=''
                word, pre, suf = self.stemmer.pro_w6(word)
                self.prefix += pre
                self.suffix = suf + self.suffix
                self.stemmer.pre = ''
                self.stemmer.suf = ''
                word, pre, suf = self.stemmer.end_w6(word)
                self.prefix += pre
                self.suffix = suf + self.suffix

            elif len(word) == 7:  # length 7 word
                self.stemmer.pre = ''
                self.stemmer.suf = ''
                actual_word=word
                word = self.stemmer.suf1(word)
                if len(word)<len(actual_word):
                    self.suffix=actual_word[-1]+self.suffix
                if len(word) == 7:
                    actual_word=word
                    word = self.stemmer.pre1(word)
                    if len(word)<len(actual_word):
                        self.prefix+=actual_word[0]

                if len(word) == 6:
                    self.stemmer.pre = ''
                    self.stemmer.suf = ''
                    word,pre,suf = self.stemmer.pro_w6(word)
                    self.prefix += pre
                    self.suffix = suf + self.suffix

                    self.stemmer.pre = ''
                    self.stemmer.suf = ''
                    word,pre,suf = self.stemmer.end_w6(word)
                    self.prefix += pre
                    self.suffix = suf + self.suffix

        #print(word)
        word = self.norm_hmza(word)
        self.root = word
        return word,self.prefix,self.suffix
