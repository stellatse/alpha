<%inherit file="base.html"/>

<%include file="config_base.html"/>	


<div class="main">
<div class="welcome">管理家长和老师信息请点击“帐户管理”</div>
<div id='to-do'>
<h2>学生列表</h2>

		<table id="tickets" >
			<thead>
				<tr>
					<th style="width:50px;">学号</th>
					<th>姓名</th>
					<th>年级</th>
					<th>其他信息</th>
					<th>关联家长</th>
					
					
				</tr>
			</thead>
			<tbody>
			% if result:
			% for i in result:
				<tr>
					<td><a href="">${i['id']}</a></td>
					<td>${i['name']}</td>
					<td>${i['grade']}</td>
					<td>${i['other']}</td>
					<td>
					% if i['parent']:
						${i['parent'].name}
					% else:
					 没有关联家长，<a href="/config/user">请添加</a>
					% endif
					</td>
					
					
				</tr>
			% endfor
					
			%endif
			</tbody>
		</table>
</div>


<%include file="foot.html"/>

</div>

