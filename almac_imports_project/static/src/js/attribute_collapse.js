odoo.define('almac_imports_project.website_sale_attributs', function (require) {
    "use strict";

    var base = require('web_editor.base');


    function set_stock_avability_qty(source_form) {
        var $form = source_form;
        var values = [];
        var product_id = false;
        var variant_ids = $form.find('ul[data-attribute_value_ids]').data('attribute_value_ids');
        var qty_variant_ids =  eval($('form[data-qty_attribute_value_ids]').attr('data-qty_attribute_value_ids'));
        var qty_container = $form.find('#qty_container');
        var fr_out_of_stock = $form.find('#fr_out_of_stock');
        var on_hand_qty = 0.0

        $form.find('input.js_variant_change:checked, select.js_variant_change').each(function () {
            values.push(+$(this).val());
        });

        for (var k in variant_ids) {
            if (!_.isEmpty(values) && !_.isEmpty(variant_ids[k][1]) &&_.isEmpty(_.difference(variant_ids[k][1], values))) {
                product_id = variant_ids[k][0];
                break;
            }
        }
        if(product_id){
            for (var qvi in qty_variant_ids){
                var split_data = qty_variant_ids[qvi].split('-')
                if (product_id == parseInt(split_data[0])){
                    on_hand_qty = parseFloat(split_data[1]);
                    break;
                }
            }
        }else if (qty_variant_ids.length == 1){
            var split_data = qty_variant_ids[0].split('-');
            on_hand_qty = parseFloat(split_data[1]);
            product_id = split_data[0];
        }
        if (on_hand_qty > 0.0) {
            fr_out_of_stock.addClass('hidden');
            qty_container.empty();
            qty_container.html("<p class='text-muted'><span>"+ parseInt(on_hand_qty) +" In Stock </span></p>");
        } else if(on_hand_qty == 0.0) {
            if (base.get_context().lang == 'fr_CA') {
                qty_container.empty();
                fr_out_of_stock.removeClass('hidden');
            }
            else {
                fr_out_of_stock.addClass('hidden');
                qty_container.html("<p class='text-muted'><span> Out of Stock </span></p>");
            }
        }
    }
    $('input[type="radio"].js_variant_change, select.js_variant_change').on('click change', function(event) {
        var $form = $(this).closest('form');
        set_stock_avability_qty($form);
    });




    $('form.js_add_cart_variants').on('click', '.js_variant_change', function(e) {
        var product_form =  $('form.js_add_cart_variants');
        var current_variant = product_form.find("input[name='product_id']").val();
        var offer_div = product_form.find('.product_offers');
        $.ajax({
            url: "/website/action/get_variant_offers",
            type: "GET",
            data: {
                'product_id': current_variant
                }
        }).then(function(result){
            if (result != '' || result != '<p><br></p><p><br></p>') {
                offer_div.empty();
                offer_div.html(result);
            } else {
                offer_div.empty();
            }
        });
    });
    $(document).ready(function () {

        $('#o_shop_collapse_attribute').on('click', '.fa-chevron-right',function(){
            $(this).parents('li').find('ul:first').show('normal');
            $(this).removeClass('fa-chevron-right');
            $(this).addClass('fa-chevron-down');
        });

        $('#o_shop_collapse_attribute').on('click', '.fa-chevron-down',function(){
            $(this).parents('li').find('ul:first').hide('normal');
            $(this).removeClass('fa-chevron-down');
            $(this).addClass('fa-chevron-right');
        });

        $('.js_variant_change').trigger('click');
        $('input[type="radio"].js_variant_change, select.js_variant_change').trigger('change');
        var source_form = $('form.js_add_cart_variants');
        if (source_form.length > 0.0){
            set_stock_avability_qty(source_form);
        }
    });
});
