cur_frm.cscript.paid_amount=function (doc,cdt,cdn) {
	var ramount=doc.labour_charge-doc.paid_amount;
	cur_frm.set_value("remaining_amount",ramount);
}