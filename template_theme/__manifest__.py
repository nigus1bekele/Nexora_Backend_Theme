{
    'name': 'Template Backend Theme',
    'summary': 'Template backend theme for customization',
    'description': '''
        Template backend theme intended as a starting point for custom Odoo
        backend themes. Includes asset bundles, settings, and example views.
    ''',
    'version': '18.0.1.0.0',
    'category': 'Themes/Backend',
    'license': 'LGPL-3',
    'author': 'Robel',
    'website': '',
    'contributors': [],
    'depends': [
        'base_setup',
        'mail',
        'web',
        'web_editor',
        'auth_signup',
    ],
    'data': [
        'templates/web_layout.xml',
        'templates/webclient_colors.xml',
        'templates/webclient_appsbar.xml',
        'views/login.xml',
        'views/home.xml',
        'views/res_config_settings.xml',
        'views/res_users_appsbar.xml',
        'views/res_users_chatter.xml',
        'views/res_users_dialog.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'template_theme/static/src/scss/colors.scss'),
            (
                'before',
                'template_theme/static/src/scss/colors.scss',
                'template_theme/static/src/scss/colors_light.scss',
            ),
            'template_theme/static/src/scss/appsbar.variables.scss',
            (
                'after',
                'web/static/src/scss/primary_variables.scss',
                'template_theme/static/src/scss/variables.scss',
            ),
        ],
        'web._assets_backend_helpers': [
            'template_theme/static/src/scss/appsbar.mixins.scss',
        ],
        'web.assets_web_dark': [
            (
                'after',
                'template_theme/static/src/scss/appsbar.variables.scss',
                'template_theme/static/src/scss/appsbar.variables.dark.scss',
            ),
            (
                'after',
                'template_theme/static/src/scss/colors.scss',
                'template_theme/static/src/scss/colors_dark.scss',
            ),
        ],
        'web.assets_web': [
            'template_theme/static/src/legacy/form_controller_alias.js',
            'template_theme/static/src/webclient/**/*.xml',
            'template_theme/static/src/webclient/**/*.scss',
            'template_theme/static/src/webclient/**/*.js',
            'template_theme/static/src/core/**/*.xml',
            'template_theme/static/src/core/**/*.scss',
            'template_theme/static/src/core/**/*.js',
            'template_theme/static/src/chatter/**/*.xml',
            'template_theme/static/src/chatter/**/*.scss',
            'template_theme/static/src/chatter/**/*.js',
            'template_theme/static/src/views/**/*.scss',
            'template_theme/static/src/views/**/*.js',
        ],
        'web.assets_frontend': [
            'template_theme/static/src/webclient/login/login.scss',
        ],
        'web.assets_backend': [
            'template_theme/static/src/legacy/form_controller_alias.js',
        ],
    },
    'images': [
        'static/description/banner.png',
    ],

}
