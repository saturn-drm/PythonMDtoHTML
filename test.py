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
soup = BeautifulSoup('<div id="content"></div>', "html.parser")
targetdiv = soup.find(id='content')
targetdiv.insert(0, tempcontent[1])
targetdiv

# %%
html = '''
<div id="offsetheader">
        <img src="/assets/img/covers/codingcover.jpg"/>
    </div>
    '''
headImgSrc = '/assests/img/covers/architecturecover.jpg'
soup = BeautifulSoup(html, "html.parser")
targetDiv = soup.find(id='offsetheader')
targetDiv.img['src'] = headImgSrc
targetDiv

# %%
import os
class filepaths():

    def __init__(self, orifp, desfolder):
        self.path = orifp
        self.fileList = []
        self.validFileList = []
        self.desFileDict = {}
        self.desfolder = desfolder

    def getFiles(self):
        for root, subFolders, files in os.walk(self.path):
            for fileName in files:
                self.fileList.append(os.path.join(root, fileName))

    def validFiles(self):
        for fileName in self.fileList:
            clearFileName = os.path.basename(fileName)
            subfolderFileName = '/'.join(fileName.split('/')[3:])
            htmlBaseName = os.path.splitext(subfolderFileName)[0] + '.html'
            if clearFileName == '.DS_Store':
                pass
            elif os.path.exists(os.path.join(self.desfolder, htmlBaseName)):
                pass
            else:
                self.validFileList.append(fileName)
                self.desFileDict[fileName] = os.path.join(self.desfolder, htmlBaseName)

    def getFilePaths(self):
        return self.fileList

    def getValidFileNames(self):
        return self.validFileList

filepathclass = filepaths('../saturn-drmtest.github.io/posts', '../saturn-drmtest.github.io/postshtml')
filepathclass.getFiles()
filepathclass.validFiles()
# filepathclass.validFileList
dic = filepathclass.desFileDict

# %%
clearFileName = os.path.basename('../saturn-drmtest.github.io/posts/01blog/01digest/2020-01-26-资治通鉴.md')
clearFileName

# %%
subfolderFileName = '/'.join('../saturn-drmtest.github.io/posts/01blog/01digest/2020-01-26-资治通鉴.md'.split('/')[3:])
subfolderFileName

# %%
htmlBaseName = os.path.splitext(clearFileName)[0] + '.html'
htmlBaseName

# %%
os.path.exists(os.path.join('../saturn-drmtest.github.io/postshtml', htmlBaseName))

# %%
print('Converting %s' % os.path.basename('../saturn-drmtest.github.io/posts/01blog/01digest/2020-01-26-资治通鉴.md'))

# %%
def insertDiv(modifiedSoup, id=''):
    targetDiv = soup.find(id=id)
    targetDiv.clear()
    targetDiv.insert(0, modifiedSoup)
htmltxt = '''
<h1 class="anchor" id="head1">head1</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                dolore
                magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
                mollit
                anim id est laborum.</p>
<h2 id="subhead1">subhead1</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                dolore
                magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
                mollit
                anim id est laborum.</p>
'''
htmlfp = '../saturn-drmtest.github.io/layout/article.html'
soup = BeautifulSoup(open(htmlfp).read(), "html.parser")
insertDiv(BeautifulSoup(htmltxt, 'html.parser'), id='content')
soup

# %%
