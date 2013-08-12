<%inherit file="base.html"/>
<%include file="parent_base.html"/>


<div class="main">
<div class="configuration">
	<h2>学生：${student.name}</h2>
	<div class="add">
		<div id='to-do'>
	
	<h2>作业情况：</h2>
	% if homeworks:
			<table id="user" >
				<thead>
					<tr>
						<th>科目</th>
						<th>作业内容</th>
						<th>状态</th>
						
					</tr>
				</thead>
				<tbody>
				
				% for h in homeworks:
					<tr>
						<td>${h.subject.name}</td>
						<td>${h.content}</td>
						<td>
						% if h.status == 1:
							未完成
						% else:
						    已完成
						% endif
						</td>
						
					</tr>
				% endfor
						
						
				</tbody>
			</table>
		% endif
	</div>
	</div>	
	<div class='search'>
		
	<div id='to-do'>
	
	<h2>成绩情况：</h2>
	% if scores:
			<table id="user" >
				<thead>
					<tr>
						<th>科目</th>
						<th>得分</th>
						<th>详细信息</th>
						
					</tr>
				</thead>
				<tbody>
				
				% for s in scores:
					<tr>
						<td>${s.subject.name}</td>
						<td>${s.score}</td>
						<td>
						${s.description}
						</td>
						
					</tr>
				% endfor
						
						
				</tbody>
			</table>
		% endif
	</div>

</div>