// 打开层
 function openLayer(o,w,h){
	 var w = w || 243;
	 var h = h || 268;
	 $.openLayer({
		width:w+"px",
		height:h+"px",
		target:o, //对象
		type:'_id' //选择类型，如果是外部加载则类型为 ajax
	});
  };
//关闭层
function closeLayer(){
	$.closeLayer();	
};

//Pop-up
function openNews (m,o){
	openLayer('openNews',243,268);
	$(".newsList").hide();
	$(".newsList"+0).show();
}
//Pop-up
function DailyEvents (m,o){
	openLayer('DailyEvents',707,608);
	$(".newsList").hide();
	$(".newsList"+0).show();
}
//Pop-up
function search_window(o){
  // if (!($(":checkbox[name='portfolio']").attr("checked"))) {
  // 	alert("Please select a portfolio");
  // 	// $(":checkbox[name='portfolio']").focus();
  // 	return false;
  // };
if($("input[name='start_date']").val()==""){
	alert("Please select a start date");
	// $("input[name='start_date']").focus();
	return false;
};
if($("input[name='end_date']").val()==""){
	alert("Please select an end date");
	return false;
};

document.getElementById('leftform').submit();

};
function book (m,o){


	openLayer('book',385,280);
	var start_date = $("#start_date"+o).text();
	var end_date = $("#end_date"+o).text();
	var every = $("#every"+o).text();
	var periods = $("#periods"+o).text();
	var portfolio_id = $("#portfolio_id").text();
	var portfolio = $("#select_portfolio").text();
	var dow = $("#dow"+o).text();
	var period_num = $("#period_num"+o).text();
	var windows = $("#window"+o).text();
	var exp = $("#exp_values").text()
	$("#confirm_portfolio").html(portfolio);
	$("#portfolio_id").html(portfolio_id);
	$("#start_end").html(start_date + "<br/>" +end_date);
	$("#start_date").html(start_date);
	$("#end_date").html(end_date);
	$("#every").html(every);
	$("#time_period").html(periods);
	$("#dow").html(dow);
	$("#period_num").html(period_num);
	$("#windows").html(windows);
	$("#exp_value").html(exp);
	$(".newsList").hide();
	$(".newsList"+0).show();
};
function book_confirm(m){
	var portfolio = $("#portfolio_id").text();
	var start_date = $("#start_date").text();
	var end_date = $("#end_date").text();
	var period_num = $("#period_num").text();
	var windows = $("#windows").text();
	var dow = $("#dow").text();
	var exp = $("#exp_value").text();
	$.post('book_confirm',
		{'portfolio':portfolio, 'dow':dow, 'start_date':start_date, 'end_date':end_date, 'window_num':period_num, 'windows':windows, 'exception': exp},
		function(){
            window.location.href ="/event/all";
        });

};
function delete_confirm(m){
	var event_id = $("#e_id_delete").text();
	$.post('delete_event_confirm', {'eventid':event_id},
		function(){
			window.location.href = "/event/all";
		});
};
function DeleteEvent(m,o){
	openLayer('book',243,268);
	// var e_id_delete = o
	$("#e_id_delete").html(o);
	$(".newsList").hide();
	$(".newsList"+0).show();
	// $.post('delete_event',{id:o});
};

