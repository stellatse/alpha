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
	<p>${message}</p>
	<form action="${request.route_url('score_add')}" method = "post">
		<h2>登记成绩</h2>
		<label>选择科目</label>
			<select name="subject">
			% for s in subjects:
			<option value="${s.id}">${s.name}</option>
			% endfor
			</select>
			<table id="tickets" >
				<thead>
					<tr>
						<th style="width:50px;">学号</th>
						<th>姓名</th>
						<th>成绩</th>
						
						
					</tr>
				</thead>
				<tbody>
				
				% for ticket in students:
					<tr>
						<td>${ticket.id}</td>
						<td>${ticket.name}</td>
						<td><input type="text" name="${ticket.id}"/></td>
						
						
						
					</tr>
				% endfor
						
						
				</tbody>
			</table>
			<input type="submit" name="chg.submitted" value="提交"/>
	</form>
	</div>



</div>