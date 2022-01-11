$(function() {

  $('.js-check-all').on('click', function() {

  	if ( $(this).prop('checked') ) {
	  	$('th input[type="checkbox"]').each(function() {
	  		$(this).prop('checked', true);
	  	})
  	} else {
  		$('th input[type="checkbox"]').each(function() {
	  		$(this).prop('checked', false);
	  	})
  	}
  });
});

$(function() {

  $(".editable_select").editable("/update", {
    indicator : 'Saving...',
    data   : "{'A option':'A value','B option':'B value','C option':'C value'}",
    type   : "select",
    submit : "OK",
    style  : "inherit"
  });
  $(".editable_textarea").editable("/update", {
      indicator : "Saving...",
      type   : 'textarea',
      submitdata: { _method: "put" },
      select : true,
      cancel    : 'Cancel',
      submit : 'OK',
      cssclass : "editable"
  });
});