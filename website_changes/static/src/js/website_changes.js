odoo.define('website_changes.website_changes', function (require) {
    "use strict";

    var core = require('web.core');
	var QWeb = core.qweb;

	QWeb.add_template('/website_changes/static/src/xml/website_sale_recently_viewed_extend.xml');
});