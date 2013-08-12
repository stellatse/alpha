<%inherit file="base.html"/>
<%include file="parent_base.html"/>


<div class="main">

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
<p>没有未读邮件</p>
% endif
</div>


</div>