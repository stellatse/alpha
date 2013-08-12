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
	<form action="${request.route_url('score_view')}" method = "post">
	<label>选择科目</label>
			<select name="subject">
			% for s in subjects:
			<option value="${s.id}">${s.name}</option>
			% endfor
			</select>
			<input type="submit"  name="form.submitted" value="查看"/>
	</form>
	% if result:
		<h2>成绩查询结果</h2>
			<table id="tickets" >
				<thead>
					<tr>
						<th style="width:50px;">学号</th>
						<th>姓名</th>
						<th>成绩</th>
						<th>科目</th>
						
						
					</tr>
				</thead>
				<tbody>
				
				% for i in result:
					<tr>
						<td><a href="">${i['sid']}</a></td>
						<td>${i['sname']}</td>
						<td>${i['score']}</td>
						<td>${i['subject']}</td>
						
						
					</tr>
				% endfor
						
						
				</tbody>
			</table>
	%elif result == []:
	  <h2>还未登记成绩</h2>

	 %endif
	</div>



</div>