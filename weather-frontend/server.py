from bottle import redirect, template, request, response, route, run, get, post
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def main():
    run(host='0.0.0.0', port=8080)

BASE_TEMPLATE = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <style type="text/css">
                body {
                    font-family: sans-serif;
                }
        </style>
        </head>
        <body>
        {{!data}}
        <a href="/">&#8592; Main</a>
        </body>
        </html>
        """        

@route('/')
def get_index():
    data = """
    <h1>List of keys</h1><ul>{{!data}}</ul>
    <form action="/" method="post"><br>
    <b><label>Create new key</label>: </label></b><br>
    <input name="new_key" type="text" placeholder="key..."/><br>
    <input name="new_val" type="text" placeholder="value..."/><br>
    <button type="submit" id="submit" name="submit" value="Update">Create new key</button>
    </form>
    """
    the_template = template(BASE_TEMPLATE, data=data)

    inner_template = "<li><a href=\"{{key}}\">{{key}}</a></li>"

    keys = r.keys('*')

    data = ""
    for key in keys:
        data = data + template(inner_template, key=key)

    return template(the_template, data=data)

main()
