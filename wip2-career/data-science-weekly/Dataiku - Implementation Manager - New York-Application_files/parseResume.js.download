$(function(){
  var POST_PATH = '/parseResume'
  var MAX_FILE_SIZE = 100*1000*1000; // 100 MB
  var req;

  var failure = $('.resume-upload-failure');
  var success = $('.resume-upload-success');
  var working = $('.resume-upload-working');
  var oversizeFailure = $('.resume-upload-oversize');

  function updateFields (data) {
    try {
      data = JSON.parse(data);
      success.show();
    } catch (e) {
      failure.show();
      return;
    }
    if (!data) {
      return;
    }

    if (data.positions && data.positions[0] && data.positions[0].org) {
      updateIfEmpty($('input[name=org]'), data.positions[0].org);
    }

    if (data.phones && data.phones[0] && data.phones[0].value) {
      updateIfEmpty($('input[name=phone]'), data.phones[0].value);
    }

    if (data.names && data.names[0]) {
      updateIfEmpty($('input[name=name]'), data.names[0]);
    }

    if (data.emails && data.emails[0] && data.emails[0].value) {
      updateIfEmpty($('input[name=email]'), data.emails[0].value);
    }

    if (data.links && data.links.length > 0) {
      var urls = ['LinkedIn', 'Twitter', 'Quora', 'GitHub']
      for (var i = 0; i < data.links.length; i++) {
        var link = data.links[i];
        for (var j = 0; j < urls.length; j++) {
          var fieldName = urls[j];
          if (link.domain && link.domain.toLowerCase().indexOf(fieldName.toLowerCase()) > -1) {
            updateIfEmpty($('input[name="urls[' + fieldName + ']"]'), link.url);
          } else {
            updateIfEmpty($('input[name="urls[Other]"]'), link.url);
          }
        }
      }
    }
  }

  function updateIfEmpty (field, value) {
    if (!field || field.val()) {
      return;
    }
    field.val(value);
  }

  $('#resume-upload-input').change(function(){
    failure.hide();
    success.hide();
    working.hide();
    oversizeFailure.hide();

    var file = this.files[0];
    if (!file || file.size == 0) {
      // File changed to nothing
      return;
    }
    if (file.size > MAX_FILE_SIZE) {
      oversizeFailure.show();
      return;
    }
    working.show();
    var formData = new FormData();
    formData.append('resume', file);

    if (req && req.readyState < 4) {
      req.abort();
    }

    req = new XMLHttpRequest();
    req.onreadystatechange = function(e) {
      if (req.readyState === 4) {
        working.hide();
        if (req.status === 200) {
          updateFields(req.response);
        } else if (req.status === 400 && req.responseText === 'PayloadTooLargeError' ) {
          oversizeFailure.show();
        } else {
          failure.show();
        }
      }
    };
    req.open('POST', POST_PATH, true);
    req.send(formData);
  });
});
