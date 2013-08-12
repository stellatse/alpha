<%inherit file="base.html"/>
<%include file="teacher_base.html"/>
<script language="javascript">
function update_to_finish(m){
	$.post('update',
		{'id':m},
		function(){
            window.location.href ="/homework/update";
        });

};
</script>
<div class="main">

	<div class="welcome">			
		<ul>
		<li class="p1"><a href="/homework/add">添加作业</a></li>
		<li class="p2"><a href="/homework/update">作业状态更新</a></li>
		
		<ul>
	</div>
	<div id='to-do'>
		<h2>作业列表</h2>
		% if homeworks:
			<table id="tickets" >
				<thead>
					<tr>
						<th style="width:50px;">科目</th>
						<th>内容</th>
						<th>学号</th>
						<th>学生姓名</th>
						<th>状态</th>
						<th>操作</th>
						
						
					</tr>
				</thead>
				<tbody>
				
				% for i in homeworks:
					<tr>
						<td><a href="">${i['subject']}</a></td>
						<td>${i['content']}</td>
						<td>${i['sid']}</td>
						<td>${i['sname']}</td>
						<td>${i['status']}</td>
						<td>
						% if i['status'] == 'Finished':
							已完成
						%else:
						<a href="javascript:void(0);" onclick="update_to_finish(${i['id']});">确认完成</a>
						%endif
						</td>
						
						
					</tr>
				% endfor
						
						
				</tbody>
			</table>
			%endif
	</div>



</div>