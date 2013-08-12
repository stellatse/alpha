<%inherit file="base.html"/>
<body>
	<div class="logo">
		<a>家校通</a>
		</div>
		<div class="nav" id="maia-nav-x">
				<div class="tab">
				<div class="logout">
				<a href="/logout"></a>
				</div>
				
				<ul>
				
				<li class="p2"><a href="/"></a></li>
				<li class="p3"><a href=""></a></li>
				<li class="p4"><a href=""></a></li>
				<li class="p5"><a href=""></a></li>
				<li class="active"><a href="/help" style="font-weight:bold">帮助</a></li>
				<ul>
				</div>
		</div>	
			
			<div class='main'>
			<div class='login'>
			<p>请登录：</p>
				<form action= "${request.route_url('login')}" method = "POST">
				
					<label for="email">Email</label>
					<input name="email" type="text" placeholder="Email"/>
					<label for="pass">Password</label>
					<input name="pass" type="password" placeholder="Password"/>
					<p>第一次使用？密码就是你的邮箱地址。</p>
                    <input type="submit"  name="form.submitted" value="LOG IN"/>
					% if message:
					<p style='color:#FF0000'>${message}</p>
					% endif
				</form>
			</div>	
			<div class="login_message">
			<h3>欢迎进入家校通网站</h3>
			<p>家校通搭起了学生家长与老师之间联系的桥梁。</p>
			<p>XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</p>
			<p>如果你不知道家校通的帐号，请联系管理员admin@jxt.com</p>
			<p><a href="/help">更多帮助</a></p>
			</div>			
			
			</div>
</body>

