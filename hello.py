def hello(env, start_response):
    '''
    Simple WSGI app
    '''
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = b'\n'.join(env['QUERY_STRING'].split('&'))

    start_response(status, headers)

    return [body]
