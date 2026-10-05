from . import models

import base64

from odoo.tools import file_open


def _setup_module(env):
    if env.ref('base.main_company', False): 
        company = env.ref('base.main_company')
        with file_open('template_theme/static/src/img/favicon.png', 'rb') as file:
            company.write({
                'favicon': base64.b64encode(file.read())
            })
        with file_open('template_theme/static/src/img/background.png', 'rb') as file:
            company.write({
                'background_image': base64.b64encode(file.read())
            })
        with file_open('template_theme/static/src/img/logo.png', 'rb') as file:
            company.write({
                'logo': base64.b64encode(file.read())
            })


def _uninstall_cleanup(env):
    env['res.config.settings']._reset_theme_color_assets()
