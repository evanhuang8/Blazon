(function() {
  this.Blazon = {
    index: {},
    get: function(url, params, cb) {
      var xhr;
      if (params == null) {
        params = {};
      }
      xhr = $.get(url, params, function(data) {
        if (typeof cb === "function") {
          cb(data);
        }
      });
      xhr.fail(function() {
        var res;
        res = {
          status: 'FAIL',
          message: 'Oops, something is not right here!'
        };
        if (typeof cb === "function") {
          cb(res);
        }
      });
    },
    post: function(url, params, cb) {
      var xhr;
      if (params == null) {
        params = {};
      }
      xhr = $.post(url, params, function(data) {
        if (typeof cb === "function") {
          cb(data);
        }
      });
      xhr.fail(function() {
        var res;
        res = {
          status: 'FAIL',
          message: 'Oops, something is not right here!'
        };
        if (typeof cb === "function") {
          cb(res);
        }
      });
    },
    postJSON: function(url, params, cb) {
      var xhr;
      xhr = $.ajax(url, {
        data: JSON.stringify(params),
        contentType: 'application/json',
        type: 'POST'
      });
      xhr.done(function(data) {
        if (typeof cb === "function") {
          cb(data);
        }
      });
      xhr.fail(function() {
        var res;
        res = {
          status: 'FAIL',
          message: 'Oops, something is not right here!'
        };
        if (typeof cb === "function") {
          cb(res);
        }
      });
    },
    init: function() {
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          xhr.setRequestHeader('X-CSRFToken', csrfToken);
        }
      });
      $('a.create-campaign-btn').click(function() {
        var params;
        params = $(this).closest('form[name=create_campaign]').serializeObject();
        Blazon.postJSON('/campaigns/', params, function(response) {
          window.location.href = "/create/" + response.id + "/";
        });
      });
      $('a.create-campaign-start-btn').click(function() {
        $('div#create-campaign').slideToggle();
      });
      $('a.cancel-campaign-start-btn').click(function() {
        $('div#create-campaign').slideUp();
      });
    }
  };

  this.Blazon.init();

}).call(this);
