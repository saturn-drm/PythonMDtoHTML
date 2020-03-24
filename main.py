# AIM - convert the md files with YAML frontmatter to HTML and insert to my templates with toc

# INPUT - file path of the folder for all md files
# OUTPUT - HTML files converted from each md file

# set up the environment
# TO DO

# iterate all md files in the folder
# return the list of file path
# TO DO

# for each file, deal with the YAML frontmatter and body
# return a dictionary of YAML
# return a string of body
# TO DO

# insert the title to post HTML <title> tag with beautifulsoup
# return templatepost.html
# TO DO

# convert md file's body into html
# pay attention to toc and tables and fenced_code ---and codehilite (no need)---
# audit tables part in HTML with beautifulsoup
# audit netease music <iframe> tag src attribute - add https: before exsisting src
# insert body html to post HTML <div id="content"> tag
# insert toc html to post HTML <div id="toc"> tag
# return templatepost.html
# TO DO

# insert title and modify date info to articles.HTML
# replace the href in articles.HTML
# return articles(blog).html
# TO DO