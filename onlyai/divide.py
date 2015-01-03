import csv

f = open('ai.txt','r',encoding='utf-8')

class Paper:

	authordict = {}
	authorset = set()
	authorcount = 0

	def __init__(self,title):
		self.title = title
		self.index = 0
		self.authors= []
		self.year = 0
		self.conf =""
		self.ref = []

	def add_index(self,index):
		self.index = index

	def add_authors(self,auths):
		for author in auths:
			if author in Paper.authorset:
				self.authors.append(Paper.authordict[author])
			else:
				Paper.authorcount+=1
				Paper.authordict[author] = Paper.authorcount
				Paper.authorset.add(author)
				self.authors.append(Paper.authordict[author])

	def add_year(self,year):
		self.year = year

	def add_conf(self,conf):
		self.conf = conf

	def add_ref(self,ref):
		self.ref.append(ref)

	def get_details(self):
		return [self.index,self.title,self.year,self.conf]
	def get_authors(self):
		auths = []
		for a in self.authors:
			auths.append([self.index,a,self.year])
		return auths
	def get_refs(self):
		refs = []
		for r in self.ref:
			refs.append([self.index,r,self.year])
		return refs

i = 0
papers = []
for row in f:
	row = row.strip('\r\n')
	if row.startswith('#*'):
		papers.append(Paper(row.strip('#*')))
	if row.startswith('#@'):
		papers[i].add_authors(row.strip('#@').split(','))
	if row.startswith('#t'):
		papers[i].add_year(row.strip('#t'))
	if row.startswith('#c'):
		papers[i].add_conf(row.strip('#c'))
	if row.startswith('#index'):
		papers[i].add_index(row.strip('#index'))
	if row.startswith('#%'):
		papers[i].add_ref(row.strip('#%'))
	if row.startswith('#!'):
		i+=1

csvwrite = csv.writer(open('author.csv','w',newline='',encoding='utf-8'))
auths = Paper.authordict
for author in auths:
	csvwrite.writerow([auths[author],author])

csvwrite = csv.writer(open('paper.csv','w',newline='',encoding='utf-8'))
for paper in papers:
	# print((paper.get_details))
	csvwrite.writerow(list(paper.get_details()))

csvwrite = csv.writer(open('paper_author.csv','w',newline='',encoding='utf-8'))	
for paper in papers:
	if paper.get_authors():
		csvwrite.writerows(list(paper.get_authors()))

csvwrite = csv.writer(open('paper_ref.csv','w',newline='',encoding='utf-8'))	
for paper in papers:
	if paper.get_refs():
		csvwrite.writerows(list(paper.get_refs()))