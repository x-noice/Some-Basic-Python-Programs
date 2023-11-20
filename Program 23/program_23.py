n = int(input('Enter no. of countries: '))
country_dict={}
cou_len=0
cap_len=0
curr_len=0
country_len = len('Country')
capital_len = len('Capital')
currency_len = len('Currency')
# Append data to dictionary
for i in range(n):
    country = input('Enter country: ')
    capital = input('Enter capital: ')
    currency = input('Enter currency: ')
    print('-'*16)
    country_dict.update({country:(capital,currency)})
    if(len(country)>cou_len):
        cou_len=len(country)
    if(len(capital)>cap_len):
        cap_len=len(capital)
    if(len(currency)>curr_len):
        curr_len=len(currency)
# Check for length
if(cou_len<country_len):
    cou_len = country_len
if(cap_len<capital_len):
    cap_len = capital_len
if(curr_len<currency_len):
    curr_len = currency_len
# Display header for table
print('Country',' '*(cou_len-country_len),' | ','Capital',' '*(cap_len-capital_len),' | ','Currency',' '*(curr_len-currency_len),sep='')
# Display table
for i in country_dict:
    capital=country_dict[i][0]
    currency = country_dict[i][1]
    print(i,' '*(cou_len-len(i)),' | ',capital,' '*(cap_len-len(capital)),' | ',currency,' '*(curr_len-len(currency)),sep='')
country = input('Enter country you would like to search for: ')
# Display searched country
if country in country_dict:
    country_1 = country_dict[country]
    print(country,country_1[0],country_1[1],sep=' | ')
else:
    print('Country record doesn\'t exist.')
