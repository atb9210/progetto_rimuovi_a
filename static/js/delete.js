
$('.delete-card').click(function(e){
    e.preventDefault();
    var card_id = $(this).data('card-id');
    var url = '/card/' + card_id;
    $.ajax({
        type: 'DELETE',
        url: url,
        success: function(data){
          $('div.card#' + card_id).remove();
        },
        error: function(xhr, status, error){
            console.log(xhr.responseText);
        }
    });
});