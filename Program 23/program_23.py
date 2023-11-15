n = int(input('Enter no. of countries: '))
country_dict={}
cou_len=0
cap_len=0
curr_len=0
for i in range(n):
    country = input('Enter country: ')
    capital = input('Enter capital: ')
    currency = input('Enter currency: ')
    country_dict.update({country:(capital,currency)})
    if(len(country)>cou_len):
        cou_len=len(country)
    if(len(capital)>cap_len):
        cap_len=len(capital)
    if(len(currency)>curr_len):
        curr_len=len(currency)
for i in country_dict:
    capital=country_dict[i][0]
    currency = country_dict[i][1]
    print(i,' '*(cou_len-len(i)),' | ',capital,' '*(cap_len-len(capital)),' | ',currency,' '*(curr_len-len(currency)),sep='')