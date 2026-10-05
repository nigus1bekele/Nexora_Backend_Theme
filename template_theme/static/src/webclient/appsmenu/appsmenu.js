// Template Theme: customize this file for your theme.
/** @odoo-module **/

import { useEffect } from "@odoo/owl";
import { url } from "@web/core/utils/urls";
import { useBus, useService } from "@web/core/utils/hooks";
import { Dropdown } from "@web/core/dropdown/dropdown";

/**
 * AppsMenu Component
 * Extends the standard Dropdown to create a full-screen app launcher.
 */
export class AppsMenu extends Dropdown {
    setup() {
    	super.setup();
    	this.commandPaletteOpen = false;
        this.commandService = useService("command");
    	this.companyService = useService('company');

        // Set the background image for the apps menu.
    	if (this.companyService.currentCompany.has_background_image) {
            this.imageUrl = url('/web/image', {
                model: 'res.company',
                field: 'background_image',
                id: this.companyService.currentCompany.id,
            });
    	} else {
            // Fallback to a default background image.
			this.imageUrl = '/template_theme/static/src/img/background.png';
    	}

        // Effect to handle opening the command palette when typing while the apps menu is open.
        useEffect(
            (isOpen) => {
            	if (isOpen) {
            		const openMainPalette = (ev) => {
            	    	if (
            	    		!this.commandServiceOpen && 
            	    		ev.key.length === 1 &&
            	    		!ev.ctrlKey &&
            	    		!ev.altKey
            	    	) {
	            	        this.commandService.openMainPalette(
            	        		{ searchValue: `/${ev.key}` }, 
            	        		() => { this.commandPaletteOpen = false; }
            	        	);
	            	    	this.commandPaletteOpen = true;
            	    	}
            		}
	            	window.addEventListener("keydown", openMainPalette);
	                return () => {
	                	window.removeEventListener("keydown", openMainPalette);
	                	this.commandPaletteOpen = false;
	                }
            	}
            },
            () => [this.state.isOpen]
		);

        // Close the apps menu when an action is performed.
    	useBus(this.env.bus, "ACTION_MANAGER:UI-UPDATED", this.state.close);
    }

    /**
     * Called when the apps menu dropdown is opened.
     * Applies the background image to the menu element.
     */
    onOpened() {
		super.onOpened();
		if (this.menuRef && this.menuRef.el) {
			this.menuRef.el.style.backgroundImage = `url('${this.imageUrl}')`;
		}
    }
}
