var qaHref = $('#nav-qa').attr('href');
function setNav(){
  var winWidth=window.innerWidth?window.innerWidth:$(window).innerWidth();
  if(winWidth>768){//pc端
    $("#nav-qa").attr("href",qaHref);
    $('.nav').css({'display':'flex','height':'','opacity':1})
    //导航下拉菜单
    $('.nav>li').each(function(){
      $(this).hover(function(){
        $(this).find('div.pc-nav-xl').stop().slideDown()
      },function(){
        $(this).find('div.pc-nav-xl').stop().slideUp()
      })
    })
  }else{
    $('#nav-qa').removeAttr("href");
    $('.nav').css({'display':'block','height':0});
    //移动导航下拉菜单
    $('.nav>li').each(function(){
      if($(this).find('div').length>0){
        $(this).find('a').eq(0).click(function(){
          $(this).next('.nav-xl').addClass('active');

        })
      }
    })
  };
}
setNav();

$(window).resize(function () {
  setNav();
})


$(function(){
  //动画效果
  var wow = new WOW({
    boxClass: 'wow',
    animateClass: 'animated',
    offset: 100,
    mobile: true,
    live: true,
  });
  wow.init();

  //导航下拉菜单
//	$('.nav>li').each(function(){
//		if($(window).innerWidth()>768){
//			$(this).hover(function(){
//				$(this).find('div.pc-nav-xl').stop().slideDown()
//			},function(){
//				$(this).find('div.pc-nav-xl').stop().slideUp()
//			})
//		}else{
//
//
//		}
//	})
//

  $('#nav-btn').click(function(){
    if($(this).hasClass('active')){
      $(this).removeClass('active');
      $('.nav').css({'height':'0px','opacity':0});
      $('.nav-xl').removeClass('active');
    }else{
      $(this).addClass('active');
      $('.nav').css({'height':$(window).innerHeight()+'px','opacity':1});
    }
  })
  $('.fanhui').click(function(){
    $(this).parents('.nav-xl').removeClass('active')
  })

  var is_weixin = (function(){return navigator.userAgent.toLowerCase().indexOf('micromessenger') !== -1})();
  if(is_weixin){
    $(function(){
      document.getElementById('logolink').onclick = function(ev){
        ev.preventDefault();
        $(".wxopen").show();
      }

      $(".wxopen,.wxopen>img").click(function(){
        $(".wxopen").hide();
      });
    });
  }else{
    $(function(){
      return false;
    });
  }
})
