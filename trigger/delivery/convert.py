import os, codecs, copy
import markdown

def getMdMeta(md):
    return md.Meta

def getMdContent(md, md_text):
    return md.convert(md_text)

def mergeMdObject(md_meta, md_content):
    md_obj = {}
    md_meta = copy.deepcopy(md_meta)
    for i in md_meta:
        if len(md_meta[i]) > 1:
            md_obj[i] = md_meta[i]
        else:
            md_obj[i] = md_meta[i][0]
    md_obj['content'] = md_content
    return md_obj

def mdFile2MdText(path):
    f = codecs.open(path, mode='r', encoding='utf-8')
    md_text = f.read()
    f.close()
    return md_text

def mdText2MdObject(md_text):
    md = markdown.Markdown(extensions=['meta'], output_format='html5')
    md_content = getMdContent(md, md_text)
    md_meta = getMdMeta(md)
    md_obj = mergeMdObject(md_meta, md_content)
    return md_obj

def convertMd(name):
    PREFIX_URL = './posts'
    md_text = mdFile2MdText(os.path.abspath('{}/{}.md'.format(PREFIX_URL, name)))
    obj = mdText2MdObject(md_text)
    return obj

if __name__ == '__main__':
    print(convertMd('test'))