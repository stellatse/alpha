<%inherit file="base.html"/>
<div class="logo">
<a>家校通</a>
</div>
<div class="nav" id="maia-nav-x">
		<div class="tab">
		<div class="logout">
		<a href="/logout">登出</a>
		</div>
		
		<ul>
		<li class="p2"><a href="/profile" style="font-weight:bold">我的资料</a></li>

		<ul>
		</div>
</div>	
	
	<div class='main'>
<div class="welcome">
<h3>Welcome <code>${email}</code></h3>
</div>
<div class="profile">
	<div class="myside">
	<ul>
	<li><a href="/${email}/view">修改资料</a></li>
	<li><a href="/${email}/edit"></a></li>
	<ul>
	</div>
	<div class="content">
	<h1>修改个人资料</h1>
	<p>请输入密码</p>
	<table class="info_baseinfo">
	<tbody>
	% if profile:
	<form action="${request.route_url('profile',email=email)}" method = "post" enctype="multipart/form-data">
			<label for="pass">Password</label>
			<input name="pass" type="password" placeholder="Your Password"/>
			<label for="pass2">Password Check</label>
			<input name="pass2" type="password" placeholder="Password Again"/>
            % if message:
			<p style="color:red">${message}</p>
			% endif
			<label for="email">Email</label>
			<input name="email" type="text" value="${email}" readonly/>
			<label for="name">姓名：</label>
			<input name="name" type="text" value="${name}"/>
			
			<label for="location">联系地址：</label>
			<input name="address" type="text" value="${address}"/>
			<label for="telephone">联系电话：</label>
			<input name="tele" type="text" value="${tele}"/>
			

	
	<input type="submit" name="chg.submitted" value="Edit"/>
	</form>
	
	% endif
	</tbody>
	</table>
	</div>
</div>
<%include file="foot.html"/>
</div>

