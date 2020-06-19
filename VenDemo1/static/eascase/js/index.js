//解决方案hover
//设置默认
$('.index-program-list>li').eq(0).addClass('index-program-list-on');
$('.index-program-list>li').hover(function(){
  $('.index-program-list>li').removeClass('index-program-list-on');
  $(this).addClass('index-program-list-on');
});
//客户说
var indexMessage=new Swiper('.index-message-slide',{
  loop:true,
  direction: 'vertical',
  slidesPerView: 2,
  autoplay:3000,
});
$('.message-prev').on('click',function(){
    indexMessage.slidePrev();
});
$('.message-next').on('click',function(){
    indexMessage.slideNext();
});
//新闻资讯
var indexNews=new Swiper('.index-news-slide',{
  simulateTouch:false
});
$('.index-news-nav>ul>li').eq(0).addClass('inde-news-on');
$('.index-news-nav>a').eq(0).show();
$('.index-news-nav>ul>li').hover(function(){
  $('.index-news-nav>ul>li').removeClass('inde-news-on');
  var index=$(this).index();
  $('.index-news-nav>a').hide();
  $('.index-news-nav>a').eq(index).show();
  $('.index-news-nav>ul>li').eq(index).addClass('inde-news-on');
  indexNews.slideTo(index);
});
//banner划过
var start={};
var end={};
var move={};
$('.banner-right').on('mouseover',function(e){
  if(start.x=='' || start.x==null){
    start.x=e.clientX;
  }else {
    start.x=start.x;
  };
  if(start.y=='' || start.y==null) {
    start.y=e.clientY;
  }else {
    start.y=start.y;
  };
});
$('.banner-right').on('mousemove',function(e){
  end.x=e.clientX;
  end.y=e.clientY;
  move.x=parseInt(start.x)-parseInt(end.x);
  move.y=parseInt(start.y)-parseInt(end.y);
  $(this).find('img').eq(0).css('transform','translate('+move.x/30+'px,'+move.y/10+'px)');
  $(this).find('img').eq(1).css('transform','translate('+move.x/35+'px,'+move.y/15+'px)');
  $(this).find('img').eq(2).css('transform','translate('+move.x/40+'px,'+move.y/20+'px)');
});
