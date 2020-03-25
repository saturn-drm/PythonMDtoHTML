#%%
from frontmatter import Frontmatter
import markdown

fp = 'testtemplate.md'


# %%
head_body = Frontmatter.read_file(fp)
head_body['body']

# %%
bodyhtml = markdown.markdown(head_body['body'], extensions=['toc', 'tables','fenced_code'])
# bodyhtml = markdown.markdown(head_body['body'], extensions=['toc', 'tables','fenced_code', 'codehilite'])
bodyhtml

# %%
ofp = 'test.html'
of = open(ofp,'w',encoding='utf-8',errors='xmlcharrefreplace')
of.write(bodyhtml)
of.close()

# %%
md = markdown.Markdown(extensions=['toc', 'tables','fenced_code'])
# need fenced_code here too

# %%
bodytoc = md.convert(head_body['body'])
bodytoc

# %%
md.toc

# %%
with open('test.html','r+',encoding='utf-8',errors='xmlcharrefreplace') as f:
    old = f.read()
    f.seek(0)
    f.write(md.toc)
    f.write(old)
    f.close()

# %%
