$(function() {
    $('.gallItem').click(function (e) {
        $('.modal').show()
        $('.popupBox').show()
        $('.popupBox').css("display", "flex");
    })
    $('.modal').click(function (e) {
        $('.modal').hide()
        $('.popupBox').hide()
    })
})