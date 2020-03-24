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
htmlwithtoc.toc

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
