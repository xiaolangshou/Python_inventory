



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
    




    var headerHeight= $('header').outerHeight();


    if($(window).innerWidth()>768){
		$('#cp-fh').click(function(){
			$(this).parents('.menu-box').fadeOut(100);
		})
        //pc端导航鼠标划过效果
        $('#nav>li').each(function(a){
            $(this).hover(function(){
                $('#nav>li').removeClass('hover')
                $(this).find('.menu-box').stop().fadeIn();
            },function(){
                $('#hover').addClass('hover')
                $(this).find('.menu-box').fadeOut(100);
            })
        })

    }else{

        $('#phone-nav,.phone-nav-1').css({'top':headerHeight+'px'});
        //移动端导航鼠标划过效果
        $('#nav-btn').click(function(){
            if($(this).hasClass('active')){
                $(this).removeClass('active');
                $('#phone-nav').css({'height':0,'opacity':0});
                $('.phone-nav-1').removeClass('active')
                $('#phone-nav>li>a').removeClass('active');
                $('header').css({'transform':''})
            }else{
                $(this).addClass('active');
                $('#phone-nav,.phone-nav-1').css({'height':$(window).innerHeight()+'px','opacity':1});
                $('header').css({'transform':'translateY(0)'})
            }

        })

        $('#phone-nav>li').each(function(i){
            if($(this).find('.phone-nav-1').length>0){
                $(this).find('a').eq(0).click(function(){
                    $(this).next('.phone-nav-1').addClass('active');
                    $('#phone-nav>li>a').addClass('active');
                })
            }
        })
        $('.fanhui').click(function(){
            $(this).parents('.phone-nav-1').removeClass('active')
            $('#phone-nav>li>a').removeClass('active');
        })

 
        


    }

})
