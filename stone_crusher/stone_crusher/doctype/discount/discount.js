cur_frm.cscript.payment_type=function(doc,cdt,cdn)
{
	frappe.call({
		method:"stone_crusher.stone_crusher.doctype.discount.discount.get_amount",
		args:{client:doc.client},
		callback:function(r)
		{
			var remaining=r.message;
			if(remaining>0)
			{
				alert("There is advance amount from this client");
			}
			if(remaining==0)
			{
				alert("This customer Is Nill");
			}
			else
			{
				cur_frm.set_value("credit_amount",r.message);
			}
		}
	});
	var d=doc.payment_type;
	if(d=='Cash')
	{
		cur_frm.toggle_enable('cheque_no', false);
	}
	else
	{
		cur_frm.toggle_enable('cheque_no', true);
	}
}
cur_frm.cscript.paid_amount=function(doc,cdt,cdn)
{

	var ramount=doc.credit_amount-(parseFloat(doc.discount_amount)+parseFloat(doc.paid_amount));
	cur_frm.set_value("remaining_amount",ramount);
}