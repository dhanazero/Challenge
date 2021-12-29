import re


def ElementHTML(a):
    tags_buka = ['<b>', '<i>', '<em>', '<div>', '<p>']
    tags_tutup = ['</b>', '</i>', '</em>', '</div>', '</p>']
    b = []
    c = re.split('(<[^>]*>)', a)
    for tags in c:
        if tags in tags_buka:
            b.append(tags)
        elif tags in tags_tutup:
            check = tags_tutup.index(tags)
            if (len(b) > 0) and (tags_buka[check] == b[len(b)-1]):
                b.pop()
    if b:
        return b[-1].replace('<', '').replace('>', '')
    return True


coba = '<div><div><b></b></div></p>'
print(ElementHTML(coba))
