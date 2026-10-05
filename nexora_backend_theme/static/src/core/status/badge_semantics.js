/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { BadgeField } from "@web/views/fields/badge/badge_field";

const STATE_SEMANTICS = {
    cyan: new Set(["draft", "confirmed", "assigned", "progress", "open", "new", "normal"]),
    magenta: new Set(["sent", "to approve", "to_approve", "pending", "review", "in_process"]),
    yellow: new Set(["waiting", "to_close", "partially_available", "expected", "attention"]),
    red: new Set(["cancel", "cancelled", "canceled", "reject", "rejected", "blocked", "overdue", "late", "unavailable", "absent"]),
    success: new Set(["done", "purchase", "sale", "posted", "paid", "approved", "resolved", "close", "available", "present"]),
};

function getStatusSemantic(value) {
    const normalizedValue = String(value || "").toLowerCase();
    return Object.entries(STATE_SEMANTICS).find(([, values]) => values.has(normalizedValue))?.[0];
}

patch(BadgeField.prototype, {
    get classFromDecoration() {
        const semantic = getStatusSemantic(this.props.record.data[this.props.name]);
        return semantic ? `nexora-status-${semantic}` : super.classFromDecoration;
    },
});