function ViewEdit(m,o){
	$.post('get_window_detail',{id:o},function(data){
		var obj = eval('(' + data + ')');
	// alert(queryString);
	// openLayer('Customized',707,608);
	$(".newsList").hide();
	$(".newsList"+1).show();
	$('#changed_event_id').html(o);
    // alert(obj[1].date);
    window.change=[];
    var string = '<table width="100%" border="0" cellspacing="0" id="datelist1" cellpadding="0" class="Pop-upDeta bookPop-up cl datelists">';
		j=1;
		for(i=1;i<=obj.length;i++){
		  if((i-1)%10==0&&i>2){
			  j=j+1;
			  string = string + '</table><table width="100%" border="0" cellspacing="0" id="datelist'+j+'" cellpadding="0" class="Pop-upDeta bookPop-up cl datelists" style="display:none">';
		  }
			news = i;
			// datestart=obj[i-1].date.valueOf();
			// newdate=datestart + (i-1) * 24 * 60 * 60 * 1000;
			// newdates = new Date(obj[i-1].date);
			// var newdate = newdates.getFullYear()+"-"+(newdates.getMonth()+1)+"-"+(newdates.getDate());
		  var html='<tr><td width="99" align="center" valign="middle" class="dates">'+obj[i-1].date+'</td><td width="507" align="center" valign="middle"><div class="PullStrip">';
		  html = html+'<div class="tslider"><input name="sliderd'+news+'_1" id="sliderd'+news+'_1" type="hidden" value="'+parseFloat(obj[i-1].time1_1)*60+';'+parseFloat(obj[i-1].time1_2)*60+'" /></div><div class="tslider"><input name="sliderd'+news+'_2" id="sliderd'+news+'_2" type="hidden" value="'+parseFloat(obj[i-1].time2_1)*60+';'+parseFloat(obj[i-1].time2_2)*60+'" /></div><div class="tslider"><input name="sliderd'+news+'_3" id="sliderd'+news+'_3" type="hidden" value="'+parseFloat(obj[i-1].time3_1)*60+';'+parseFloat(obj[i-1].time3_2)*60+'" /></div>';
		  html = html+'</div></td><td width="66" align="center" valign="middle"><img onclick="delrow(this)" src="/static/images/book_iconTc_18.gif" /></td></tr>';
		  string = string+html;
		}
		string = string+'</table>';
		$('#pages').val(j);
		$('#datalistdiv').html('1');
		$('#datalistdiv').html(string);
		for(i=1;i<=obj.length;i++){
			news = i;
			jQuery("#sliderd"+news+"_1").sslider({ from: 0, to: 480, step: 15, dimension: '', limits: false, calculate: function( value ){
			var hours = Math.floor( value / 60 );
			var mins = ( value - hours*60 );
			return (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins );
		  }, callback:function(value){
		  		time=value.split(";");
		  		var change_date=$(this)[0].domNode[0].parentNode.parentNode.parentNode.parentNode.firstChild.textContent;
		  		for (i=0; i<time.length;i++){
			  		var hours = Math.floor( time[i] / 60);
			  		var mins = ( time[i] - hours*60);
			  		time[i]= (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins) ;
		  		}
		  		
		  		window.change.push({'type':'update', 'date':change_date, 'time':time});
		  }})
	
		  jQuery("#sliderd"+news+"_2").sslider({ from: 480, to: 960,skin: "blue", step: 15, dimension: '', limits: false, calculate: function( value ){
			var hours = Math.floor( value / 60 );
			var mins = ( value - hours*60 );
			return (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins );
		  }, callback:function(value){
		  		time=value.split(";");
		  		var change_date=$(this)[0].domNode[0].parentNode.parentNode.parentNode.parentNode.firstChild.textContent;
		  		for (i=0; i<time.length;i++){
			  		var hours = Math.floor( time[i] / 60);
			  		var mins = ( time[i] - hours*60);
			  		time[i]= (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins) ;
		  		}
		  		
		  		window.change.push({'type':'update', 'date':change_date, 'time':time});
		  }})
	
		  jQuery("#sliderd"+news+"_3").sslider({ from: 960, to: 1440,skin: "plastic", step: 15, dimension: '', limits: false, calculate: function( value ){
			var hours = Math.floor( value / 60 );
			var mins = ( value - hours*60 );
			return (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins );
		  }, callback:function(value){
		  		time=value.split(";");
		  		var change_date=$(this)[0].domNode[0].parentNode.parentNode.parentNode.parentNode.firstChild.textContent;
		  		for (i=0; i<time.length;i++){
			  		var hours = Math.floor( time[i] / 60);
			  		var mins = ( time[i] - hours*60);
			  		time[i]= (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins) ;
		  		}
		  		
		  		window.change.push({'type':'update', 'date':change_date, 'time':time});
		  }})
		}
		str = '';
		for(k=1;k<=j;k++){
			start = (k-1)*10+1;
			end = k*10;
			if(end>obj.length){
				end = obj.length;
			}
			str = str+'<span class="Page"';
			if(k>1){
				str = str+' style="display:none;"';
			}
			str = str+'>'+start+' - '+end+' of '+obj.length+'</span>';
		}
		$('#pagenums').html('1');
		$('#pagenums').html(str);
		$('#searchs').val(1);
		oldhtml = $('#dataform').html();
	})
	openLayer('Customized',707,608);
	$(".newsList").hide();
	$(".newsList"+o).show();
};

