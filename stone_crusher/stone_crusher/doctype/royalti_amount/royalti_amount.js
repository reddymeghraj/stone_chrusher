cur_frm.cscript.rate=function(doc,cdt,cdn){
	var amount=doc.brass*doc.rate;
	cur_frm.set_value("amount",amount);
}
cur_frm.cscript.amount_received=function(doc,cdt,cdn)
{
	var ramount=doc.amount-doc.amount_received;
	cur_frm.set_value("remaining_amount",ramount);
}