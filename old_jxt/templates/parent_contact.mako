<%inherit file="base.html"/>
<%include file="parent_base.html"/>


<div class="main">
<div class="welcome">			
		<ul>
		<li class="p1"><a href="/parent/inbox">收件箱</a></li>
		<li class="p2"><a href="/parent/outbox">发件箱</a></li>
		<ul>
	</div>
<div id='to-do'>
<h2>未读邮件(${count})</h2>
% if mails:
		<table id="tickets" >
			<thead>
				<tr>
					<th>发件人</th>
					<th>标题</th>
					<th>发送时间</th>
					<th>状态</th>
					<th>操作</th>
					
				</tr>
			</thead>
			<tbody>
			
			% for ticket in mails:
				<tr>
					<td>${ticket.m_from}</td>
					<td><a href="/teacher/mail/{$ticket.id}">${ticket.title}</a></td>
					<td>${ticket.send_time}</td>
					<td>${ticket.status}</td>
					<td><a href="/teacher/mail/${ticket.id}">查看</a></td>
				</tr>
			% endfor
					
					
			</tbody>
		</table>
% else:
<p>没有邮件</p>
% endif
</div>
<div id='to-do'>
<h2>老师列表</h2>
% if teachers:
		<table id="tickets" >
			<thead>
				<tr>
					<th>ID</th>
					<th>姓名</th>
					<th>操作</th>
					
				</tr>
			</thead>
			<tbody>
			
			% for j in teachers:
				<tr>
					<td>${j.id}</td>
					<td>${j.name}</td>
					<td><a href="/parent/mail/${j.id}">发送信件</a></td>
				</tr>
			% endfor
					
					
			</tbody>
		</table>
% else:
<p>没有可联系老师</p>
% endif
</div>

</div>