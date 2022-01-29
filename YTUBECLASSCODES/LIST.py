
lang = ['java','C','C++','Python','Javascript']
print(lang)
print(lang[0])
print(lang[3].upper())



lang[2]='C#'
print(lang)

lang.append('HTML')
print(lang)

lang.extend(['CSS','Angular'])
print(lang)

lang.append(['CSS','Angular'])
print(lang)

del lang[-1]
print(lang)

lang.insert(2,'C++')
print(lang)

print(lang[-1])

removed_lang=lang.pop()
print(removed_lang)
print(lang)

js=lang.pop(-4)
print(js)
print(lang)

lang.remove("HTML")
print(lang)

lang.sort()
print(lang)

lang.sort(reverse=True)
print(lang)


num=[30,2,1,6,7,88,55]
num.sort()
print(num)

print(num[:-1])

num.reverse()
print(num)

