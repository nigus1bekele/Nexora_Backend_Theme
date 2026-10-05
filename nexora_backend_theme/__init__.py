from . import models
from . import controllers

import base64

from odoo.tools import file_open


def _setup_module(env):
    env['ir.config_parameter'].sudo().set_param(
        'nexora_backend_theme.color_topbar_background',
        '#2393D2',
    )
    env['ir.config_parameter'].sudo().set_param(
        'nexora_backend_theme.color_topbar_text',
        '#FFFFFF',
    )
    if env.ref('base.main_company', False):
        company = env.ref('base.main_company')
        with file_open('nexora_backend_theme/static/src/img/hero_nexora_blue_halftone.png', 'rb') as file:
            company.write({
                'hero_section_bg': base64.b64encode(file.read()),
                'use_custom_hero_section_bg': False,
            })


def _uninstall_cleanup(env):
    env['ir.attachment'].search([('url', 'like', '/web/assets/%nexora_backend_theme/%')]).unlink()
    env['ir.asset'].search([
        '|', ('path', 'like', '%nexora_backend_theme/%'),
        ('target', 'like', 'nexora_backend_theme/%'),
    ]).unlink()
    env['ir.config_parameter'].search([('key', 'like', 'nexora_backend_theme.%')]).unlink()

    env.registry.clear_cache('assets')
