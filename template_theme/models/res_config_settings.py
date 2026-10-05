from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    def _template_theme_color_fields(self):
        return [
            'color_appsmenu_text',
            'color_appbar_text',
            'color_appbar_active',
            'color_appbar_background',
            'color_theme_primary',
            'color_theme_background',
            'color_theme_text',
            'color_theme_text_muted',
            'color_theme_text_hover',
            'color_theme_button',
            'color_theme_button_text',
        ]

    @property
    def COLOR_ASSET_THEME_URL(self):
        return 'template_theme/static/src/scss/colors.scss'
        
    @property
    def COLOR_BUNDLE_THEME_NAME(self):
        return 'web._assets_primary_variables'
    
    #----------------------------------------------------------
    # Fields
    #----------------------------------------------------------
    
    theme_favicon = fields.Binary(
        related='company_id.favicon',
        readonly=False
    )
    
    theme_background_image = fields.Binary(
        related='company_id.background_image',
        readonly=False
    )
    
    theme_color_appsmenu_text = fields.Char(
        string='Apps Menu Text Color',
        config_parameter='template_theme.color_appsmenu_text',
    )
    
    theme_color_appbar_text = fields.Char(
        string='AppsBar Text Color',
        config_parameter='template_theme.color_appbar_text',
    )
    
    theme_color_appbar_active = fields.Char(
        string='AppsBar Active Color',
        config_parameter='template_theme.color_appbar_active',
    )
    
    theme_color_appbar_background = fields.Char(
        string='AppsBar Background Color',
        config_parameter='template_theme.color_appbar_background',
    )

    theme_color_theme_primary = fields.Char(
        string='Theme Primary Color',
        config_parameter='template_theme.color_theme_primary',
    )

    theme_color_theme_background = fields.Char(
        string='Theme Background Color',
        config_parameter='template_theme.color_theme_background',
    )

    theme_color_theme_text = fields.Char(
        string='Theme Text Color',
        config_parameter='template_theme.color_theme_text',
    )

    theme_color_theme_text_muted = fields.Char(
        string='Theme Muted Text Color',
        config_parameter='template_theme.color_theme_text_muted',
    )

    theme_color_theme_text_hover = fields.Char(
        string='Theme Text Hover Color',
        config_parameter='template_theme.color_theme_text_hover',
    )

    theme_color_theme_button = fields.Char(
        string='Theme Button Color',
        config_parameter='template_theme.color_theme_button',
    )

    theme_color_theme_button_text = fields.Char(
        string='Theme Button Text Color',
        config_parameter='template_theme.color_theme_button_text',
    )
    
    #----------------------------------------------------------
    # Helper
    #----------------------------------------------------------
    
    def _reset_theme_color_assets(self):
        self.env['web_editor.assets'].reset_asset(
            self.COLOR_ASSET_THEME_URL, 
            self.COLOR_BUNDLE_THEME_NAME,
        )
    
    #----------------------------------------------------------
    # Action
    #----------------------------------------------------------
    
    def action_reset_theme_color_assets(self):
        self._reset_light_color_assets()
        self._reset_dark_color_assets()
        self._reset_theme_color_assets()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
    
    #----------------------------------------------------------
    # Functions
    #----------------------------------------------------------
