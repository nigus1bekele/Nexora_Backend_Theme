// Template Theme: customize this file for your theme.
/** @odoo-module **/

import { url } from '@web/core/utils/urls';
import { useService } from '@web/core/utils/hooks';
import { Component, onWillUnmount } from '@odoo/owl';

/**
 * AppsBar Component
 * This component renders the vertical sidebar containing app icons.
 */
export class AppsBar extends Component {
    static template = 'template_theme_appsbar.AppsBar';
    static props = {};

	setup() {
		this.companyService = useService('company');
        this.appMenuService = useService('app_menu');

        const appIconAlias = {
            sale_management: 'sale',
            base: 'settings',
            template_theme: 'home',
        };

        // Set the sidebar background image if configured for the current company.
    	if (this.companyService.currentCompany.has_appsbar_image) {
            this.sidebarImageUrl = url('/web/image', {
                model: 'res.company',
                field: 'appbar_image',
                id: this.companyService.currentCompany.id,
            });
    	}

        /**
         * Resolves the icon for an app.
         * Tries to find a theme-specific icon first.
         */
        this.getAppIcon = (app) => {
            if (app.xmlid) {
                if (app.xmlid === 'base.menu_management') {
                    return `/template_theme/static/src/img/apps/Apps.png`;
                }
                const moduleName = app.xmlid.split('.')[0];
                const iconName = appIconAlias[moduleName];
                if (iconName) {
                    return `/template_theme/static/src/img/apps/${iconName}.png`;
                }
            }
            return app.webIconData || '/base/static/description/icon.png';
        };

        // Re-render the sidebar when the active app changes.
    	const renderAfterMenuChange = () => {
            this.render();
        };
        this.env.bus.addEventListener(
        	'MENUS:APP-CHANGED', renderAfterMenuChange
        );

        // Clean up the event listener when the component is unmounted.
        onWillUnmount(() => {
            this.env.bus.removeEventListener(
            	'MENUS:APP-CHANGED', renderAfterMenuChange
            );
        });
    }

    /**
     * Handles clicking on an app icon in the sidebar.
     * @param {Object} app - The app object that was clicked.
     */
    _onAppClick(app) {
        return this.appMenuService.selectApp(app);
    }
}
