cur_frm.cscript.rate=function(doc,cdt,cdn){
	var amount=doc.brass*doc.rate;
	cur_frm.set_value("amount",amount);
}
cur_frm.cscript.vat_amount=function(doc,cdt,cdn)
{
	var ramount=(parseFloat(doc.amount)+parseFloat(doc.vat_amount));
	cur_frm.set_value("amount_received",ramount);
	frappe.call({
		method:"stone_crusher.stone_crusher.doctype.credit_sale.credit_sale.get_credit_amount",
		args:{client:doc.client},
		callback:function(r)
		{
			var cramount=r.message-ramount;
			cur_frm.set_value("credit_amount",cramount);
		}
	})
}