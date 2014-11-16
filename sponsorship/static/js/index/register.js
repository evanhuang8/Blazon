(function() {
  this.Blazon.index.register = {
    init: function() {
      $('a.register').click(function() {
        var params;
        params = $('form[name=register]').serializeObject();
        Blazon.post('/user/create/', params, function(response) {
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

  this.Blazon.index.register.init();

}).call(this);
