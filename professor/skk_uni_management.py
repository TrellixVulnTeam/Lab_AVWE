import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

v = ['25', '24', '23', '21', '20', '19', '50']
va = ['경영정보', '국제경영/무역', '마케팅', '매니지먼트', '재무', '회계', '비즈']
for i in range(len(v)):
    url = 'https://biz.skku.edu/bizskk/intro/faculty.do?mode=list&srProfessorType='+ v[i] +'&srSearchKey=&srSearchVal='

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    ul = soup.select('#jwxe_main_content > div > div > div > div > div > div')
    for li in ul:
        name = li.select_one('dl > dd:nth-child(2) > ul > li:nth-child(2) > span').text
        tit = va[i]
        if li.select_one('dl > dd:nth-child(3) > ul > li.mail > a') is not None:
            email = li.select_one('dl > dd:nth-child(3) > ul > li.mail > a').text
        if li.select_one('dl > dd:nth-child(3) > ul > li.call') is not None:
            tel = li.select_one('dl > dd:nth-child(3) > ul > li.call').text.strip()
        print(name, tit, email, tel)
        sheet.append([name, tit, email, tel])
wb.save("professor.xlsx")


# sheet.append([name, tit, email, tel])
# wb.save("professor.xlsx")
