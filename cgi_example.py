import cgi

form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<HTML>')
print('<title>Replay Page</title>')
print('<BODY>')
if not 'user' in form:
    print('<h1>Who are you</h1>')
else:
    print('<h1>Hello <i>%s</i></h1>' % cgi.escape(form['user'].value))
print('</BODY></HTML>')
