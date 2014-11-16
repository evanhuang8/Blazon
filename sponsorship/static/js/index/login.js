(function() {
  this.Blazon.index.login = {
    init: function() {
      $('a.login').click(function() {
        var params;
        params = $('form[name=login]').serializeObject();
        Blazon.post('/user/auth/', params, function(response) {
          if (response.status === 'OK') {
            window.location.href = '/';
          } else {
            if (response.message != null) {
              alert(response.message);
            }
            console.log(response.message);
          }
        });
      });
    }
  };

  this.Blazon.index.login.init();

}).call(this);
