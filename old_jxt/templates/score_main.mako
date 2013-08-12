<%inherit file="base.html"/>
<%include file="teacher_base.html"/>

<div class="main">

	<div class="welcome">			
		<ul>
		<li class="p1"><a href="/score/add">添加成绩</a></li>
		<li class="p2"><a href="/score/view">查看历史成绩</a></li>
		<ul>
	</div>
	<div id='to-do'>
		<h2>学生列表</h2>
			<table id="tickets" >
				<thead>
					<tr>
						<th style="width:50px;">学号</th>
						<th>姓名</th>
						<th>年级</th>
						<th>其他信息</th>
						
						
					</tr>
				</thead>
				<tbody>
				
				% for ticket in students:
					<tr>
						<td><a href="">${ticket.id}</a></td>
						<td>${ticket.name}</td>
						<td>${ticket.grade}</td>
						<td>${ticket.other_info}</td>
						
						
					</tr>
				% endfor
						
						
				</tbody>
			</table>
	</div>



</div>