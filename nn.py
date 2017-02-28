import csv
# from numpy import exp, array, random, dot

values = []
countries = ["AED", "AUD", "BBD", "BGN", "BHD", "BWP", "CAD", "CHF", "CNH", "CNY", "CZK", "DKK", "EGP", "EUR", "FJD", "GBP", "GHS", "HKD", "HRK", "HUF", "ILS", "INR", "JMD", "JOD", "JPY", "KES", "KWD", "LKR", "LSL", "LTL", "MAD", "MUR", "MXN", "NOK", "NZD", "OMR", "PEN", "PGK", "PHP", "PLN", "QAR", "RON", "RSD", "RUB", "SAR", "SBD", "SEK", "SGD", "SZL", "THB", "TND", "TOP", "TRY", "UGX", "USD", "VUV", "WST", "XCD", "XPF", "ZAR", "ZMW"]

with open('netowrkdata.csv', 'rb') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        row[1] = countries.index(row[1])
        row[2] = countries.index(row[2])
        values.append(row)

for row in values:
    print row
