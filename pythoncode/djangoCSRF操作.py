<body>

        <input type="button" onclick="AjaxSubmit();" value="Ajax提交">
        <script src="/static/js/jquery.js"></script> 

        <script>
            // 获取cookie csrftoken
			function getCookie(c_name)
			{
			    if (document.cookie.length > 0)
			    {
			        c_start = document.cookie.indexOf(c_name + "=");
			        if (c_start != -1)
			        {
			            c_start = c_start + c_name.length + 1;
			            c_end = document.cookie.indexOf(";", c_start);
			            if (c_end == -1) c_end = document.cookie.length;
			            return unescape(document.cookie.substring(c_start,c_end));
			        }
			    }
			    return "";
			 }
			
            function AjaxSubmit(){

                // 写入setting
			    $.ajaxSetup({
			        headers: { "X-CSRFToken": getCookie("csrftoken") }

			    });  

				$.ajax({
                    url:'/it/ajax/',
                    type:'POST',
                    data:{h:'host',p:'port'},
                    success:function(arg){}
                });
            };
        </script>

</body>


#对于form可以加个标签 后端用render渲染
<form  method="post" action="">

    {% csrf_token %}

</form>