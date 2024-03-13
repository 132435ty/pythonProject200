list = '''
<li>
    Hello
</li>
<li>
	I
</li>
<li>
	Am
</li>
<li>
	A
</li>
<li>
	Robot
</li>
<li>
	Привет
</li>
<li>
	Это
</li>
<li>
	статья
</li>
<li>
	пуста
</li>
<li>
	извини
</li>
<li>
	пожалуста
</li>
'''

cleanedlist = ' '.join(map(lambda x: x, list.split('</li>')))
cleanedlist1 = ' '.join(lambda x: x, cleanedlist.split('<li>')))
print(cleanedlist1)
