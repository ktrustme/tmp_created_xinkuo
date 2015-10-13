/**
 * Created by kuoxin on 10/8/15.
 */
var main = function(){

    var editProfileBtn = document.querySelector(".user_info_table .edit_profile_btn");

    editProfileBtn.onclick = function(){
        $(".user_info_table").animate({opacity:'0.0'});
        var distance = $(".user_info_table").outerHeight();

        $(".edit_user_info_table").animate({opacity: '1', top: "" + (-distance-30)+""});
    };

    if( $("#error_flag:empty").length == 0){
        var distance = $(".user_info_table").outerHeight();
        $(".user_info_table").css({opacity:'0.0'});
        $(".edit_user_info_table").css({"opacity": '1', "top": "" + (-distance-30)+"px"});
    }
    $(".follow_btn_large").click(function(){alert("HI");});

}

document.addEventListener("DOMContentLoaded", main);