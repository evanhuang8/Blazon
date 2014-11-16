(function() {
  this.Blazon.index.register = {
    init: function() {
      $('a.save-profile').click(function() {
        var params;
        params = $('form[name=profile]').serializeObject();
        Blazon.post("/user/edit/" + params.id + "/", params, function(response) {
          if (response.status == null) {
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
