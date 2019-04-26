import os, codecs
import markdown

def mdFile2Text(path):
    f = codecs.open(path, mode='r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def mdText2html(text):
    return markdown.markdown(text, extensions=['meta'], output_format='html5')

if __name__ == '__main__':
    text = mdFile2Text(os.path.abspath('./posts/test.md'))
    html = mdText2html(text)
    print(html)