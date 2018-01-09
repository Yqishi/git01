$(function(){
    var $li = $('.product_image_h2 li');
    
    //获取小原点的父级
    var $points = $('.points');
    
    //存储幻灯片的个数
    var iLen = $li.length;
    
    //定义两个变量存储当前要运动过来的幻灯片的索引值
    var iNowli = 0;

    //定义两个变量存储当前要运动离开的幻灯片的索引值
    var iPrevli = 0;

    var $prev = $('.prev');
    var $next = $('.next');

    //除了第一张其他的都放右边去
    $li.not(':first').css({'left':760});


    //根据幻灯片的个数动态创建小圆点
    for(var i =0;i<iLen;i++){
        var $newli = $('<li>') 
        if(i==0){
            $newli.addClass('active');
        }
        $points.append($newli);
    }
    //获取小圆点
    $pli = $('.points li');
    
    //小圆点点击交互
    $pli.click(function(){
        iNowli = $(this).index();
        fnMove()
        $(this).addClass('active').siblings().removeClass('active');
    })


    //左右箭头点击交互
    $prev.click(function(){
        iNowli --;
        fnMove()
        $(this).prev().addClass('active').siblings().removeClass('active');
    })

    $next.click(function(){
        iNowli ++;
        fnMove()
        $(this).next().addClass('active').siblings().removeClass('active');
    })



    //幻灯片运动动画
    function fnMove(){
        if(iNowli>iLen){
            iNowli = 0;
            
            
        }
        if (iNowli == iPrevli){
            return;
        }
        if (iNowli > iPrevli){
            $li.eq(iNowli).css({'left':760});
            $li.eq(iNowli).animate({'left':0});
            $li.eq(iPrevli).animate({'left':-760});
            iPrevli = iNowli;
        }
        else{
            $li.eq(iNowli).css({'left':-760});
            $li.eq(iNowli).animate({'left':0});
            $li.eq(iPrevli).animate({'left':760});
            iPrevli = iNowli;
        }
    }
    


})
