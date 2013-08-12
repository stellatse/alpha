<%inherit file="base.html"/>
<%include file="config_base.html"/>
			
			<div class="main">
			
			<div class="configuration">
				<h2>用户配置管理中心</h2>
				<div class="content">
			<h1>用户编号: ${profile.id}</h1>
			<table class="info_baseinfo">
			<tbody>
			% if profile:
			<form action="${request.route_url('view_user', uid=profile.id)}" method = "post" enctype="multipart/form-data">
                    % if message:
					<p style="color:red">${message}</p>
					% endif
					<label for="email">Email</label>
					<input name="email" type="text" value="${profile.email}" readonly/>
					<label for="fullname">姓名：</label>
					<input name="fullname" type="text" value="${profile.name}" readonly/>
					
					
					<label for="location">联系地址：</label>
					<input name="address" type="text" value="${profile.address}" readonly/>
					<label for="telephone">联系电话：</label>
					<input name="tele" type="text" value="${profile.telephone}" readonly/>
					<label for="type">用户类型：</label>
					<input name="type" type="text" value="${profile.usertype_id}" readonly/>
					<label>所属组</label>
					% for group in profile.mygroups:
					<a href="/user/${profile.id}/del/${group.id}">${group.name}<img src="${request.static_url('jxt:static/img/del.png')}" style="width:10px;height:10px"/></a>
					<br/>
					
					% endfor
					<label>添加所属组：</label>
						<select name="configgp">
						<option value="1">superuser</option>
						<option value="2">default</option>
						<option value="3">ChangeCordinator</option>
						<option value="4">ProblemCordinator</option>
						<option value="5">ServiceDeskHelp</option>
					</select>

			
			<input type="submit" name="chg.submitted" value="Append Group"/>
			</form>
			
			% endif
			</tbody>
			</table>
			</div>
				
				
				
				
			</div>
			<%include file="foot.html"/>
		</div>
		