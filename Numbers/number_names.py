#!/usr/bin/env python

import sys


class Number:
    def __init__(self, num):
        self.num = num

    def name(self):
        thousands_arr = self.split_thousands()
        names_arr = []
        for num in thousands_arr:
            names_arr.append(self.nameXXX(num))
        for idx, name in enumerate(names_arr):
            if name != 'zero' and idx != 0:
                suffix = self.thousands(idx)
                names_arr[idx] = "%s %s" % (names_arr[idx], suffix)
        names_arr = [name for name in names_arr if name != 'zero']
        name = ' '.join(reversed(names_arr))
        return name

    def split_thousands(self):
        arr = []
        num = self.num
        while num > 0:
            arr.append(num % 1000)
            num = num / 1000
        return arr

    def nameXXX(self, num):
        name = ''
        if num >= 100:
            name += self.digit(num / 100) + ' hundred '
            num = num % 100
        if num >= 20:
            name += self.tens(num)
            if num % 10 != 0:
                name += '-'
            num = num % 10
        if num >= 1:
            name += self.digit(num)
        elif len(name) == 0:
            name = self.digit(0)
        return name

    def digit(self, num):
        digits = ['zero', 'one', 'two', 'three', 'four', 'five',
                  'six', 'seven', 'eight', 'nine', 'ten',
                  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                  'sixteen', 'seventeen', 'eighteen', 'nineteen']
        return digits[num]

    def tens(self, num):
        tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
                'sixty', 'seventy', 'eighty', 'ninety']
        return tens[num / 10]

    def thousands(self, num):
        thousands = ['zero', 'thousand', 'million', 'billion', 'trillion',
                     'quadrillion']
        return thousands[num]


num = Number(int(sys.argv[1]))
print num.name()

