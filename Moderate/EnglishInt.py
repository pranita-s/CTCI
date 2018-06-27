import re
def helper(s):
    smalls = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five',
              '6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','11':'Eleven',
              '12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen',
              '17':'Seventeen','18':'Eighteen','19':'Nineteen'}

    tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    result = ''
    for i in range(len(s)):
        place = len(s)-i
        if place == 3 and s[i] != '0':
            result = smalls[s[i]] +' ' + 'Hundred'+ ' '
        elif place == 2 and s[i] == '1':
            t = s[i:i+2]
            result += smalls[s[i:i+2]]
            break
        elif place == 2:
            result += tens[int(s[i])] + ' '
        elif place == 1 and s[i] != '0':
            result += smalls[s[i]] + ' '
    return result

def intToWords(num):

    str_num = str(num)
    comma_appended = ''
    while str_num:
        if len(str_num) <= 3:
            comma_appended = str_num[-3:] + comma_appended
            break
        comma_appended = ',' + str_num[-3:] + comma_appended
        str_num = str_num[:-3]

    lookup = {0:'',1:'Thousand',2:'Million',3:'Billion'}
    splitted = comma_appended.split(',')
    result = ''
    for i in range(len(splitted)):
        if splitted[i] == '000':
            continue
        words = helper(splitted[i])
        result += words +' '+ lookup[len(splitted)-i-1] + ' '
    
    result = re.sub(' +',' ',result)
    return result.strip()


print(intToWords(1000000))
