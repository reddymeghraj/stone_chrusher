cur_frm.cscript.diesel_rate=function(doc,cdt,cdn)
{
	var damount=doc.diesel*doc.diesel_rate;
	cur_frm.set_value("diesel_amount",damount);
}

cur_frm.cscript.payment_type=function(doc,cdt,cdn)
{
	var d=doc.trip_details;
	var len=d.length;
	var total=0;
	for(i=0;i<len;i++)
	{
		total=parseFloat(total)+parseFloat(d[i].transport_rent);
	}
	cur_frm.set_value("total_amount",total);
}
cur_frm.cscript.paid_amount=function(doc,cdt,cdn)
{
	var ramount=doc.total_amount-doc.paid_amount-doc.diesel_amount;
	cur_frm.set_value("remaining_amount",ramount);
}