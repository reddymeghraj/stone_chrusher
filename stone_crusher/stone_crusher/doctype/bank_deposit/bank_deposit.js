cur_frm.cscript.payment_type=function(doc,cdt,cdn)
{
	var payment_type=doc.payment_type;
	if(payment_type=='Cash')
	{
		cur_frm.toggle_enable("cheque_no", false);
	}
	else
	{
		cur_frm.toggle_enable("cheque_no", true);
	}
}