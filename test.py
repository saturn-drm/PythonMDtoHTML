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
import os
fp = '../saturn-drmtest.github.io/posts'
for root, subfolders, files in os.walk(fp):
    print('subfolders')
    for subfolder in subfolders:
        print(os.path.join(root, subfolder))
    print('files')
    for filename in files:
        print(os.path.join(root, filename))

# %%
import os
class filepaths():

    def __init__(self, orifp):
        self.path = orifp
        self.fileList = []
        self.validFileList = []

    def getFiles(self):
        for root, subFolders, files in os.walk(self.path):
            for fileName in files:
                self.fileList.append(os.path.join(root, fileName))

    def validFiles(self):
        for fileName in self.fileList:
            clearFileName = os.path.basename(fileName)
            if clearFileName == '.DS_Store':
                pass
            else:
                self.validFileList.append(fileName)

    def getFilePaths(self):
        return self.fileList

    def getValidFileNames(self):
        return self.validFileList

fp = '../saturn-drmtest.github.io/posts'
inputfp = filepaths(fp)
inputfp.getFiles()
inputfp.validFiles()
inputfp.getValidFileNames()

# %%
class analyzeYAML():

    def __init__(self, fileName):
        self.MDFileName = fileName
        self.MDINFOs = {}
        self.headINFODict = {}
        self.bodyINFOStr = ''

    def decodeMD(self):
        self.MDINFOs = Frontmatter.read_file(self.MDFileName)

    def setHeadINFO(self):
        self.headINFODict = self.MDINFOs['attributes']

    def setBodyINFO(self):
        self.bodyINFOStr = self.MDINFOs['body']

    def getHeadINFODict(self):
        return self.headINFODict

    def getBodyINFOStr(self):
        return self.bodyINFOStr
    
fp = 'testtemplate.md'
decodeMD = analyzeYAML(fp)
decodeMD.decodeMD()
decodeMD.setHeadINFO()
decodeMD.setBodyINFO()
decodeMD.getBodyINFOStr()

# %%
