// Template Theme: customize this file for your theme.
/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { user } from "@web/core/user";
import { standardActionServiceProps } from "@web/webclient/actions/action_service";

class TemplateThemeHome extends Component {
    static template = "template_theme.Home";
    static props = { ...standardActionServiceProps };

    setup() {
        this.orm = useService("orm");
        this.state = useState({
            loading: true,
            metrics: [],
            moduleCards: [],
            focusItems: [],
            summary: {
                activityCount: 0,
                salesCount: 0,
                hasSales: false,
            },
            userName: user.name || "User",
        });

        onWillStart(() => this.loadHome());
    }

    async loadHome() {
        const formatter = new Intl.NumberFormat();
        const formatCount = (value) => formatter.format(value || 0);
        const today = new Date().toISOString().slice(0, 10);
        const modelCandidates = [
            "mail.activity",
            "sale.order",
            "account.move",
            "purchase.order",
            "stock.picking",
            "project.task",
            "res.partner",
        ];
        const modelRecords = await this.orm.searchRead(
            "ir.model",
            [["model", "in", modelCandidates]],
            ["model"]
        );
        const availableModels = new Set(modelRecords.map((record) => record.model));
        const hasModel = (model) => availableModels.has(model);

        const countCache = new Map();
        const getCount = async (model, domain) => {
            const cacheKey = `${model}:${JSON.stringify(domain)}`;
            if (countCache.has(cacheKey)) {
                return countCache.get(cacheKey);
            }
            const value = await this.orm.searchCount(model, domain);
            countCache.set(cacheKey, value);
            return value;
        };

        const metricDefs = [
            {
                key: "activities",
                label: "My Activities",
                model: "mail.activity",
                domain: [["user_id", "=", user.userId]],
                iconClass: "fa fa-check-circle",
                accentClass: "tt_stat_primary",
                iconClassName: "tt_stat_icon_blue",
                subtext: "Assigned to you",
            },
            {
                key: "sales",
                label: "Sales Orders",
                model: "sale.order",
                domain: [["state", "=", "sale"]],
                iconClass: "fa fa-line-chart",
                accentClass: "tt_stat_accent",
                iconClassName: "tt_stat_icon_green",
                subtext: "Confirmed orders",
            },
            {
                key: "invoices",
                label: "Invoices Due",
                model: "account.move",
                domain: [
                    ["move_type", "=", "out_invoice"],
                    ["state", "=", "posted"],
                    ["payment_state", "in", ["not_paid", "partial"]],
                ],
                iconClass: "fa fa-file-text-o",
                accentClass: "tt_stat_warning",
                iconClassName: "tt_stat_icon_orange",
                subtext: "Awaiting payment",
            },
            {
                key: "transfers",
                label: "Stock Transfers",
                model: "stock.picking",
                domain: [["state", "in", ["confirmed", "assigned", "waiting"]]],
                iconClass: "fa fa-truck",
                accentClass: "tt_stat_purple",
                iconClassName: "tt_stat_icon_purple",
                subtext: "Ready to process",
            },
        ];

        const metrics = [];
        for (const def of metricDefs) {
            if (!hasModel(def.model)) {
                continue;
            }
            const count = await getCount(def.model, def.domain);
            metrics.push({
                ...def,
                value: formatCount(count),
                rawValue: count,
            });
        }

        const salesMetric = metrics.find((metric) => metric.key === "sales");
        const activityMetric = metrics.find((metric) => metric.key === "activities");
        this.state.summary.activityCount = activityMetric ? activityMetric.rawValue : 0;
        this.state.summary.salesCount = salesMetric ? salesMetric.rawValue : 0;
        this.state.summary.hasSales = Boolean(salesMetric);

        let focusItems = [];
        if (hasModel("mail.activity")) {
            const activities = await this.orm.searchRead(
                "mail.activity",
                [["user_id", "=", user.userId]],
                ["summary", "res_name", "date_deadline", "activity_type_id"],
                { order: "date_deadline asc", limit: 6 }
            );
            focusItems = activities.map((activity, index) => {
                const title = activity.summary || activity.activity_type_id?.[1] || "Activity";
                const record = activity.res_name || "";
                const date = activity.date_deadline || "";
                return {
                    id: activity.id || index,
                    title,
                    record,
                    type: activity.activity_type_id?.[1] || "Task",
                    date,
                    isOverdue: Boolean(date && date < today),
                };
            });
        }

        const cardDefs = [
            {
                key: "accounting",
                title: "Accounting",
                description: "Track customer invoices and vendor bills.",
                model: "account.move",
                domain: [["state", "=", "draft"]],
                metricLabel: "Invoices Draft",
                headerClass: "tt_bg_blue",
                iconClass: "fa fa-file-text-o",
                watermarkClass: "fa fa-calculator",
                badge: "Review",
                badgeClass: "tt_badge_blue",
            },
            {
                key: "sales",
                title: "Sales",
                description: "Quotes, orders, and customer commitments.",
                model: "sale.order",
                domain: [["state", "in", ["draft", "sent"]]],
                metricLabel: "Quotes Pending",
                headerClass: "tt_bg_orange",
                iconClass: "fa fa-line-chart",
                watermarkClass: "fa fa-handshake-o",
                badge: "Active",
                badgeClass: "tt_badge_orange",
            },
            {
                key: "purchases",
                title: "Purchases",
                description: "Requests, approvals, and vendor orders.",
                model: "purchase.order",
                domain: [["state", "in", ["draft", "sent", "to approve"]]],
                metricLabel: "Orders Waiting",
                headerClass: "tt_bg_green",
                iconClass: "fa fa-shopping-cart",
                watermarkClass: "fa fa-truck",
                badge: "Queued",
                badgeClass: "tt_badge_green",
            },
            {
                key: "inventory",
                title: "Inventory",
                description: "Transfers, replenishment, and stock health.",
                model: "stock.picking",
                domain: [["state", "in", ["confirmed", "assigned", "waiting"]]],
                metricLabel: "Transfers",
                headerClass: "tt_bg_purple",
                iconClass: "fa fa-dropbox",
                watermarkClass: "fa fa-cubes",
                badge: "In Progress",
                badgeClass: "tt_badge_gray",
            },
            {
                key: "contacts",
                title: "Contacts",
                description: "Customer and vendor directory snapshots.",
                model: "res.partner",
                domain: [["active", "=", true]],
                metricLabel: "Total Contacts",
                headerClass: "tt_bg_blue",
                iconClass: "fa fa-address-book",
                watermarkClass: "fa fa-users",
                badge: "Active",
                badgeClass: "tt_badge_blue",
            },
        ];

        const moduleCards = [];
        for (const def of cardDefs) {
            if (!hasModel(def.model)) {
                continue;
            }
            const count = await getCount(def.model, def.domain);
            moduleCards.push({
                ...def,
                metric: `${formatCount(count)} ${def.metricLabel}`,
            });
            if (moduleCards.length >= 4) {
                break;
            }
        }

        this.state.metrics = metrics;
        this.state.moduleCards = moduleCards;
        this.state.focusItems = focusItems;
        this.state.loading = false;
    }
}

registry.category("actions").add("template_theme.home", TemplateThemeHome);
