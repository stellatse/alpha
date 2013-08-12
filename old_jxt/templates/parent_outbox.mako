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
<h2>发件箱</h2>
% if mails:
		<table id="tickets" >
			<thead>
				<tr>
					<th>收件人</th>
					<th>标题</th>
					<th>操作</th>
					
				</tr>
			</thead>
			<tbody>
			
			% for ticket in mails:
				<tr>
					<td>${ticket['mail'].m_to}</td>
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