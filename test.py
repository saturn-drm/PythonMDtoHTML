#%%
from frontmatter import Frontmatter

post = Frontmatter.read_file('../saturn-drmtest.github.io/posts/02tabs/2017-08-20-travel-is-meaningful.md')

# %%
post

# %%
post['body']

# %%
import markdown
htmlres = markdown.markdown(post['body'])
htmlres

# %%
post2 = Frontmatter.read_file('../saturn-drmtest.github.io/posts/01blog/01digest/2020-01-23-放言五首.md')
post2['body']

# %%
htmlres2 = markdown.markdown(post2['body'])
htmlres2

# %%
outputFile = open('testoutput.html','w',encoding='utf-8',errors='xmlcharrefreplace')
outputFile.write(htmlres2)

# %%
outputFile.close()

# %%
htmlwithtoc = markdown.markdown(post['body'], extensions=['toc'])
htmlwithtoc

# %%
outputFile2 = open('testoutput-toc.html','w',encoding='utf-8',errors='xmlcharrefreplace')
outputFile2.write(htmlwithtoc)
outputFile2.close()
outputFile3 = open('testoutput-notoc.html','w',encoding='utf-8',errors='xmlcharrefreplace')
outputFile3.write(htmlwithtoc)
outputFile3.close()

# %%
md = markdown.Markdown(extensions=['toc'])
htmlwithtoc2 = md.convert(post['body'])
htmlwithtoc2

# %%
md.toc

# %%
with open('testoutput-toc.html','r+',encoding='utf-8',errors='xmlcharrefreplace') as f:
    old = f.read()
    f.seek(0)
    f.write(md.toc)
    f.write(old)
    f.close()


# %%
post['frontmatter']

# %%
print(post['frontmatter'])

# %%
post['attributes']

# %%
post['attributes']['title']

# %%
from bs4 import BeautifulSoup
html = open('testoutput-toc.html').read()
soup = BeautifulSoup(html)
definetitle = soup.new_tag('title')
definetitle.string = post['attributes']['title']
definetitle

# %%
soup.title

# %%
soup.title.replace_with(definetitle)

# %%
soup.title

# %%
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension
# mdtable = markdown.Markdown(extensions=[TocExtension, TableExtension])
mdwithtable = Frontmatter.read_file('../saturn-drmtest.github.io/posts/00projects/2020-01-22-urban-intensification.md')
htmlwithtable = markdown.markdown(mdwithtable['body'], extensions=['toc', 'tables'])
htmlwithtable

# %%
outputfilewithtable = open('htmlwithtabke.html','w',encoding='utf-8',errors='xmlcharrefreplace')
outputfilewithtable.write(htmlwithtable)
outputfilewithtable.close()

# %%
