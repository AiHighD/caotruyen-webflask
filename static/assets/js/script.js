$(document).ready(function(){
    // Bắt sự kiện click trên ảnh và tiêu đề
    $('.image-card a').click(function(e){
        e.preventDefault(); // Ngăn chặn hành vi mặc định của thẻ <a>
        var url = $(this).attr('href'); // Lấy đường dẫn từ thuộc tính href
        window.location.href = url; // Chuyển hướng trang sang đường dẫn đã lấy
    });
});
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scrollBtn").style.display = "block";
    } else {
        document.getElementById("scrollBtn").style.display = "none";
    }
}

function scrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

