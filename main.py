import markdown

f = open('page.md', 'r')
md_content = f.read()
f.close()

f = open('template.html', 'r')
template = f.read().split('SPLIT')
f.close()

html_content = template[0] + markdown.markdown(md_content) + template[1]

f = open('index.html', 'w')
f.write(html_content)
f.close()

