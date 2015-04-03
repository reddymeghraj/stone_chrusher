cur_frm.cscript.rate=function(doc,cdt,cdn)
{
	var amount=doc.quantity*doc.rate;
	cur_frm.set_value("amount",amount);
}
cur_frm.cscript.paid_amount=function(doc,cdt,cdn)
{
	var ramount=(parseFloat(doc.amount)+parseFloat(doc.vat_amount))-doc.paid_amount;
	cur_frm.set_value("reamining_amount",ramount);
}