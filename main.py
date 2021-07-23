# AIM - convert the md files with YAML frontmatter to HTML and insert to my templates with toc

# INPUT - file path of the folder for all md files
# OUTPUT - HTML files converted from each md file

# set up the environment
import os
from frontmatter import Frontmatter
import markdown
from bs4 import BeautifulSoup
import re

# iterate all md files in the folder
# return the list of file path
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
            # elif os.path.exists(os.path.join(self.desfolder, htmlBaseName)):
            #     pass
            else:
                self.validFileList.append(fileName)
                self.desFileDict[fileName] = os.path.join(self.desfolder, htmlBaseName)

    def getFilePaths(self):
        return self.fileList

    def getValidFileNames(self):
        return self.validFileList

    def getDesFileDict(self):
        return self.desFileDict

# for each file, deal with the YAML frontmatter and body
# return a dictionary of YAML - title, modify time, head image
# return a string of body
class analyzeYAML():

    def __init__(self, filePath):
        self.MDFilePath = filePath
        self.MDINFOs = Frontmatter.read_file(self.MDFilePath)
        self.headINFODict = self.MDINFOs['attributes']
        self.bodyINFOStr = self.MDINFOs['body']

    def getTitleStr(self):
        return self.headINFODict['title']
    
    def getModifyDateStr(self):
        return self.headINFODict['modify date']

    def getTagsList(self):
        return self.headINFODict['tags']
    
    def getHeadIMGStr(self):
        return self.headINFODict['head image']

# get the soup ready for writing and inserting
# return soup
class analyzeSoup():

    def __init__(self, obj, analyzeMode='fp'):
        if analyzeMode == 'fp':
            self.obj = obj
            self.html = open(self.obj).read()
            self.soup = BeautifulSoup(self.html, "html.parser")
        if analyzeMode == 'html':
            self.obj = obj
            self.soup = BeautifulSoup(self.obj, "html.parser")

# add class to <h> tag to avoid header overlapping the anchor
    def modifyHTagAnchor(self):
        self.headList = self.soup.findAll(re.compile('^h\d'))
        for tag in self.headList:
            if tag.has_attr('class') and 'anchor' not in tag['class']:
                tag['class'].append('anchor')
            elif tag.has_attr('class') and 'anchor' in tag['class']:
                pass
            else:
                tag['class'] = 'anchor'
    
# pay attention to image filepath
    def modifyIMGPath(self):
        self.IMGList = self.soup.select('#post img')
        for IMGTag in self.IMGList:
            orisrc = IMGTag['src']
            pathList = orisrc.split('/')
            IMGTag['src'] = '/'.join(pathList[pathList.index('assets'):])

# delete table head content
# audit tables part in HTML with beautifulsoup
    def modifyTableHead(self):
        self.tableHeadList = self.soup.findAll("th")
        for tableHead in self.tableHeadList:
            tableHead.string = ''
    
# insert body html to post HTML <div id="content"> tag
# insert toc html to post HTML <div id="toc"> tag
    def insertDiv(self, modifiedSoup, id=''):
        targetDiv = self.soup.find(id=id)
        targetDiv.clear()
        if id == 'toc':
            targetDiv.insert(0, BeautifulSoup(modifiedSoup, 'html.parser'))
        else:
            targetDiv.insert(0, modifiedSoup)

# insert article title
    def insertTitleInArticle(self, titletxt):
        titletag = self.soup.new_tag('h1', style="color: #fd746c;")
        titletag.string = titletxt
        addingTag = self.soup.find(id='post')
        addingTag.insert(0, titletag)

# edit head picture
    def modifyHeadImg(self, headImgSrc):
        if headImgSrc == '':
            pass
        else:
            targetDiv = self.soup.find(id='offsetheader')
            targetDiv.img['src'] = headImgSrc

# insert the title to post HTML <title> tag with beautifulsoup
    def modifyTitle(self, newTitle):
        self.soup.title.string = newTitle

# ------ audit netease music <iframe> tag src attribute - add https: before exsisting src ------

