/*cur_frm.cscript.paid_amount=function(doc,cdt,cdn)
{
	if(!doc.advance)
	{
		var ramount=doc.salary-doc.paid_amount;
		cur_frm.set_value("remaining_amount",ramount);
	}
	else
	{
		var d=doc.advance;
		var len=d.length;
		var total=0;
		for(i=0;i<len;i++)
		{
			total=parseFloat(total)+parseFloat(d[i].amount);
		}
		var ramount=doc.salary-(parseFloat(total)+parseFloat(doc.paid_amount));
		cur_frm.set_value("remaining_amount",ramount);
	}
}*/
cur_frm.cscript.payment_date=function(doc,cdt,cdn)
{
	var d=doc.salary_month;
	var arr=d.split("-");
	var month=arr[1];
	var year=arr[0];
	var salary=new Date(d);
	var last_day  = new Date(salary.getFullYear(), salary.getMonth()+1, 0);
	var d1=doc.payment_date;
	var sdate=new Date(d1);
	if(last_day>sdate)
	{
		cur_frm.set_value("payment_date",'');
		alert("Salary Sleep Can not be generated");
	}	
}