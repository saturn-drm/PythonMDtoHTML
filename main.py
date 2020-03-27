# AIM - convert the md files with YAML frontmatter to HTML and insert to my templates with toc

# INPUT - file path of the folder for all md files
# OUTPUT - HTML files converted from each md file

# set up the environment
# TO DO
import os
from frontmatter import Frontmatter

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
        self.MDINFOs = {}
        self.headINFODict = {}
        self.bodyINFOStr = ''

    def decodeMD(self):
        self.MDINFOs = Frontmatter.read_file(self.MDFilePath)

    def setHeadINFO(self):
        self.headINFODict = self.MDINFOs['attributes']

    def setBodyINFO(self):
        self.bodyINFOStr = self.MDINFOs['body']

    def getHeadINFODict(self):
        return self.headINFODict

    def getBodyINFOStr(self):
        return self.bodyINFOStr

# insert the title to post HTML <title> tag with beautifulsoup
# return templatepost.html
# TO DO

# convert md file's body into html
# pay attention to toc and tables and fenced_code ---and codehilite (no need)---
# pay attention to image filepath
# delete table head content
# add class to <h> tag to avoid header overlapping the anchor
# audit tables part in HTML with beautifulsoup
# audit netease music <iframe> tag src attribute - add https: before exsisting src
# audit netease music <iframe> tag width attribute - 100%
# insert body html to post HTML <div id="content"> tag
# insert toc html to post HTML <div id="toc"> tag
# return templatepost.html
# TO DO

# insert title and modify date info to articles.HTML
# replace the href in articles.HTML
# return articles(blog).html
# TO DO