# PythonMDtoHTML

> Modify date: 2020-04-11

## Target

Convert the local markdown posts into html for my personal website.

Insert the html into layout file.

## Highlights

* Construct the html posts folder with same structure as that for markdown posts.
* Detect the YAML info of markdown posts and use the info in modified html posts. e.g.

```YAML
title: 其他摘录
modify date: 2020-01-29
tags: [Digest, Classical Chinese Literature]
head image: /assets/img/covers/codingcover.jpg
```

* Convert markdown posts with tables, code and toc into html codes.
* Add the class "anchor" to each \<h\> tag in html that appear in "toc", for the padding space format in html files.

```python
self.headList = self.soup.findAll(re.compile('^h\d'))
```

* Modify the table if table head is not need. (Basically in lots of markdown editors table without head cannot be rendered correctly.)
* Deal with the differences in relative file path of images between markdown and html codes. e.g.

> Path in Markdown

```markdown
![02-1L.jpg](../../assets/img/00architecture/03MAUD-EX02/02-1L.jpg)
```

> Path in HTML

```html
<p><img alt="02-1L.jpg" src="../../assets/img/00architecture/03MAUD-EX02/02-1L.jpg"/></p>
```

* Insert content, toc, title to layout template and modify the title and head image if needed.