function obj2str(obj) {
    //遍历对象
    obj.t=new Date().getDate();
   var res =[];
   for (var key in obj){
       res.push(key+"="+obj[key]);
   }
   return res.join("&");
}
function ajaxget(url,obj,success,error){
    //0.将对象转换为字符串
    var str = obj2str(obj);
    //1.创建异步对象
    var xmlhttp;
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    //2.设置请求方式和地址
    /*
    method:请求类型：GET或者POST
    url:文件在服务器上的位置
    async:true(异步)或false（同步）
    */
    xmlhttp.open("GET",url +"?"+str,true);
    //3.发送请求
    xmlhttp.send();
    //4.监听状态变化
    xmlhttp.onreadystatechange=function(ev2)
    {
        /*
        存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。

       0: 请求未初始化
       1: 服务器连接已建立
       2: 请求已接收
       3: 请求处理中
       4: 请求已完成，且响应已就绪
       */
        if (xmlhttp.readyState==4 )
        {
            //判断是否请求成功
            if(xmlhttp.status>=200 && xmlhttp.status<300 || xmlhttp.status===304){
                //5.处理返回结果
                success(xmlhttp);
            }
            else {
                error(xmlhttp);
            }
        }
    }
}