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

		<ul>
		</div>
</div>	

<div class="main">

<div class="configuration">
		<div class="content">
		% if reply:
	

			<table class="info_baseinfo">
			<tbody>
			
			<form action="${request.route_url('reply_mail', mid=mail.id)}" method = "post" enctype="multipart/form-data">
                    % if message:
					<p style="color:red">${message}</p>
					% endif
					<label for="email">收件人:</label>
					<input name="email" type="text" value="${m_from.name}" readonly/>
					<label for="fullname">标题：</label>
					<input name="title" type="text" value="RE:${mail.title}" />
					<input name="unique" type="hidden" value="${mail.unique}"/>
					<input name="m_to" type="hidden" value="${m_from.id}"/>
					
					<label for="location">内容：</label>
					<textarea name="content" rows="10" cols="25">${mail.content}</textarea>

			
			<input type="submit" name="chg.submitted" value="回复"/>
			</form>
			</tbody>
			</table>
		%else:
			<table class="info_baseinfo">
			<tbody>
                    % if message:
					<p style="color:red">${message}</p>
					% endif
					<label for="email">发件人：${m_from.name}</label>
					<br/>
					
					<label for="location">标题：${mail.title}</label>
					<br/>
					<label for="telephone">内容：${mail.content}</label>
					<br/>
					<a href="/reply/${mail.id}">回复</a>
			
			</tbody>
			</table>
		%endif
		</div>


				
				
				
				
</div>

</div>