# return templatepost.html
# TO DO
class convertMDPost():

    def __init__(self, mdstr):
        self.mdstr = mdstr

# convert md file's body into html
# pay attention to toc and tables and fenced_code ---and codehilite (no need)---
    def convertALL(self, extensions=['toc', 'tables','fenced_code']):
        MDMethod = markdown.Markdown(extensions=extensions)
        self.bodyHTML = MDMethod.convert(self.mdstr)
        self.bodyTOC = MDMethod.toc

# insert title and modify date info to articles.HTML
# replace the href in articles.HTML
# return articles(blog).html
# TO DO

### HERE WE GO! ###
if __name__ == '__main__':
    # set up the src and des folders
    orifp = '../saturn-drm.github.io/posts'
    desfp = '../saturn-drm.github.io/postshtml'
    templatefp = '../saturn-drm.github.io/layout/article.html'
    print('Step 1 completed: Set up the file paths.')

    # get the files need to be converted and the output file location respectively
    filePathInstance = filepaths(orifp, desfp)
    filePathInstance.getFiles()
    filePathInstance.validFiles()
    postsTOConvertList = filePathInstance.validFileList
    htmlDesDic = filePathInstance.desFileDict
    print('Step 2 completed: Fetch MD need converting LIST, and corresponding destination path DICTIONARY.')

    # soup the template html file
    templateHTMLInstance = analyzeSoup(templatefp, analyzeMode='fp')
    templateSOUP = templateHTMLInstance.soup
    print('Step 3 completed: Read template hmtl file with SOUP.')

    # work with single MD post
        # analyze YAML
    for mdFilePath in postsTOConvertList:
        print('Converting %s...' % os.path.basename(mdFilePath))
        desFilePath = htmlDesDic[mdFilePath]
        MDYAMLClass = analyzeYAML(mdFilePath)
        MDBodyStr = MDYAMLClass.bodyINFOStr
        htmlTitle = MDYAMLClass.getTitleStr()
        htmlDate = MDYAMLClass.getModifyDateStr()
        htmlTags = MDYAMLClass.getTagsList()
        htmlHeadImg = MDYAMLClass.getHeadIMGStr()
        print('%s YAML analysis completed' % os.path.basename(mdFilePath))

        # convert to hmtl
        MDToHTMLClass = convertMDPost(MDBodyStr)
        MDToHTMLClass.convertALL(extensions=['toc', 'tables','fenced_code'])
        bodyHTML = MDToHTMLClass.bodyHTML
        bodyTOC = MDToHTMLClass.bodyTOC
        print('Markdown file %s converted to HTML with TOC' % os.path.basename(mdFilePath))

        # Modify soup and html
        # soup the converted html txt
        convertingHTMLInstance = analyzeSoup(bodyHTML, analyzeMode='html')
        convertingSOUP = convertingHTMLInstance.soup
        # <h> add class anchor
        convertingHTMLInstance.modifyHTagAnchor()
        # tables
        convertingHTMLInstance.modifyTableHead()
        # IMG
        convertingHTMLInstance.modifyIMGPath()
        print('Modified %s SOUP.' % os.path.basename(mdFilePath))

        # insert content
        templateHTMLInstance.insertDiv(convertingSOUP, id='post')
        # insert toc
        templateHTMLInstance.insertDiv(bodyTOC, id='toc')
        # add article title
        templateHTMLInstance.insertTitleInArticle(htmlTitle)
        # head img
        templateHTMLInstance.modifyHeadImg(htmlHeadImg)
        # title
        templateHTMLInstance.modifyTitle(htmlTitle)
        print('Inserted %s into layout.html.' % os.path.basename(mdFilePath))

        # write to file
        htmlFile = open(desFilePath, 'w', encoding='utf-8', errors='xmlcharrefreplace')
        htmlFile.write(str(templateSOUP))
        htmlFile.close()
        print('%s convert finished.' % os.path.basename(mdFilePath))
    
    print('Mission completed.')