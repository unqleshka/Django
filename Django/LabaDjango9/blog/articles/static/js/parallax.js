$(document).ready(function(){
    var lotusFirstPosition=$('.icons-for-parallax').offset().top; 
    var currentPosition; 
    $(document).scroll(function(){ 
        if($('.icons-for-parallax').offset().top<=$(document).scrollTop()){ 
            currentPosition=$(document).scrollTop(); 
            $('.icons-for-parallax').css('top',$(document).scrollTop()+'px'); 
            $('.icons-for-parallax').css({ 
            'position':'absolute' 
            }) 
        } 
        else if(currentPosition>=lotusFirstPosition){ 
            currentPosition=$(document).scrollTop(); 
            $('.icons-for-parallax').css('top',$(document).scrollTop()+'px'); 
        } 
        else{ 
            $('.icons-for-parallax').css('top',lotusFirstPosition+'px'); 
        } 
    }); 
});