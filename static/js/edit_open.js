
// # OPEN MODAL EDIT

$('.edit-card').click(function(event) {
    event.preventDefault();
    var card_id = $(this).data('card-id');
    console.log(card_id);
    $.ajax({
        url: '/edit/' + card_id,
        type: 'GET',
        success: function(data) {
            // populate the form fields with the returned data
            console.log(data);  // log the entire data object
            console.log(data.name);  // log the data.name value
            console.log(data.id);   // log the data.id value
            $('#nameModal').val(data[1]);
            $('#idModal').val(data[0]);
            //show the modal
            $('#editModal').modal('show');
        }
    });
});