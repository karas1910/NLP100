#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
import cgi


HTML_BODY = '''
<html>
<head>
<title>アーティスト検索</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<form method="GET" action="/cgi-bin/n69.py">
アーティスト名：<input type="text" name="name" value="{}" size="20"/><br />
別名：<input type="text" name="alias" value="{}" size="20"/><br />
タグ：<input type="text" name="tag" value="{}" size="20"/><br />
<input type="submit" value="検索"/>
</form>
{}
</body>
</html>
'''
HTML_RESULT = '''
<hr>
アーティスト名： {} (ID:{}) <br>
別名： {} <br>
タグ： {} <br>
活動エリア： {} <br>
レーティング： {} <br>
'''


def print_html(name, alias, tag, result):
    print(HTML_BODY.format(name, alias, tag, result))


if __name__ == '__main__':
    form = cgi.FieldStorage()
    client = pymongo.MongoClient()
    db = client.sample
    collection = db.artist
    result = ''
    search_dict = {}
    iname, ialias, itag = '', '', ''

    if form.getvalue('name') is not None:
        iname = form.getvalue('name')
        search_dict['name'] = iname
    if form.getvalue('alias') is not None:
        ialias = form.getvalue('alias')
        search_dict['aliases.name'] = ialias
    if form.getvalue('tag') is not None:
        itag = form.getvalue('tag')
        search_dict['tags.value'] = itag

    docl = collection.find(search_dict)
    docl = docl.sort('rating.count', pymongo.DESCENDING)

    for doc in docl:
        rid = doc.get('_id')
        rname = doc.get('name')
        if doc.get('aliases') is not None:
            ralias = doc.get('aliases')[0].get('name')
        else:
            ralias = '情報がありません'
        if doc.get('tags') is not None:
            tags = [t.get('value') for t in (tl for tl in doc.get('tags'))]
            tags = ', '.join(tags)
        else:
            tags = '情報がありません'

        if doc.get('rating') is not None:
            rating = doc.get('rating').get('count')
        else:
            rating = '情報がありません'
        if doc.get('area') is not None:
            area = doc.get('area')
        else:
            area = '情報がありません'
        result += HTML_RESULT.format(rname, rid, ralias, tags, area, rating)

    print_html(iname, ialias, itag, result)
