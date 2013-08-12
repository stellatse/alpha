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
<h2>发件箱</h2>
% if mails:
		<table id="tickets" >
			<thead>
				<tr>
					<th>发件人</th>
					<th>标题</th>
					<th>操作</th>
					
				</tr>
			</thead>
			<tbody>
			
			% for ticket in mails:
				<tr>
					<td>${ticket['mail'].m_from}</td>
					<td><a href="/mail/${ticket['mail'].id}">${ticket['mail'].title}</a></td>
					<td><a href="/mail/${ticket['mail'].id}">查看</a></td>
				</tr>
			% endfor
					
					
			</tbody>
		</table>
% else:
<p>没有邮件</p>
% endif
</div>

</div>