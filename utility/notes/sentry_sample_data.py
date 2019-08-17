emit_data = {'user': {'ip_address': '127.0.0.1', 'id': 1, 'email': '', 'username': 'nimish'}, 'request': {'method': 'GET', 'url': 'http://127.0.0.1:8000/projects/1/sample/', 'query_string': '', 'data': None, 'cookies': {'djdt': 'hide', 'csrftoken': 'BrhAIWFHL8htsLS5eFtfJUOs08qFEpiisYNJIhrqYWB8ACaBOfRH563XwNGOfWpG', 'sessionid': 'ar8qsiz69b96byzsrrzzfdnbswmgrlmq'}, 'headers': {'Content-Length': '', 'Content-Type': 'text/plain', 'Host': '127.0.0.1:8000', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cookie': 'djdt=hide; csrftoken=BrhAIWFHL8htsLS5eFtfJUOs08qFEpiisYNJIhrqYWB8ACaBOfRH563XwNGOfWpG; sessionid=ar8qsiz69b96byzsrrzzfdnbswmgrlmq'}, 'env': {'REMOTE_ADDR': '127.0.0.1', 'SERVER_NAME': 'localhost', 'SERVER_PORT': '8000'}}, 'tags': {}, 'extra': {'sys.argv': ["'manage.py'", "'runserver'"]}, 'level': 40, 'exception': {'values': [{'value': 'division by zero', 'type': 'ZeroDivisionError', 'module': 'builtins', 'stacktrace': {'frames': [{'abs_path': '/home/nimish/PycharmProjects/ProLoggerBackend/ProLogger/venv/lib/python3.6/site-packages/django/core/handlers/exception.py', 'filename': 'django/core/handlers/exception.py', 'module': 'django.core.handlers.exception', 'function': 'inner', 'lineno': 34, 'vars': {'exc': "ZeroDivisionError('division by zero',)", 'request': '<WSGIRequest at 0x140093367532736>', 'get_response': '<bound method BaseHandler._get_response of <django.core.handlers.wsgi.WSGIHandler object at 0x7f6a08e8b518>>'}, 'pre_context': ['    can rely on getting a response instead of an exception.', '    """', '    @wraps(get_response)', '    def inner(request):', '        try:'], 'context_line': '            response = get_response(request)', 'post_context': ['        except Exception as exc:', '            response = response_for_exception(request, exc)', '        return response', '    return inner', ''], 'in_app': False}, {'abs_path': '/home/nimish/PycharmProjects/ProLoggerBackend/ProLogger/venv/lib/python3.6/site-packages/django/core/handlers/base.py', 'filename': 'django/core/handlers/base.py', 'module': 'django.core.handlers.base', 'function': '_get_response', 'lineno': 115, 'vars': {'wrapped_callback': '<function sample from Project.api.views at 0x7f6a08519b70>', 'middleware_method': '<bound method CsrfViewMiddleware.process_view of <django.middleware.csrf.CsrfViewMiddleware object at 0x7f6a0798e978>>', 'callback_kwargs': {}, 'callback_args': [], 'callback': '<function sample from Project.api.views at 0x7f6a08519b70>', 'resolver_match': 'ResolverMatch(func=Project.api.views.sample, args=(), kwargs={}, url_name=None, app_names=[], namespaces=[], route=^projects/sample/)', 'resolver': "<URLResolver 'ProLogger.urls' (None:None) '^/'>", 'response': None, 'request': '<WSGIRequest at 0x140093367532736>', 'self': '<django.core.handlers.wsgi.WSGIHandler object at 0x7f6a08e8b518>'}, 'pre_context': ['        if response is None:', '            wrapped_callback = self.make_view_atomic(callback)', '            try:', '                response = wrapped_callback(request, *callback_args, **callback_kwargs)', '            except Exception as e:'], 'context_line': '                response = self.process_exception_by_middleware(e, request)', 'post_context': ['', '        # Complain if the view returned None (a common error).', '        if response is None:', '            if isinstance(callback, types.FunctionType):    # FBV', '                view_name = callback.__name__'], 'in_app': False}, {'abs_path': '/home/nimish/PycharmProjects/ProLoggerBackend/ProLogger/venv/lib/python3.6/site-packages/django/core/handlers/base.py', 'filename': 'django/core/handlers/base.py', 'module': 'django.core.handlers.base', 'function': '_get_response', 'lineno': 113, 'vars': {'wrapped_callback': '<function sample from Project.api.views at 0x7f6a08519b70>', 'middleware_method': '<bound method CsrfViewMiddleware.process_view of <django.middleware.csrf.CsrfViewMiddleware object at 0x7f6a0798e978>>', 'callback_kwargs': {}, 'callback_args': [], 'callback': '<function sample from Project.api.views at 0x7f6a08519b70>', 'resolver_match': 'ResolverMatch(func=Project.api.views.sample, args=(), kwargs={}, url_name=None, app_names=[], namespaces=[], route=^projects/sample/)', 'resolver': "<URLResolver 'ProLogger.urls' (None:None) '^/'>", 'response': None, 'request': '<WSGIRequest at 0x140093367532736>', 'self': '<django.core.handlers.wsgi.WSGIHandler object at 0x7f6a08e8b518>'}, 'pre_context': ['                break', '', '        if response is None:', '            wrapped_callback = self.make_view_atomic(callback)', '            try:'], 'context_line': '                response = wrapped_callback(request, *callback_args, **callback_kwargs)', 'post_context': ['            except Exception as e:', '                response = self.process_exception_by_middleware(e, request)', '', '        # Complain if the view returned None (a common error).', '        if response is None:'], 'in_app': False}, {'abs_path': '/home/nimish/PycharmProjects/ProLoggerBackend/ProLogger/Project/api/views.py', 'filename': 'Project/api/views.py', 'module': 'Project.api.views', 'function': 'sample', 'lineno': 36, 'vars': {'b': '50', 'a': '40', 'request': '<WSGIRequest at 0x140093367532736>'}, 'pre_context': ['', 'def sample(request):', '    a = 40', '    b = 50', "    print('hehehe')"], 'context_line': '    print(a/(b-50))', 'post_context': ['    print("hahahah")', "    print('hohoho')", '    return'], 'in_app': True}]}}]}, 'server_name': 'nimish-Lenovo-ideapad-320-15IKB', 'modules': {'django': '2.2.3', 'rest_framework': '3.10.1', 'raven': '6.10.0', 'python': '3.6.9'}, 'release': '3211a5f7684be2bb9e10a3ae16f09000bf617944', 'transaction': '/projects/sample/', 'message': 'ZeroDivisionError: division by zero', 'project': '1442732', 'timestamp': '2019-08-07T19:26:39Z', 'time_spent': None, 'event_id': '49b967d872494e0f9a45587e53450fb7', 'platform': 'python', 'sdk': {'name': 'raven-python', 'version': '6.10.0'}, 'repos': {}, 'breadcrumbs': {'values': [{'type': 'default', 'timestamp': 1565205991.2686882, 'level': None, 'message': 'SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date" FROM "django_session" WHERE ("django_session"."expire_date" > \'2019-08-07 19:26:31.267072\' AND "django_session"."session_key" = \'ar8qsiz69b96byzsrrzzfdnbswmgrlmq\')', 'category': 'query', 'data': None}, {'type': 'default', 'timestamp': 1565205991.2696812, 'level': None, 'message': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'category': 'query', 'data': None}, {'type': 'default', 'timestamp': 1565205991.665997, 'level': None, 'message': 'SELECT "django_admin_log"."id", "django_admin_log"."action_time", "django_admin_log"."user_id", "django_admin_log"."content_type_id", "django_admin_log"."object_id", "django_admin_log"."object_repr", "django_admin_log"."action_flag", "django_admin_log"."change_message", "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined", "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_admin_log" INNER JOIN "auth_user" ON ("django_admin_log"."user_id" = "auth_user"."id") LEFT OUTER JOIN "django_content_type" ON ("django_admin_log"."content_type_id" = "django_content_type"."id") WHERE "django_admin_log"."user_id" = 1 ORDER BY "django_admin_log"."action_time" DESC  LIMIT 10', 'category': 'query', 'data': None}, {'type': 'default', 'timestamp': 1565205991.6769423, 'level': 'info', 'message': '"GET /admin/ HTTP/1.1" 200 6825', 'category': 'django.server', 'data': {'request': "<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 35382)>", 'server_time': '07/Aug/2019 19:26:31', 'status_code': 200}}, {'type': 'default', 'timestamp': 1565205999.35821, 'level': None, 'message': 'SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date" FROM "django_session" WHERE ("django_session"."expire_date" > \'2019-08-07 19:26:39.352138\' AND "django_session"."session_key" = \'ar8qsiz69b96byzsrrzzfdnbswmgrlmq\')', 'category': 'query', 'data': None}, {'type': 'default', 'timestamp': 1565205999.3598962, 'level': None, 'message': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'category': 'query', 'data': None}]}}

# keys
emit_data_keys = ['project', 'breadcrumbs', 'level', 'repos', 'platform', 'modules', 'time_spent', 'event_id', 'user', 'timestamp', 'extra', 'tags', 'sdk', 'exception', 'request', 'server_name', 'release', 'message', 'transaction']

emit_data['project'] = 1442732
emit_data['level'] = 40
emit_data['platform'] = 'python'
emit_data['modules'] = {
    'django': '2.2.3',
    'python': '3.6.9',
    'raven': '6.10.0',
    'rest_framework': '3.10.1'
}

emit_data['event_id'] = '49b967d872494e0f9a45587e53450fb7'
emit_data['user'] = {'email': '', 'id': 1, 'ip_address': '127.0.0.1', 'username': 'nimish'}
emit_data['timestamp'] = '2019-08-07T19:26:39Z'
emit_data['extra'] = {'sys.argv': ["'manage.py'", "'runserver'"]}
emit_data['sdk'] = {'name': 'raven-python', 'version': '6.10.0'}

emit_data['request']['headers'] = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '',
    'Content-Type': 'text/plain',
    'Cookie': 'djdt=hide; csrftoken=BrhAIWFHL8htsLS5eFtfJUOs08qFEpiisYNJIhrqYWB8ACaBOfRH563XwNGOfWpG; sessionid=ar8qsiz69b96byzsrrzzfdnbswmgrlmq',
    'Host': '127.0.0.1:8000',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36'
}

emit_data['request']['env'] = {'REMOTE_ADDR': '127.0.0.1', 'SERVER_NAME': 'localhost', 'SERVER_PORT': '8000'}
emit_data['request']['method'] = 'GET'
emit_data['request']['url'] = 'http://127.0.0.1:8000/projects/1/sample/'
emit_data['request']['cookies'] = {
    'csrftoken': 'BrhAIWFHL8htsLS5eFtfJUOs08qFEpiisYNJIhrqYWB8ACaBOfRH563XwNGOfWpG',
    'djdt': 'hide',
    'sessionid': 'ar8qsiz69b96byzsrrzzfdnbswmgrlmq'
}
emit_data['request']['data']
emit_data['request']['query_string']

emit_data['message'] = 'ZeroDivisionError: division by zero'
emit_data['transaction'] = '/projects/sample/'


#####
emit_data['exception']['values'][0]['type'] = 'ZeroDivisionError'
emit_data['exception']['values'][0]['value'] = 'division by zero'

emit_data['exception']['values'][0]['stacktrace']['frames'][3] = {
    'abs_path': '/home/nimish/PycharmProjects/ProLoggerBackend/ProLogger/Project/api/views.py',
    'context_line': '    print(a/(b-50))',
    'filename': 'Project/api/views.py',
    'function': 'sample',
    'in_app': True,
    'lineno': 36,
    'module': 'Project.api.views',
    'post_context': ['    print("hahahah")', "    print('hohoho')", '    return'],
    'pre_context': [
        '',
        'def sample(request):',
        '    a = 40',
        '    b = 50',
        "    print('hehehe')"
    ],
    'vars': {'a': '40',
    'b': '50',
    'request': '<WSGIRequest at 0x140093367532736>'}
}

sample = emit_data['exception']['values'][0]['stacktrace']['frames'][3]


def print_frame(frame):
    for i in frame['pre_context']:
        print(i)
    print("###########################################")
    print(frame['context_line'])
    print("##########################################")
    for i in frame['post_context']:
        print(i)


def print_stacktrace(frames_list):
    for frame in frames_list[::-1]:
        print_frame(frame)
        print("------------------------------------------")


frames_list = emit_data['exception']['values'][0]['stacktrace']['frames']
print_stacktrace(frames_list)
q=emit_data['exception']['values'][0]['stacktrace']['frames']