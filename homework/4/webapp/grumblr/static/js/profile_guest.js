/**
 * Created by kuoxin on 10/8/15.
 */
var main = function(){

    var distance = $(".follow_btn_large").outerWidth();
    $(".follow_btn_large").each(function(){
        if($(this).siblings(".follow_or_not").val() === '-1') {
            $(this).css({"opacity":0})
            $(this).next().css({"opacity":"0"});
        }
        if($(this).siblings(".follow_or_not").val() === '1') {
            $(this).css({"opacity":0})
            $(this).next().css({"opacity":"1", "left":"-"+(distance+15)+"px"});
        }
    });

    //alert($(".follow_or_not").first().val());
    $(".unfollow_btn_large").each(function(){
        if($(this).siblings(".follow_or_not").val() === '-1') {
            $(this).css({"opacity":0})
            $(this).next().css({"opacity":"0"});
        }
        if($(this).siblings(".follow_or_not").val() === '0') {
            $(this).css({"opacity":0})
        }

    });

    $(".follow_btn_large").click(function(){
            var distance = $(".follow_btn_large").outerWidth();
            var data = $.get("/follow_"+$(".follow_btn_large").val(), function(data){
                //alert(data);
                if(data==="success"){
                    $(".unfollow_btn_large").animate({"opacity":"1", "left":"-"+(distance+15)+"px"});
                    $(".follow_btn_large").animate({"opacity":"0"});
                }
            });
        }
    );

    $(".unfollow_btn_large").click(function(){
            //alert($(".follow_btn_large").val());
            var data = $.get("/unfollow_"+$(".unfollow_btn_large").val(), function(data){
                //alert(data);
                if(data==="success"){
                    $(".follow_btn_large").animate({"opacity":"1"});
                    $(".unfollow_btn_large").animate({"opacity":"0", "left":"0"});

                }
            });
        }
    );

}

document.addEventListener("DOMContentLoaded", main);/**
 * Created by kuoxin on 10/9/15.
 */
