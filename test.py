#%%
from frontmatter import Frontmatter

post = Frontmatter.read_file('../saturn-drmtest.github.io/2017-08-20-travel-is-meaningful.md')

# %%
post

# %%
post['body']

# %%
import markdown
htmlres = markdown.markdown(post['body'])
htmlres

# %%
