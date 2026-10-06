import base64

from odoo import fields, models
from odoo.tools import file_open


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'
    LOGIN_INFO_PANEL_PARAM = 'nexora_backend_theme.login_show_info_panel'

    def _nexora_backend_theme_color_fields(self):
        return [
            'color_appbar_active',
            'color_hero_overlay_start',
            'color_hero_overlay_end',
            'color_sidebar_background',
            'color_sidebar_text',
            'color_sidebar_icon',
            'color_sidebar_footer_text',
            'color_sidebar_footer_active_text',
            'color_company_name_text',
            'color_left_background',
            'color_left_text',
            'color_topbar_background',
            'color_topbar_text',
            'color_sidebar_active_indicator',
            'color_sidebar_active_background',
            'color_sidebar_active_text',
            'color_sidebar_active_icon',
            'color_sidebar_hover_background',
            'color_sidebar_hover_text',
            'color_badge_background',
            'color_badge_text',
            'color_theme_primary',
            'color_theme_background',
            'color_theme_text',
            'color_theme_text_muted',
            'color_theme_text_hover',
            'color_theme_button',
            'color_theme_button_text',
            'color_login_left_panel_bg',
            'color_login_right_panel_bg',
            'color_login_company_text',
            'color_login_motto_text',
            'color_login_other_button',
            'color_login_other_button_text',
            'color_home_kicker',
            'color_home_title',
            'color_home_lead',
        ]

    @property
    def COLOR_ASSET_THEME_URL(self):
        return 'nexora_backend_theme/static/src/scss/colors.scss'
        
    @property
    def COLOR_BUNDLE_THEME_NAME(self):
        return 'web._assets_primary_variables'
    
    #----------------------------------------------------------
    # Fields
    #----------------------------------------------------------
    
    theme_motto = fields.Char(
        related='company_id.motto',
        readonly=False
    )
    
    theme_hero_section_bg = fields.Binary(
        related='company_id.hero_section_bg',
        readonly=False
    )

    theme_use_custom_hero_section_bg = fields.Boolean(
        related='company_id.use_custom_hero_section_bg',
        readonly=False
    )

    theme_login_page_logo = fields.Binary(
        related='company_id.login_page_logo',
        readonly=False
    )

    theme_login_left_panel_bg_image = fields.Binary(
        related='company_id.login_left_panel_bg_image',
        readonly=False
    )

    theme_left_bg_image = fields.Binary(
        related='company_id.left_bg_image',
        readonly=False
    )
    
    # theme_color_appbar_active = fields.Char(
    #     string='AppsBar Active Color',
    #     config_parameter='nexora_backend_theme.color_appbar_active',
    #     default='#3058cf',
    # )

    theme_color_hero_overlay_start = fields.Char(
        string='Hero Overlay Start Color',
        config_parameter='nexora_backend_theme.color_hero_overlay_start',
        default='#19172E',
    )

    theme_color_hero_overlay_end = fields.Char(
        string='Hero Overlay End Color',
        config_parameter='nexora_backend_theme.color_hero_overlay_end',
        default='#19172E',
    )

    theme_hero_overlay_opacity = fields.Integer(
        string='Hero Overlay Opacity (%)',
        config_parameter='nexora_backend_theme.hero_overlay_opacity',
        default=0,
    )

    theme_color_sidebar_background = fields.Char(
        string='Sidebar Background Color',
        config_parameter='nexora_backend_theme.color_sidebar_background',
        default='#FFFFFF',
    )

    theme_color_sidebar_text = fields.Char(
        string='Sidebar Text Color',
        config_parameter='nexora_backend_theme.color_sidebar_text',
        default='#45435B',
    )

    theme_color_sidebar_icon = fields.Char(
        string='Sidebar Icon Color',
        config_parameter='nexora_backend_theme.color_sidebar_icon',
        default='#706E85',
    )

    theme_color_sidebar_footer_text = fields.Char(
        string='Sidebar Footer Text Color',
        config_parameter='nexora_backend_theme.color_sidebar_footer_text',
        default='#706E85',
    )

    theme_color_sidebar_footer_active_text = fields.Char(
        string='Sidebar Footer Active Text Color',
        config_parameter='nexora_backend_theme.color_sidebar_footer_active_text',
        default='#5746D8',
    )

    theme_color_company_name_text = fields.Char(
        string='Company Name Text Color',
        config_parameter='nexora_backend_theme.color_company_name_text',
        default='#19172E',
    )

    theme_color_left_background = fields.Char(
        string='Brand Background Color',
        config_parameter='nexora_backend_theme.color_left_background',
        default='#FFFFFF',
    )

    theme_color_left_text = fields.Char(
        string='Brand Text Color',
        config_parameter='nexora_backend_theme.color_left_text',
        default='#19172E',
    )

    theme_color_topbar_background = fields.Char(
        string='Top Bar Background Color',
        config_parameter='nexora_backend_theme.color_topbar_background',
        default='#19172E',
    )

    theme_color_topbar_text = fields.Char(
        string='Top Bar Text Color',
        config_parameter='nexora_backend_theme.color_topbar_text',
        default='#FFFFFF',
    )

    theme_color_sidebar_active_indicator = fields.Char(
        string='Sidebar Active Indicator Color',
        config_parameter='nexora_backend_theme.color_sidebar_active_indicator',
        default='#5746D8',
    )

    theme_color_sidebar_active_background = fields.Char(
        string='Sidebar Active Background Color',
        config_parameter='nexora_backend_theme.color_sidebar_active_background',
        default='#F0EEFF',
    )

    theme_color_sidebar_active_text = fields.Char(
        string='Sidebar Active Text Color',
        config_parameter='nexora_backend_theme.color_sidebar_active_text',
        default='#4636BD',
    )

    theme_color_sidebar_active_icon = fields.Char(
        string='Sidebar Active Icon Color',
        config_parameter='nexora_backend_theme.color_sidebar_active_icon',
        default='#5746D8',
    )

    theme_color_sidebar_hover_background = fields.Char(
        string='Sidebar Hover Background Color',
        config_parameter='nexora_backend_theme.color_sidebar_hover_background',
        default='#F6F5FB',
    )

    theme_color_sidebar_hover_text = fields.Char(
        string='Sidebar Hover Text Color',
        config_parameter='nexora_backend_theme.color_sidebar_hover_text',
        default='#19172E',
    )

    theme_color_badge_background = fields.Char(
        string='Badge Background Color',
        config_parameter='nexora_backend_theme.color_badge_background',
        default='#5746D8',
    )

    theme_color_badge_text = fields.Char(
        string='Badge Text Color',
        config_parameter='nexora_backend_theme.color_badge_text',
        default='#FFFFFF',
    )

    theme_color_theme_primary = fields.Char(
        string='Theme Primary Color',
        config_parameter='nexora_backend_theme.color_theme_primary',
        default='#5746D8',
    )

    theme_color_theme_background = fields.Char(
        string='Theme Background Color',
        config_parameter='nexora_backend_theme.color_theme_background',
        default='#F7F7FC',
    )

    theme_color_theme_text = fields.Char(
        string='Theme Text Color',
        config_parameter='nexora_backend_theme.color_theme_text',
        default='#19172E',
    )

    theme_color_theme_text_muted = fields.Char(
        string='Theme Muted Text Color',
        config_parameter='nexora_backend_theme.color_theme_text_muted',
        default='#706E85',
    )

    theme_color_theme_text_hover = fields.Char(
        string='Theme Text Hover Color',
        config_parameter='nexora_backend_theme.color_theme_text_hover',
        default='#19172E',
    )

    theme_color_theme_button = fields.Char(
        string='Theme Button Color',
        config_parameter='nexora_backend_theme.color_theme_button',
        default='#5746D8',
    )

    theme_color_theme_button_text = fields.Char(
        string='Theme Button Text Color',
        config_parameter='nexora_backend_theme.color_theme_button_text',
        default='#FFFFFF',
    )

    theme_login_show_info_panel = fields.Boolean(
        string='Show Login Info Panel',
        config_parameter=LOGIN_INFO_PANEL_PARAM,
        default=True,
    )

    theme_color_login_left_panel_bg = fields.Char(
        string='Login Left Panel Background',
        config_parameter='nexora_backend_theme.color_login_left_panel_bg',
        default='#19172E',
    )

    theme_color_login_right_panel_bg = fields.Char(
        string='Login Right Panel Background',
        config_parameter='nexora_backend_theme.color_login_right_panel_bg',
        default='#FFFFFF',
    )

    theme_color_login_company_text = fields.Char(
        string='Login Company Text Color',
        config_parameter='nexora_backend_theme.color_login_company_text',
        default='#5746D8',
    )

    theme_color_login_motto_text = fields.Char(
        string='Login Motto Text Color',
        config_parameter='nexora_backend_theme.color_login_motto_text',
        default='#B9B7CC',
    )

    theme_color_login_other_button = fields.Char(
        string='Auth Other Button Color',
        config_parameter='nexora_backend_theme.color_login_other_button',
        default='#F7F7FC',
    )

    theme_color_login_other_button_text = fields.Char(
        string='Auth Other Button Text Color',
        config_parameter='nexora_backend_theme.color_login_other_button_text',
        default='#19172E',
    )

    theme_color_home_kicker = fields.Char(
        string='Home Hero Kicker Color',
        config_parameter='nexora_backend_theme.color_home_kicker',
        default='#9DF6DC',
    )

    theme_color_home_title = fields.Char(
        string='Home Hero Title Color',
        config_parameter='nexora_backend_theme.color_home_title',
        default='#FFFFFF',
    )

    theme_color_home_lead = fields.Char(
        string='Home Hero Lead Color',
        config_parameter='nexora_backend_theme.color_home_lead',
        default='#E5E7EB',
    )

    theme_home_kicker_size = fields.Integer(
        string='Home Hero Kicker Size (px)',
        config_parameter='nexora_backend_theme.home_kicker_size',
        default=20,
    )

    theme_home_title_size = fields.Integer(
        string='Home Hero Title Size (px)',
        config_parameter='nexora_backend_theme.home_title_size',
        default=40,
    )

    theme_home_lead_size = fields.Integer(
        string='Home Hero Lead Size (px)',
        config_parameter='nexora_backend_theme.home_lead_size',
        default=16,
    )

    theme_home_kicker_weight = fields.Integer(
        string='Home Hero Kicker Weight',
        config_parameter='nexora_backend_theme.home_kicker_weight',
        default=700,
    )

    theme_home_title_weight = fields.Integer(
        string='Home Hero Title Weight',
        config_parameter='nexora_backend_theme.home_title_weight',
        default=800,
    )

    theme_home_lead_weight = fields.Integer(
        string='Home Hero Lead Weight',
        config_parameter='nexora_backend_theme.home_lead_weight',
        default=500,
    )
    
    #----------------------------------------------------------
    # Helper
    #----------------------------------------------------------
    
    def _reset_theme_color_assets(self):
        self.env['web_editor.assets'].reset_asset(
            self.COLOR_ASSET_THEME_URL, 
            self.COLOR_BUNDLE_THEME_NAME,
        )

    def _theme_color_param_keys(self):
        return [
            'nexora_backend_theme.color_appbar_active',
            'nexora_backend_theme.color_hero_overlay_start',
            'nexora_backend_theme.color_hero_overlay_end',
            'nexora_backend_theme.hero_overlay_opacity',
            'nexora_backend_theme.color_sidebar_background',
            'nexora_backend_theme.color_sidebar_text',
            'nexora_backend_theme.color_sidebar_icon',
            'nexora_backend_theme.color_sidebar_footer_text',
            'nexora_backend_theme.color_sidebar_footer_active_text',
            'nexora_backend_theme.color_company_name_text',
            'nexora_backend_theme.color_left_background',
            'nexora_backend_theme.color_left_text',
            'nexora_backend_theme.color_topbar_background',
            'nexora_backend_theme.color_topbar_text',
            'nexora_backend_theme.color_sidebar_active_indicator',
            'nexora_backend_theme.color_sidebar_active_background',
            'nexora_backend_theme.color_sidebar_active_text',
            'nexora_backend_theme.color_sidebar_active_icon',
            'nexora_backend_theme.color_sidebar_hover_background',
            'nexora_backend_theme.color_sidebar_hover_text',
            'nexora_backend_theme.color_badge_background',
            'nexora_backend_theme.color_badge_text',
            'nexora_backend_theme.color_theme_primary',
            'nexora_backend_theme.color_theme_background',
            'nexora_backend_theme.color_theme_text',
            'nexora_backend_theme.color_theme_text_muted',
            'nexora_backend_theme.color_theme_text_hover',
            'nexora_backend_theme.color_theme_button',
            'nexora_backend_theme.color_theme_button_text',
            'nexora_backend_theme.login_show_info_panel',
            'nexora_backend_theme.color_login_left_panel_bg',
            'nexora_backend_theme.color_login_right_panel_bg',
            'nexora_backend_theme.color_login_company_text',
            'nexora_backend_theme.color_login_motto_text',
            'nexora_backend_theme.color_login_other_button',
            'nexora_backend_theme.color_login_other_button_text',
            'nexora_backend_theme.color_home_kicker',
            'nexora_backend_theme.color_home_title',
            'nexora_backend_theme.color_home_lead',
            'nexora_backend_theme.home_kicker_size',
            'nexora_backend_theme.home_title_size',
            'nexora_backend_theme.home_lead_size',
            'nexora_backend_theme.home_kicker_weight',
            'nexora_backend_theme.home_title_weight',
            'nexora_backend_theme.home_lead_weight',
        ]

    def _to_bool_param(self, value, default=False):
        if value is None:
            return default
        return str(value).strip().lower() in ('1', 'true', 'yes', 'on')

    def get_values(self):
        res = super().get_values()
        raw_value = self.env['ir.config_parameter'].sudo().get_param(self.LOGIN_INFO_PANEL_PARAM)
        res['theme_login_show_info_panel'] = self._to_bool_param(raw_value, default=True)
        res['theme_color_topbar_background'] = '#19172E'
        res['theme_color_topbar_text'] = '#FFFFFF'
        return res

    def set_values(self):
        res = super().set_values()
        params = self.env['ir.config_parameter'].sudo()
        params.set_param(
            self.LOGIN_INFO_PANEL_PARAM,
            'True' if self.theme_login_show_info_panel else 'False',
        )
        params.set_param('nexora_backend_theme.color_topbar_background', '#19172E')
        params.set_param('nexora_backend_theme.color_topbar_text', '#FFFFFF')
        return res
    
    def _set_default_hero_section_bg(self):
        with file_open('nexora_backend_theme/static/src/img/hero_nexora_blue_halftone.png', 'rb') as file:
            default_hero = base64.b64encode(file.read())
        for settings in self:
            settings.company_id.sudo().write({
                'hero_section_bg': default_hero,
                'use_custom_hero_section_bg': False,
            })
            
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

    def action_reset_all_theme_settings(self):
        params = self.env['ir.config_parameter'].sudo()
        for key in self._theme_color_param_keys():
            params.search([('key', '=', key)]).unlink()
        for settings in self:
            settings.company_id.sudo().write({
                'motto': '',
                'left_bg_image': False,
                'login_page_logo': False,
                'login_left_panel_bg_image': False,
            })
        self._set_default_hero_section_bg()
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
