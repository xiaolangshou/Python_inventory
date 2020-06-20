function Yalert(){
  this.promt=function(text,time){
    $('.y-promt').remove();
    var addHtml='<div class="y-promt">'+text+'</div>';
    $('body').before(addHtml);
    $('.y-promt').addClass('promtAnomate');
    setTimeout(function(){
      $('.y-promt').removeClass('promtAnomate');
      setTimeout(function(){
        $('.y-promt').remove();
      },500);
    },time);
  };
  this.promtOk=function(text,time) {
    var addHtmlOk='<div class="y-promtOk">'+text+'</div>';
    $('body').before(addHtmlOk);
    $('.y-promtOk').addClass('promtAnomate');
    setTimeout(function(){
      $('.y-promtOk').removeClass('promtAnomate');
      setTimeout(function(){
        $('.y-promtOk').remove();
      },500);
    },time);    
  }
};
var yAlert=new Yalert();