function confirm_event_change(){
	
	event_id=$('#changed_event_id').html();

	if (window.change.length != 0){
		exp = JSON.stringify(window.change);
		$.post('change_event_confirm', {'eventid':event_id, 'exp':exp},
		function(){
			window.location.href = "/event/all";
		});
	} else {
		alert('No change detective')
		return false;
	}
	
};

function openException(m, o){
	openLayer('exption',707,608);
	// var e_id_delete = o
	value=JSON.stringify(o)
	$(".expceptions").html('Changed:'+value);
	$(".newsList").hide();
	$(".newsList"+0).show();
}

function confirm_exp(){
	$("#exp").val('');
	exp = JSON.stringify(window.change);
	$("#exp").val(exp);
	closeLayer();

}
//Pop-up
function Customized (m,o){

if($("input[name='start_date']").val()==""){
	alert("Please select a start date");
	return false;
};
if($("input[name='end_date']").val()==""){
	alert("Please select an end date");
	return false;
};

window.change=[];
var queryString = $('#leftform').formSerialize();
alert(queryString)
$.post('get_customize_initial_data', queryString + '&page=1',function(data){
	// var obj = JSON.parse(data);
	var obj = eval('(' + data + ')');
	// var obj = result.result;
	// alert(obj);
	// alert(queryString);
	openLayer('Customized',707,608);
	$(".newsList").hide();
	$(".newsList"+o).show();
    // alert(obj[1].date);
    var string = '<table width="100%" border="0" cellspacing="0" id="datelist1" cellpadding="0" class="Pop-upDeta bookPop-up cl datelists">';
		j=1;
		for(i=1;i<=obj.length;i++){
		  if((i-1)%10==0&&i>2){
			  j=j+1;
			  string = string + '</table><table width="100%" border="0" cellspacing="0" id="datelist'+j+'" cellpadding="0" class="Pop-upDeta bookPop-up cl datelists" style="display:none">';
		  }
			news = i;
			// datestart=obj[i-1].date.valueOf();
			// newdate=datestart + (i-1) * 24 * 60 * 60 * 1000;
			// newdates = new Date(obj[i-1].date);
			// var newdate = newdates.getFullYear()+"-"+(newdates.getMonth()+1)+"-"+(newdates.getDate());
		  var html='<tr><td width="99" align="center" valign="middle" class="dates">'+obj[i-1].date+'</td><td width="507" align="center" valign="middle"><div class="PullStrip">';
		  html = html+'<div class="tslider"><input name="sliderd'+news+'_1" id="sliderd'+news+'_1" type="hidden" value="'+parseFloat(obj[i-1].time1_1)*60+';'+parseFloat(obj[i-1].time1_2)*60+'" /></div><div class="tslider"><input name="sliderd'+news+'_2" id="sliderd'+news+'_2" type="hidden" value="'+parseFloat(obj[i-1].time2_1)*60+';'+parseFloat(obj[i-1].time2_2)*60+'" /></div><div class="tslider"><input name="sliderd'+news+'_3" id="sliderd'+news+'_3" type="hidden" value="'+parseFloat(obj[i-1].time3_1)*60+';'+parseFloat(obj[i-1].time3_2)*60+'" /></div>';
		  html = html+'</div></td><td width="66" align="center" valign="middle"><img onclick="delrow(this)" src="/static/images/book_iconTc_18.gif" /></td></tr>';
		  string = string+html;
		}
		string = string+'</table>';
		$('#pages').val(j);
		$('#datalistdiv').html('1');
		$('#datalistdiv').html(string);
		for(i=1;i<=obj.length;i++){
			news = i;
			// alert(obj[i-1].date);
			jQuery("#sliderd"+news+"_1").sslider({ from: 0, to: 480, step: 15, dimension: '', limits: false, calculate: function( value ){
			var hours = Math.floor( value / 60 );
			var mins = ( value - hours*60 );
			return (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins );
		  }, callback:function(value){
		  		time=value.split(";");
		  		var change_date=$(this)[0].domNode[0].parentNode.parentNode.parentNode.parentNode.firstChild.textContent;
		  		for (i=0; i<time.length;i++){
			  		var hours = Math.floor( time[i] / 60);
			  		var mins = ( time[i] - hours*60);
			  		time[i]= (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins) ;
		  		}
		  		
		  		window.change.push({'type':'update', 'date':change_date, 'time':time});
		  }})
			
		  jQuery("#sliderd"+news+"_2").sslider({ from: 480, to: 960,skin: "blue", step: 15, date: obj[i-1].date,dimension: '', limits: false, calculate: function( value ){
			var hours = Math.floor( value / 60 );
			var mins = ( value - hours*60 );
			return (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins );
		  }, callback:function(value){
		  		time=value.split(";");
		  		var change_date=$(this)[0].domNode[0].parentNode.parentNode.parentNode.parentNode.firstChild.textContent;
		  		for (i=0; i<time.length;i++){
			  		var hours = Math.floor( time[i] / 60);
			  		var mins = ( time[i] - hours*60);
			  		time[i]= (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins) ;
		  		}
		  		
		  		window.change.push({'type':'update', 'date':change_date, 'time':time});
		  }}) 
	
		  jQuery("#sliderd"+news+"_3").sslider({ from: 960, to: 1440,skin: "plastic", step: 15, dimension: '', limits: false, calculate: function( value ){
			var hours = Math.floor( value / 60 );
			var mins = ( value - hours*60 );
			return (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins );
		  }, callback:function(value){
		  		time=value.split(";");
		  		var change_date=$(this)[0].domNode[0].parentNode.parentNode.parentNode.parentNode.firstChild.textContent;
		  		for (i=0; i<time.length;i++){
			  		var hours = Math.floor( time[i] / 60);
			  		var mins = ( time[i] - hours*60);
			  		time[i]= (hours < 10 ? "0"+hours : hours) + ":" + ( mins == 0 ? "00" : mins) ;
		  		}
		  		
		  		window.change.push({'type':'update', 'date':change_date, 'time':time});
		  }})
		}
		str = '';
		for(k=1;k<=j;k++){
			start = (k-1)*10+1;
			end = k*10;
			if(end>obj.length){
				end = obj.length;
			}
			str = str+'<span class="Page"';
			if(k>1){
				str = str+' style="display:none;"';
			}
			str = str+'>'+start+' - '+end+' of '+obj.length+'</span>';
		}
		$('#pagenums').html('1');
		$('#pagenums').html(str);
		$('#searchs').val(1);
		oldhtml = $('#dataform').html();
});

// alert(queryString);
	
}
//InviteNewUserSet
function InviteNewUserSet(m,o){
	openLayer('InviteNewUserSet',320,250);
	$(".newsList").hide();
	$(".newsList"+o).show();
}
function CreateNew(m,o){
	openLayer('CreateNew',320,140);
	$(".newsList").hide();
	$(".newsList"+o).show();
}

$(function(){
	$(".AddToMy").mousedown(function()
			{$(".AddToMyCon").css("display","block")
	});
	$('.BoxleftNavword li font').click(function(){
		var div = $(this).parent().parent();
		var cc = $(div).attr('class');
		if(cc=='hover'){
			$(div).attr('class','');
			$(div).next().css('display','none');
		}else{
			$(div).attr('class','hover');
			$(div).next().css('display','block');
		}
	});
	$('.BoxleftNavnoicon li font').click(function(){
		var div = $(this).parent();
		var cc = $(div).parent().attr('class');
		if(cc=='hover'){
			$(div).parent().attr('class','');
			$(div).next().css('display','none');
		}else{
			$(div).parent().attr('class','hover');
			$(div).next().css('display','block');
		}
	});
});

function format(t){
	if(t!=parseInt(t)){
		var dt = t-parseInt(t);
		t=parseInt(t)+dt*0.6;
	}
	t=t.toFixed(2);
	if(t<12){
		return t+"AM";
	}else{
		return t+"PM";
	}
}