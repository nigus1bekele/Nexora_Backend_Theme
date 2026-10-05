{
    'name': 'Nexora Backend Theme Suite',
    'summary': 'A clean, modern backend theme for Odoo Community with flexible customization.',
    'description': '''
        Nexora Backend Theme is a polished, modern theme for Odoo Community that delivers
        a clean UI, responsive layout, and configurable styling. It provides
        ready-to-use assets, settings, and views to speed up branding
        and customization work.
    ''',
    'version': '18.0.1.0.1',
    'category': 'Themes/Backend',
    'license': 'LGPL-3',
    'author': 'Nexora',
    'website': 'robelbekele4.00@gmail.com',
    'depends': [
        'base_setup',
        'mail',
        'web',
        'web_editor',
        'auth_signup',
    ],
    'data': [
        'data/navbar_cyan.xml',
        'templates/web_layout.xml',
        'templates/webclient_colors.xml',
        'templates/webclient_appsbar.xml',
        'views/login.xml',
        'views/reset_pwd.xml',
        'views/home.xml',
        'views/res_config_settings.xml',
        'views/res_users_appsbar.xml',
        'views/res_users_chatter.xml',
        'views/res_users_dialog.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'nexora_backend_theme/static/src/scss/colors.scss'),
            (
                'before',
                'nexora_backend_theme/static/src/scss/colors.scss',
                'nexora_backend_theme/static/src/scss/colors_light.scss',
            ),
            'nexora_backend_theme/static/src/scss/appsbar.variables.scss',
            (
                'after',
                'web/static/src/scss/primary_variables.scss',
                'nexora_backend_theme/static/src/scss/variables.scss',
            ),
        ],
        'web._assets_backend_helpers': [
            'nexora_backend_theme/static/src/scss/appsbar.mixins.scss',
        ],
        'web.assets_web_dark': [
            (
                'after',
                'nexora_backend_theme/static/src/scss/appsbar.variables.scss',
                'nexora_backend_theme/static/src/scss/appsbar.variables.dark.scss',
            ),
            (
                'after',
                'nexora_backend_theme/static/src/scss/colors.scss',
                'nexora_backend_theme/static/src/scss/colors_dark.scss',
            ),
        ],
        'web.assets_frontend': [
            'nexora_backend_theme/static/src/webclient/login/login.scss',
            'nexora_backend_theme/static/src/webclient/login/reset_pwd.scss',
        ],
        'web.assets_backend': [
            'nexora_backend_theme/static/src/webclient/**/*.xml',
            'nexora_backend_theme/static/src/webclient/**/*.scss',
            'nexora_backend_theme/static/src/webclient/**/*.js',
            'nexora_backend_theme/static/src/core/**/*.xml',
            'nexora_backend_theme/static/src/core/**/*.scss',
            'nexora_backend_theme/static/src/core/**/*.js',
            'nexora_backend_theme/static/src/chatter/**/*.xml',
            'nexora_backend_theme/static/src/chatter/**/*.scss',
            'nexora_backend_theme/static/src/chatter/**/*.js',
            'nexora_backend_theme/static/src/views/**/*.scss',
            'nexora_backend_theme/static/src/views/**/*.js',
        ],
    },
    'images': [
        'static/description/icon.png',
        'static/description/banner.png',
    ],
    'post_init_hook': '_setup_module',
    'uninstall_hook': '_uninstall_cleanup',
}
