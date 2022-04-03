#!/usr/bin/python
# -*- coding: utf-8 -*-
from gp import MorphologicalAnalysis
import  re
import pandas
from Animation import *
import os

'''
words=re.findall("[\u0600-\u06FF0-9\u0621-\u064A]+",input_paragraph)
for i in words:
    print(i)
'''

'''input_paragraph=u"في كل من البندول والارجوحة تتبادل طاقة الوضع وطاقة الحركة,دون أن ينتهيا بحيث: يصبح مجموعهما (عند) اي لحظة ثابت." \
                u"يتكون العمود الكهربي البسيط من محلول حمضي ينغمس فيه معندنان مختلفان,وتحدث به تفاعلات كميائية تؤدي الي تحويل الطاقة الكيميائية الي طاقة كهربية." \
                u"ذاكرت 3 دروس." \
                u"١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ ٠" \
                u" واحد..."
input_paragraph=u"1 2 3 4 5 6 7 8 9 0"'''
def getseq(input_paragraph):
    data_set=[]
    df = pandas.read_csv('LabelsCSV.csv', encoding='utf-8')
    data_set=list(df['words'])
    paragraphes=[]
    animation_sequance=[]
    paragraphes=re.split(':|:-|-:|\\.|\n',input_paragraph)
    for paragraph in paragraphes:
        sentances=paragraph.split(',')
        for sentance in sentances:
            words = re.findall(u"[\u0600-\u06FF0-9\u0621-\u064A]+", sentance)
            #words=sentance.split(' ')
            tst = MorphologicalAnalysis()
            for word in words:
                if len(word)>0:
                    w,pre,suf=tst.get_root(word)
                    if type(w) == type(6):
                        animation_sequance.append(w)
                    elif w in data_set:
                        if pre!=None and len(pre)>0 and pre in data_set:
                            #print('pre', ' :',data_set.index(pre)+1)
                            animation_sequance.append(data_set.index(pre) + 1)
                        animation_sequance.append(data_set.index(w) + 1)
                        #print('root ',':',data_set.index(w)+1)
                        if suf!=None and len(suf)>0 and suf in data_set:
                            #print('suf', ' :', data_set.index(suf)+1)
                            animation_sequance.append(data_set.index(suf) + 1)
                    else:
                        animation_sequance.append(0)
            animation_sequance.append(0)
    print(animation_sequance)
    GenerateAnimation(animation_sequance)

    os.system('cmd /c "cd C:/Users/ahmed/Desktop/ProblemSolving"')
    os.system('cmd /c "start Output.FBX"')
