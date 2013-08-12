<%inherit file="base.html"/>
<%include file="teacher_base.html"/>

<div class="main">

	<div class="welcome">			
		<ul>
		<li class="p1"><a href="/homework/add">添加作业</a></li>
		<li class="p2"><a href="/homework/update">作业状态更新</a></li>
		<ul>
	</div>
	<div id='to-do'>
	<p>${message}</p>
	<form action="${request.route_url('homework_add')}" method = "post">
		<h2>添加作业</h2>
		<label>选择科目</label>
			<select name="subject">
			% for s in subjects:
			<option value="${s.id}">${s.name}</option>
			% endfor
			</select>
		<label>作业内容</label>
		<input type="text" name="content"/>
			<input type="submit" name="chg.submitted" value="提交"/>
	</form>
	</div>



</div>