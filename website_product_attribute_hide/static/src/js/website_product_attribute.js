odoo.define('website_product_attribute_hide.website_product_attribute', function (require) {
    'use strict';
    
    if (!$('#o_shop_collapse_attribute').length) {
        return $.Deferred().reject("DOM doesn't contain '#o_shop_collapse_category'");
    }
    $('#o_shop_collapse_attribute').on('click', '.o_shop_collapse_attribute_name', function() {
        $(this).parents('div:first').find('i:first').click();
    });
    $('#o_shop_collapse_attribute').on('click', '.fa-chevron-right', function() {
        $(this).parents('li').find('ul:first').show();
        $(this).toggleClass('fa-chevron-down fa-chevron-right');
    });
    $('#o_shop_collapse_attribute').on('click', '.fa-chevron-down', function() {
        $(this).parents('li').find('ul:first').hide();
        $(this).toggleClass('fa-chevron-down fa-chevron-right');
    });    
});