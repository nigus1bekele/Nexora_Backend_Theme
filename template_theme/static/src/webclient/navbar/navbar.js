// Template Theme: customize this file for your theme.
/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { useService } from '@web/core/utils/hooks';
import { registry } from '@web/core/registry';
import { onMounted, onPatched, onWillUnmount, useRef, useState } from '@odoo/owl';
import { NavBar } from '@web/webclient/navbar/navbar';
import { AppsMenu } from "@template_theme/webclient/appsmenu/appsmenu";
import { session } from "@web/session";
import { browser } from "@web/core/browser/browser";

// Patching the standard NavBar to add custom functionality and references.
patch(NavBar.prototype, {
	setup() {
        super.setup();
        this.appMenuService = useService('app_menu');
        this.commandService = useService('command');
        this.companyService = useService('company');
        this.actionService = useService('action');
        this.user = session; // Expose session user data

        this.mobileSidebarState = useState({ isOpen: false });
        this.toggleMobileSidebar = () => {
             this.mobileSidebarState.isOpen = !this.mobileSidebarState.isOpen;
        };
        this.closeMobileSidebar = () => {
             this.mobileSidebarState.isOpen = false;
        };

        this.searchState = useState({ open: false, query: '', results: [], loading: false });
        this.searchContainerRef = useRef('searchContainer');
        this.searchInputRef = useRef('searchInput');
        this.searchRequestId = 0;
        this.searchFooterTips = registry
            .category('command_setup')
            .getEntries()
            .map(([namespace, config]) => ({ namespace, name: config.name }))
            .filter((entry) => entry.name);
        this.onDocumentClick = (ev) => {
            const container = this.searchContainerRef?.el;
            if (!container) {
                return;
            }
            if (this.searchState.open && !container.contains(ev.target)) {
                this.searchState.open = false;
            }
        };
        this.onDocumentKeydown = (ev) => {
            if (ev.key === 'Escape' && this.searchState.open) {
                this.searchState.open = false;
            }
        };
        
        this.getCompanyLogo = () => {
            const companyId = this.companyService.currentCompany ? this.companyService.currentCompany.id : '';
            return `/web/binary/company_logo?company=${companyId}`;
        };

        this.onLogoClick = () => {
            this.actionService.doAction("template_theme.home");
        };

        this.getApps = () => {
            return this.appMenuService.getAppsMenuItems().filter(app => 
                app.xmlid !== 'base.menu_administration' && 
                app.xmlid !== 'base.menu_management'
            );
        };

        this.getSettingsApp = () => {
            return this.appMenuService.getAppsMenuItems().find(app => app.xmlid === 'base.menu_administration');
        };

        this.getAppsApp = () => {
            return this.appMenuService.getAppsMenuItems().find(app => app.xmlid === 'base.menu_management');
        };

        // References to horizontal scrollers in the custom navbar.
        this.appsRowRef = useRef('appsRow');
        this.appsScrollerRef = useRef('appsScroller');
        this.subnavScrollerRef = useRef('subnavScroller');
        this.updateAppsOverflow = () => {
            const rowEl = this.appsRowRef?.el;
            const scrollerEl = this.appsScrollerRef?.el;
            if (!rowEl || !scrollerEl) {
                return;
            }
            const isOverflowing = scrollerEl.scrollWidth > scrollerEl.clientWidth + 1;
            rowEl.classList.toggle('is-overflowing', isOverflowing);
        };
        this.onAppsResize = () => {
            this.updateAppsOverflow();
        };
        this.ensureActiveAppVisible = () => {
            const scrollerEl = this.appsScrollerRef?.el;
            if (!scrollerEl) {
                return;
            }
            const activePill = scrollerEl.querySelector('.my_theme_app_pill.is-active');
            if (!activePill) {
                return;
            }
            activePill.scrollIntoView({
                behavior: 'smooth',
                block: 'nearest',
                inline: 'center',
            });
        };

        const appIconAlias = {
            sale_management: 'sale',
            base: 'settings',
            template_theme: 'home',
        };

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
            const iconData = app.webIconData;
            if (iconData) {
                if (iconData.startsWith('data:image')) {
                    return iconData;
                }
                if (iconData.startsWith('/')) {
                    return iconData;
                }
                const prefix = iconData.startsWith('P')
                    ? 'data:image/svg+xml;base64,'
                    : 'data:image/png;base64,';
                return prefix + iconData.replace(/\s/g, '');
            }
            return '/web/static/img/default_icon_app.png';
        };

        onMounted(() => {
            this.updateAppsOverflow();
            this.ensureActiveAppVisible();
            window.addEventListener('resize', this.onAppsResize);
            document.addEventListener('click', this.onDocumentClick);
            document.addEventListener('keydown', this.onDocumentKeydown);
            const scrollerEl = this.appsScrollerRef?.el;
            if (scrollerEl) {
                scrollerEl.addEventListener('scroll', this.onAppsResize, { passive: true });
            }
        });

        onPatched(() => {
            this.updateAppsOverflow();
            this.ensureActiveAppVisible();
        });

        onWillUnmount(() => {
            window.removeEventListener('resize', this.onAppsResize);
            document.removeEventListener('click', this.onDocumentClick);
            document.removeEventListener('keydown', this.onDocumentKeydown);
            const scrollerEl = this.appsScrollerRef?.el;
            if (scrollerEl) {
                scrollerEl.removeEventListener('scroll', this.onAppsResize);
            }
        });
    },

    toggleSearchPopover(ev) {
        if (ev) {
            ev.stopPropagation();
        }
        this.searchState.open = !this.searchState.open;
        if (this.searchState.open) {
            requestAnimationFrame(() => {
                this.searchInputRef?.el?.focus?.();
            });
            if (this.searchState.query) {
                this.runSearch();
            }
        }
    },

    onSearchInput(ev) {
        this.searchState.query = ev?.target?.value || '';
        if (!this.searchState.open) {
            this.searchState.open = true;
        }
        this.runSearch();
    },

    // Kept for template compatibility: mobile markup calls _onSearchChange.
    _onSearchChange(ev) {
        this.onSearchInput(ev);
    },

    getSearchFooterTips() {
        return this.searchFooterTips;
    },

    applySearchNamespace(namespace) {
        this.searchState.query = `${namespace}`;
        const input = this.searchInputRef?.el;
        if (input) {
            input.value = this.searchState.query;
            input.focus();
            input.setSelectionRange(input.value.length, input.value.length);
        }
        this.runSearch();
    },

    parseSearchNamespaces(query) {
        const trimmed = (query || '').trimStart();
        const prefix = trimmed[0];
        if (['/', '@', '#'].includes(prefix)) {
            return { namespaces: [prefix], searchValue: trimmed.slice(1).trimStart() };
        }
        return { namespaces: ['/', '@'], searchValue: trimmed };
    },

    async runSearch() {
        const { namespaces, searchValue } = this.parseSearchNamespaces(this.searchState.query);
        if (!searchValue) {
            this.searchState.results = [];
            this.searchState.loading = false;
            return;
        }
        const requestId = ++this.searchRequestId;
        this.searchState.loading = true;
        const providers = registry.category('command_provider').getAll();
        const matchingProviders = providers.filter((provider) => {
            const providerNamespace = provider.namespace || 'default';
            return namespaces.includes(providerNamespace);
        });
        const results = (await Promise.all(
            matchingProviders.map((provider) => provider.provide(this.env, { searchValue }))
        )).flat();

        if (requestId !== this.searchRequestId) {
            return;
        }

        this.searchState.results = results
            .map((command, index) => ({
                id: command.id || `${command.name}-${index}`,
                name: command.name,
                href: command.href,
                action: command.action,
                iconUrl: command?.props?.imgUrl || command?.props?.webIconData,
            }))
            .slice(0, 12);
        this.searchState.loading = false;
    },

    onSearchSelect(command) {
        this.searchState.open = false;
        if (command?.action) {
            command.action();
        } else if (command?.href) {
            browser.location.href = this._normalizeBackendHref(command.href);
        }
    },

    _normalizeBackendHref(href) {
        if (!href) {
            return href;
        }
        if (href.startsWith('/odoo')) {
            const clean = href.substring(5);
            return clean.startsWith('/') ? clean : `/${clean}`;
        }
        if (href === '/web' || href.startsWith('/web/') || href.startsWith('/web#')) {
            const clean = href.substring(4);
            return clean ? (clean.startsWith('/') ? clean : `/${clean}`) : '/';
        }
        return href;
    },

    /**
     * Opens the Odoo command palette (Ctrl+K).
     */
    openCommandPalette(ev) {
        if (ev) {
            ev.stopPropagation();
            if (ev.target && typeof ev.target.blur === 'function') {
                ev.target.blur();
            }
        }
        if (this.commandService) {
            this.commandService.openMainPalette();
        }
    },

    /**
     * Handles smooth scrolling for horizontal menu rows.
     * @param {string} refName - The name of the scroller ('apps' or 'subnav').
     * @param {number} direction - The direction to scroll (1 for right, -1 for left).
     */
    onScrollRow(refName, direction) {
        const refMap = {
            apps: this.appsScrollerRef,
            subnav: this.subnavScrollerRef,
        };
        const target = refMap[refName]?.el;
        if (!target) {
            return;
        }
        target.scrollBy({ left: direction * 220, behavior: 'smooth' });
    },

    /**
     * Trigger a click on a systray item rendered in the hidden proxy container.
     * @param {string} selector
     */
    triggerSystrayClick(selector) {
        const proxy = document.querySelector('.tt_systray_proxy');
        if (!proxy) {
            return;
        }
        const target = proxy.querySelector(selector);
        if (!target) {
            return;
        }
        const clickable = target.querySelector('button, .dropdown-toggle, a, i') || target;
        clickable.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
    },

    /**
     * Mobile Menu Actions
     */
    onMobileAction(mode) {
         if (mode === 'logout') {
            browser.location.href = '/web/session/logout';
         } else if (mode === 'settings') {
            this.actionService.doAction('base.action_res_users_my');
         } else if (mode === 'messages') {
            this.actionService.doAction('mail.action_discuss');
         } else if (mode === 'notifications') {
            // Open activities or inbox
             this.actionService.doAction('mail.action_discuss', { active_id: 'mail.box_inbox' });
         }
    },
});

// Register the custom AppsMenu component in the NavBar.
patch(NavBar, {
    components: {
        ...NavBar.components,
        AppsMenu,
    },
});
