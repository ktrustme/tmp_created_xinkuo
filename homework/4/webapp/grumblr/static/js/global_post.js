/**
 * Created by kuoxin on 10/8/15.
 */
var main = function(){
    var distance = $(".follow_btn").outerWidth();
    $(".follow_btn").each(function(){
        if($(this).siblings(".follow_or_not").val() === '-1') {
            $(this).css({"display":"none"})
            $(this).next().css({"display":"none"});
        }
        if($(this).siblings(".follow_or_not").val() === '1') {
            $(this).css({"opacity":0})
            $(this).next().css({"opacity":"1", "left":"-"+(distance+15)+"px"});
        }
    });

    //alert($(".follow_or_not").first().val());
    $(".unfollow_btn").each(function(){
        if($(this).siblings(".follow_or_not").val() === '-1') {
            $(this).css({"opacity":0})
            $(this).next().css({"opacity":"0"});
        }
        if($(this).siblings(".follow_or_not").val() === '0') {
            $(this).css({"opacity":0})
        }

    });

    $(".follow_btn").click(function(){

            var this_btn = $(this);
            var data = $.get("/follow_"+$(this).val(), function(data){
                //alert(data);
                if(data==="success"){
                    this_btn.next().animate({"opacity":"1", "left":"-"+(distance+15)+"px"});
                    this_btn.animate({"opacity":"0"});
                }
            });
        }
    );

    $(".unfollow_btn").click(function(){
            var this_btn = $(this);
            var data = $.get("/unfollow_"+$(this).val(), function(data){
                //alert(data);
                if(data==="success"){
                    this_btn.prev().animate({"opacity":"1"});
                    this_btn.animate({"opacity":"0", "left":"0"});

                }
            });
        }
    );

}

document.addEventListener("DOMContentLoaded", main);/**
 * Created by kuoxin on 10/9/15.
 */
