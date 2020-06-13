$(document).on('click', '#mm-subnit', function(){
	console.log('abcd');
    $.validator.setDefaults({
        submitHandler: function() {
            alert("提交事件!");
        }
    });
    $().ready(function() {
        // 手机号码验证
        jQuery.validator.addMethod("isMobile", function(value, element) {
            var length = value.length;
            var mobile = /^(13[0-9]{9})|(18[0-9]{9})|(14[0-9]{9})|(17[0-9]{9})|(15[0-9]{9})$/;
            return this.optional(element) || (length == 11 && mobile.test(value));
        }, "请正确填写您的手机号码");

        var validator = $("#form1").validate({
            errorPlacement: function(error, element) {
                $(element).closest( ".m-form2" ).find( "span" ).html( error );
            },
            errorElement: "span",
            rules: {
                mobile : {
                    required : true,
                    minlength : 11,
                    isMobile : true
                },
                mail:{
                    required : true,
                    email : true
                }
            },
            //提示信息
            messages: {
                name: {
                    required: "请输入姓名",
                    minlength: " (不能少于 2 个字母)",
                    maxlength: " (不能大于 5个字母)"
                },
                title:"请输入职位",
                mail: {
                    email:'请输入有效的邮箱地址',
                    required:"请输电子入邮箱",
                },
                company:"请输入公司名称",
                company_address:"请输入公司地址",
                industry:"请输入行业",
                project_name:"请输入项目名称",
                memo: {
                    required: "请填写您的重点需求描述",
                    minlength: " (不能少于 10 个字母)"
                },
                mobile: {
                    required: "请输入手机号",
                    isMobile : "请正确填写您的手机号码"
                },
            },
            success: function(label) {
                label.html("&nbsp;").addClass("checked");
            }
        });
    });
} )
