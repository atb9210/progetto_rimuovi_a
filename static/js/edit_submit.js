
// # SUMBIT AND SAVE EDIT

$('#updateForm').submit(function(event) {
      event.preventDefault();
      var card_id = $('#idModal').val();
      var new_name = $('#nameModal').val();
      $.ajax({
          url: '/update',
          type: 'POST',
          data: {
              id: card_id,
              name: new_name
          },
          success: function(data) {
              window.location.href = '/';
              $('#editModal').modal('hide')
          }
      });
    });