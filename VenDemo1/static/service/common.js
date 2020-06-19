//导航
var top=$(window).scrollTop(0);

$(window).on('scroll',function(){
  var top=$(window).scrollTop();
  if(top>=40) {
      $('.nav-box').addClass('nav-alert-box');
  }else {
    $('.nav-box').removeClass('nav-alert-box');
  };
    if(top>=1865) {
      indexAdvant();
    }else if(top<=1500){
      indexAdvantReset();
    };
});
//我们的优势
function indexAdvant(){
  //合作客户数量
  var client={
    num:500,
    freq:1,
    time:1,
    start:Number($('.index-advan-left>em').text())
  };
  var clientNum=setInterval(function(){
    if(client.start!=client.num){
        client.start+=client.freq;
        $('.index-advan-left>em').text(client.start);
    }else {
      clearInterval(clientNum);
    };
  },client.time);
  //行业经验
  var experience={
    num:9,
    freq:1,
    time:150,
    start:Number($('.index-advan-center>em').text())
  };
  var experNum=setInterval(function(){
    if(experience.start!=experience.num) {
      experience.start+=experience.freq;
      $('.index-advan-center>em').text(experience.start);
    }else {
      clearInterval(experNum);
    }
  },experience.time);
};
function indexAdvantReset(){
  $('.index-advan-left>em').text(0);
  $('.index-advan-center>em').text(0);
};
//意见提交
function sendData(dle){

  var that=dle;
  var info={
    name:$('#name').val(),
    phone:$('#phone').val(),
    message:$('#message').val(),
    code:$('#code').val()
  };
  var infoReg={
    name:/[\u4e00-\u9fa5]/,
    phone:/0?(13|14|15|18|17)[0-9]{9}/,
    tell:/0\d{2,3}-\d{5,9}|0\d{2,3}-\d{5,9}/
  };
  if(info.name==''){
    yAlert.promt('请输入您的姓名',4000);
    $('#name').focus();
    return false;
  }else if(!infoReg.name.test(info.name)) {
    yAlert.promt('请输入正确的姓名',4000);
    $('#name').focus();
    return false;
  }else if(info.phone=='') {
    yAlert.promt('请输入您的电话号码',4000);
    $('#phone').focus();
    return false;
  }else if(!infoReg.phone.test(info.phone)){
    yAlert.promt('请输入正确的联系方式',4000);
    $('#phone').focus();
    return false;
  }else if(info.message==''){
    yAlert.promt('请输入您的需求',4000);
    $('#message').focus();
    return false;
  }else if(info.code=='') {
    yAlert.promt('请输入验证码',4000);
    $('#code').focus();
    return false;    
  };
  //发送需求
  $(that).text('数据提交中...');
  $(that).unbind();
  $.get('/index.php?m=content&v=message',{data:info},function(data){
    console.log(data);
    if(data=='OK') {
      yAlert.promtOk('需求提交成功',4000);
      // $('#name').val('');
      // $('#phone').val('');
      // $('#message').val('');
      // $('#code').val('');
      setTimeout(function(){
        window.location.reload(); 
      }, 4000);
       
    }else if(data=='code_error'){
      yAlert.promt('验证码输入错误',40000);
      $('#code').val('');
      $('#code').focus();     

      //window.location.reload();   
    };
    $(that).text('提交需求');
      $('.index-send').on('click',function(){
        sendData(this);
      });  

   },'text');
};
$('.index-send').on('click',function(){
  sendData(this);
});
//返回顶部
$('.go-top').on('click',function(){
  $(document).scrollTop(0);
});
