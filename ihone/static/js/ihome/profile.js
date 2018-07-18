

function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(document).ready(function () {
    // 页面加载好
    $("#form-avatar").submit(function (event) {
        event.preventDefault()
        // jquery.form.min.js  让form表单支持ajax异步提交
        $(this).ajaxSubmit({
            url:"/api/v1_0/users/avatar",
            type:"post",
            dataType:"json",
            headers:{
                "X-CSRFToken":getCookie("csrf_token")
            },
            success:function (resp) {
                if (resp.errno==0){
                    $("#user-avatar").attr("src",resp.data.avatar_url)
                }else if (resp.errno==4101){
                    location.href="/login.html"
                }else {
                    alert(resp.errmsg);
                }
            }
        });

    })

})


