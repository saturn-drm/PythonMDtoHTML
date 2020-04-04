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
# TO DO
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

# add class to <h> tag to avoid header overlapping the anchor
    def modifyHTagAnchor(self):
        self.headList = self.soup.findAll(re.compile('^h'))
        for tag in self.headList:
            if tag.has_attr('class') and 'anchor' not in tag['class']:
                tag['class'].append('anchor')
            elif tag.has_attr('class') and 'anchor' in tag['class']:
                pass
            else:
                tag['class'] = 'anchor'

# ------ pay attention to image filepath ------
# delete table head content
# audit tables part in HTML with beautifulsoup

# audit netease music <iframe> tag src attribute - add https: before exsisting src

# insert body html to post HTML <div id="content"> tag
# insert toc html to post HTML <div id="toc"> tag
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