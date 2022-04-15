$(document).ready(function () {



    $(".btn-eliminar").click(function (e) {

        var self = $(this)
        $.ajax({
            url: "/eliminarComentario/" + self.attr('obj-id'),

            success: function (response) {

                console.log(response)
            }
        });


    })

});
$(document).ready(function () {
    $(".btn-eliminar-publicacion").click(function (e) {

        var self = $(this)
        $.ajax({
            url: "/eliminar/" + self.attr('obj-id'),

            success: function (response) {

                console.log(response)
            }
        });


    })


});