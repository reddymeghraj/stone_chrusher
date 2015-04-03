cur_frm.cscript.rate=function(doc,cdt,cdn){
	var rate=doc.rate*doc.footing;
	cur_frm.set_value("amount",rate);
}
cur_frm.cscript.diesel_rate=function(doc,cdt,cdn)
{
	var amount=doc.diesel*doc.diesel_rate;
	cur_frm.set_value("diesel_amount",amount);
}
cur_frm.cscript.paid_amount=function(doc,cdt,cdn)
{
	var ramount=(doc.amount-doc.diesel_amount)-doc.paid_amount;
	cur_frm.set_value("remaining_amount",ramount);
}