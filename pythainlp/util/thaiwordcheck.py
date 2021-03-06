# -*- coding: utf-8 -*-
'''
From https://github.com/wannaphongcom/open-thai-nlp-document/blob/master/check_thai_word.md
'''
import re

def _check1(word): # เช็คตัวสะกดว่าตรงตามมาตราไหม
	if word in ['ก','ด','บ','น','ง','ม','ย','ว']:
		return True
	else:
		return False
def _check2(word): # เช็คตัวการันต์ ถ้ามี ไม่ใช่คำไทยแท้
	if '์' in word:
		return False
	else:
		return True
def _check3(word):
	if word in list("ฆณฌฎฏฐฑฒธศษฬ"): # ถ้ามี แสดงว่าไม่ใช่คำไทยแท้
		return False
	else:
		return True
def thaicheck(word):
	pattern = re.compile(r"[ก-ฬฮ]",re.U) # สำหรับตรวจสอบพยัญชนะ
	res = re.findall(pattern,word) # ดึงพยัญชนะทัั้งหมดออกมา
	if res==[]:
		return False
	elif _check1(res[len(res)-1]) or len(res)==1:
		if _check2(word):
			word2=list(word)
			i=0
			thai=True
			if word in ['ฆ่า','เฆี่ยน','ศึก','ศอก','เศิก','เศร้า','ธ','ณ','ฯพณฯ','ใหญ่','หญ้า','ควาย','ความ','กริ่งเกรง','ผลิ']: # ข้อยกเว้น คำเหล่านี้เป็นคำไทยแท้
				return True
			while i<len(word2) and thai==True:
				thai= _check3(word2[i])
				if thai==False:
					return False
				i+=1
			return True
		else:
			return False
	elif word in ['กะ','กระ','ปะ','ประ']:
		return True
	else:
		return False
