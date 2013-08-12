<%inherit file="base.html"/>
<%include file="teacher_base.html"/>


<div class="main">
<div class="welcome">			
		<ul>
		<li class="p1"><a href="/teacher/inbox">收件箱</a></li>
		<li class="p2"><a href="/teacher/outbox">发件箱</a></li>
		<ul>
	</div>
<div id='to-do'>
<h2>未读邮件(${count})</h2>
% if unreadmail:
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
			
			% for ticket in unreadmail:
				<tr>
					<td>${ticket.m_from}</td>
					<td><a href="/mail/{$ticket.id}">${ticket.title}</a></td>
					<td>${ticket.send_time}</td>
					<td>${ticket.status}</td>
					<td><a href="/mail/${ticket.id}">查看</a></td>
				</tr>
			% endfor
					
					
			</tbody>
		</table>
% else:
<p>没有邮件</p>
% endif
</div>
<div id='to-do'>
<h2>家长列表</h2>
% if parents:
		<table id="tickets" >
			<thead>
				<tr>
					<th>姓名</th>
					<th>学生</th>
					<th>操作</th>
					
				</tr>
			</thead>
			<tbody>
			
			% for j in parents:
				<tr>
					<td>${j['parent'].name}</td>
					<td>
					% if j['student']:
					${j['student'].name}
					% else:
					没有关联学生
					% endif
					</td>
					<td><a href="/teacher/mail/${j['parent'].id}">发送信件</a></td>
				</tr>
			% endfor
					
					
			</tbody>
		</table>
% else:
<p>没有可联系老师</p>
% endif
</div>

</div>