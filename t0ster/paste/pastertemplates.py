from paste.script.templates import Template
from paste.script.templates import var
from random import choice


class DjangoTemplate(Template):
    vars = [
        var('version', 'Version (like 0.1)', default='0.1'),
        var('description', 'One-line description of the package'),
        var('long_description', 'Multi-line description (in reST)'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name'),
        var('zip_safe', 'True/False: if the package can be distributed as a .zip file',
            default=False),
    ]

    use_cheetah = True
    required_templates = []

    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(DjangoTemplate, self).check_vars(vars, command)


class DjangoAppTemplate(DjangoTemplate):
    _template_dir = 'templates/django_app'
    summary = 'Template for a basic Django reusable application'


def append_secret_key(vars):
    default_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    vars.append(
        var('secret_key', 'Secret key', default=default_key)
    )


class DjangoProjectTemplate(DjangoTemplate):
    _template_dir = 'templates/django_project'
    summary = 'Template for a Django project'

    def __init__(self, name):
        append_secret_key(self.vars)
        super(DjangoProjectTemplate, self).__init__(name)
