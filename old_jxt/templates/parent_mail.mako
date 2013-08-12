<%inherit file="base.html"/>
<%include file="parent_base.html"/>


<div class="main">
	<div class="welcome">			
		<ul>
		<li class="p1"><a href="/parent/inbox">收件箱</a></li>
		<li class="p2"><a href="/parent/outbox">发件箱</a></li>
		<ul>
	</div>
<div class="info_baseinfo">
	<a>发送邮件：</a>
	
	<form action= "${request.route_url('parent_mail', tid=m_to)}" method = "POST">

			<label>收件人:</label>
			<input name="m_to_email" type="text" value="${teacher.name}" />
			<input name="m_to" type="hidden" value="${m_to}" />
			<input name="m_from" type="hidden" value="${m_from}" />
			<label for="name">邮件标题:</label>
			<input name="title" type="text" placeholder="标题"/>
			<label>邮件正文</label>
			<textarea name="content" rows="10" cols="25"></textarea>
			
			<input type="submit"  name="form.submitted" value="发送"/>
			%if message:
			<p style="color:red;">${message}</p>
			% endif
		</form>
	<br/>
	<a href=""></a>
	
	</div>	

</div>