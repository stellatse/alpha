(function($) {
    //层背景默认参数
    var setupJqueryMPopups = {
        screenLockerBackground: "#000",
        screenLockerOpacity: 0.5
    };

    var defaultType = true;//_id的时候
    var boxId = '';
    //设置层背景
    $.setupJMPopups = function(settings) {
        setupJqueryMPopups = jQuery.extend(setupJqueryMPopups, settings);
        return this;
    }
    
    //打开层
    $.openLayer = function(settings){
        
        settings = jQuery.extend({
                width: "500px",
                height: "500px",
                target: "",
                type:"_id"
        }, settings);
        addBg ();
        
        openWindow(settings);
    };
    
    //关闭层
    $.closeLayer = function(settings){
        closeFn (settings);
    };

    //层内容
    var conId ; //层内容id
    function openWindow(settings){
        
        conId = "#layCon";    
        
        if(settings.type=='ajax'){
            $("body").append("<div id='layCon'></div>");
            $(conId).load(settings.target);    
            defaultType = false;
        }else if(settings.type=='_id'){
            defaultType = true;
            $("#"+settings.target).wrap("<div id='layCon'></div>");
            boxId = settings.target;
            
            $("#"+settings.target).fadeIn(100);
        }    
        $(conId).css({
                     width:settings.width,
                     height:settings.height,
                     zIndex:1001,
                     position:"absolute"
        });        
        
        countLayer(true);//设置坐标
        
        window.onscroll = function(){
            setBg();
        };
        window.onresize = function(){
            setBg();
        };
    };
    
    
    //设置层内容方法
    function countLayer(test){
        var windowWidth,windowHeight,scrollTop;//窗口的高和宽
        //取得窗口的高和宽
        if (self.innerHeight) {
            windowWidth=self.innerWidth-20;//火狐减去滚动条宽度
            windowHeight=self.innerHeight;
        }else if (document.documentElement&&document.documentElement.clientHeight) {
            windowWidth=document.documentElement.clientWidth;
            windowHeight=document.documentElement.clientHeight;
        } else if (document.body) {
            windowWidth=document.body.clientWidth;
            windowHeight=document.body.clientHeight;
        };
        scrollTop = document.documentElement.scrollTop || document.body.scrollTop;//显示区域以上隐藏部分高度
        var l=0;//左
        var t=0;//上
            l=windowWidth/2-$(conId).width()/2;
            t=windowHeight/2-$(conId).height()/2;
            if($(conId).outerHeight(true)>windowHeight){
				t = scrollTop;
			}else{
				t = scrollTop+t;//隐藏部分+相对窗口居中值
			}
            //alert($(conId).width()/2);
        if(test){//如果是点击弹开，直接设置坐标（防止僵硬的显示）
            $(conId).css({
                left:l+"px",
                top:t+"px"
            });
        }else{//滚动/改变窗口的时候改变坐标
            $(conId).animate({
                left:l+"px",
                top:t+"px"
         }, 300 );
        }        
        
    }
    
    //层背景
    var bgId ;
    function addBg (){
        $("body").append("<div id='layBg' style='display:none'><!----></div>");
        bgId = "#layBg";
        $(bgId).css({
                    background:setupJqueryMPopups.screenLockerBackground,
                    opacity: setupJqueryMPopups.screenLockerOpacity,
                    zIndex:1000,
                    width:$(document.body).outerWidth(true),
                    height:$(document).height(),
                    position:"absolute",
                    left:0,
                    top:0
        });
        $(bgId).fadeIn();//渐变显示
        if($("#layCon:hidden")){$("#layCon").fadeIn(100);}
        $(bgId).click(function(){
             $.closeLayer();
        });
    };
    
    //设置背景大小
    function setBg(){
        $(conId).stop();
        countLayer();
        
        $(bgId).css({
                width:$(document.body).outerWidth(true),
                height:$(document).height()
        });
    };
    
    //关闭层
    function closeFn (settings){
        $(bgId).fadeOut(100);//渐变消失    
        $(conId).fadeOut(100);//渐变消失    
        
        var setIntervalID = setInterval(function(){                    
            if(defaultType){    
                $("#"+boxId).unwrap();
                $("#"+boxId).hide();
            }else{
                $("div").remove(conId);
            }
            
            $("div").remove(bgId);
            clearInterval(setIntervalID);
        },200);

    };
    
})(jQuery);

/*百问百答*/
//<!--

