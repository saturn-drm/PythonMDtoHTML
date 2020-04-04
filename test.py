#%%
from frontmatter import Frontmatter
import markdown

fp = 'testtemplate.md'


# %%
head_body = Frontmatter.read_file(fp)
type(head_body['body'])

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
# bodytoc
bodyhtml == bodytoc

# %%
md.toc

# %%
with open('test.html','r+',encoding='utf-8',errors='xmlcharrefreplace') as f:
    old = f.read()
    f.seek(0)
    f.write(md.toc)
    f.write(old)
    f.close()

#%%
from bs4 import BeautifulSoup
htmlfp = '../saturn-drmtest.github.io/layout/articletest.html'
soup = BeautifulSoup(open(htmlfp).read(), "html.parser")
soup.title

# %%
type(soup.title.string)

# %%
soup.title.string = 'new title'
soup.title

# %%
import re
htmltesttest = '''
<h1 class="anchor" id="head1">head1</h1>
<h2 id="subhead1">subhead1</h2>
<h3 id="subsubhead1">subsubhead1</h3>
<h1 id="todo">todo</h1>
'''
htmltesttest2 = '<h2 id="subhead1">subhead1</h2>'

class analyzeSoup():

    def __init__(self, obj, analyzeMode='fp'):
        if analyzeMode == 'fp':
            self.obj = obj
            self.html = open(self.obj).read()
            self.soup = BeautifulSoup(self.html, "html.parser")
        if analyzeMode == 'html':
            self.obj = obj
            self.soup = BeautifulSoup(self.obj, "html.parser")

# insert the title to post HTML <title> tag with beautifulsoup
    def modifyTitle(self, newTitle):
        self.soup.title.string = newTitle

    def modifyHTagAnchor(self):
        self.headList = self.soup.findAll(re.compile('^h'))
        for tag in self.headList:
            if tag.has_attr('class') and 'anchor' not in tag['class']:
                tag['class'].append('anchor')
            elif tag.has_attr('class') and 'anchor' in tag['class']:
                pass
            else:
                tag['class'] = 'anchor'

souptestaddclass = analyzeSoup(htmltesttest, analyzeMode='html')
souptestaddclass2 = analyzeSoup(htmltesttest2, analyzeMode='html')
souptestaddclass.modifyHTagAnchor()
souptestaddclass.headList

# %%
