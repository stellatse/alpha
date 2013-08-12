<%inherit file="base.html"/>

<%include file="config_base.html"/>
<div class="main">

<div class="configuration">
	<h2>用户帐号管理中心</h2>
	<div class="add">
	<a>添加用户</a>
	
	<form action= "${request.route_url('add_user')}" method = "POST">
			<label>Email:</label>
			<input name="email" type="text" placeholder="Email" />
			<label for="name">姓名:</label>
			<input name="name" type="text" placeholder="姓名"/>
			<label>用户类型</label>
			<select name="configgp">
			<option value="1">管理员</option>
			<option value="2">老师</option>
			<option value="3">家长</option>
			</select>
			<label for="name">关联学号:(添加家长必填)</label>
			<input name="sid" type="text" placeholder="学号"/>
			<input type="submit"  name="form.submitted" value="添加"/>
			<p style="color:red;">${message}</p>
		</form>
	<br/>
	<a href=""></a>
	
	</div>	
	<div class='search'>
		<form action= "${request.route_url('search_user')}" method = "GET">
			<label>搜索现有用户:</label>
			<input name="search_user" type="text" placeholder="Searching Email.." style="width:300px" />
			<input type="submit"  name="form.submitted" value="搜索"/>
			<p style="color:red;">${message}</p>
		</form>
	</div>
	
	
	<div id='to-do'>
	% if users:
	<h2>搜索结果：</h2>
			<table id="user" >
				<thead>
					<tr>
						<th>Email</th>
						<th>姓名</th>
						<th>用户类型</th>
						<th>操作</th>
						
					</tr>
				</thead>
				<tbody>
				
				% for user in users:
					<tr>
						<td>${user.email}</td>
						<td>${user.name}</td>
						<td>
						% if user.usertype_id == 1: 
						管理员
						% elif user.usertype_id == 2:
						老师
						% else:
						家长	
						%endif
						</td>
						<td><a href="/user/${user.id}">查看</a> </td>
						
					</tr>
				% endfor
						
						
				</tbody>
			</table>
		% endif
	</div>
	<%include file="foot.html"/>
</div>



