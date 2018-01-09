window.onload = function(){
    var oImg = document.getElementById('product_image_h2');
    var i = 2;
    function Myfunc(){ 
        var sTr ="images/slide0"+i+".jpg";
        oImg.src=sTr;
        i ++;
        if (i == 5){
            i = 1;
        } 
    }
    setInterval(Myfunc,5000);
}

$(function(){
    var $prev = $('.prev');
    var $next = $('.next');
    var $oImg = $('#product_image_h2');
    var $oPoint = $('.points li');
    var $btn = $('.product_image_h1 li .a1');
    $btn.click(function(){
        $btn.next().slideToggle();
    })
    





    $oPoint.click(function(){
        $(this).addClass('active').siblings().removeClass('active');
        var iNum =  $(this).index() + 1;
        $oImg.prop({src:"images/slide0"+iNum+".jpg"});
    })



    $next.click(function(){
        var str = $oImg.attr('src');
        var iNum = str.substring(13,14);
         
        if (iNum==4){
            iNum = 1;
            $oImg.prop({src:"images/slide0"+iNum+".jpg"});
        }
        else{
            iNum ++;
            $oImg.prop({src:"images/slide0"+iNum+".jpg"});
        }
    });

    $prev.click(function(){
        var str = $oImg.attr('src');
        var iNum = str.substring(13,14);
        
        if (iNum==1){
            $oImg.prop({src:"images/slide04.jpg"});
        }
        else{
            iNum -= 1;
            $oImg.prop({src:"images/slide0"+iNum+".jpg"});
        };
    });
});



  