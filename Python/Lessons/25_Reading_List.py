dna = [ 'AUG', 'AUC', 'UCG' ]


dna.append("NEA")
dna.insert(1,"THOR")
dna.remove("AUC")
dna.pop(0)
#print(dna)



books = ['Zero to One',
'The Lean Startup',
'The Mom Test',
'Made to Stick',
'Life in Code', ]


#print(books)

books.append('Zero to Sold')
books.pop(0)
books.remove('The Lean Startup')

#print(books)

for i in books:
    print(i)