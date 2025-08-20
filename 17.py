ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def number_to_words(n):
    if n == 0:
        return ''
    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n - 10]
    if n < 100:
        return tens[n // 10] + number_to_words(n % 10)
    if n < 1000:
        quotient, remainder = divmod(n, 100)
        if remainder == 0:
            return ones[quotient] + 'hundred'
        else:
            return ones[quotient] + 'hundredand' + number_to_words(remainder)
    if n == 1000:
        return 'onethousand'

def euler_17(n):
    return sum(len(number_to_words(i)) for i in range(1, n + 1))

inputs = [342, 115]
for n in inputs:
    print(f"{n}: {len(number_to_words(n))}")

inputs = [5, 1000]
for n in inputs:
    print(f"{n}: {euler_17(n)}")
