(function() {
  this.Blazon.index.create = {
    init: function() {
      $('a.show-add-tier').click(function() {
        $('div.tier.add').addClass('hide');
        $('div.add-tier').removeClass('hide');
      });
      $('div.add-tier a.cancel').click(function() {
        $('div.add-tier form').trigger('reset');
        $('div.add-tier').addClass('hide');
        $('div.tier.add').removeClass('hide');
      });
      $('div.tier a.delete').click(function() {
        var id;
        if (confirm('Are you sure you want to delete this sponsorship tier?')) {
          id = $(this).attr('data-id');
          Blazon.deleteJSON("/tiers/" + id + "/", {}, (function(_this) {
            return function(response) {
              if ((response == null) || (response.status == null)) {
                $(_this).closest('div.tier').remove();
              } else {
                if (response.message != null) {
                  alert(response.message);
                }
              }
            };
          })(this));
        }
      });
      $('div.add-tier a.add').click(function() {
        var params;
        params = $('form[name=tier]').serializeObject();
        params.price = parseInt(params.price) * 100;
        Blazon.postJSON('/tiers/', params, function(response) {
          var price, tier;
          if (response.id != null) {
            tier = $('div.tier.template').clone(true);
            $(tier).removeClass('template').removeClass('hide');
            price = (response.price / 100).toFixed(2);
            $(tier).find('h3').text("$" + price + " " + response.name);
            $(tier).find('div.bottom').text(response.description);
            $(tier).find('a.delete').attr('data-id', response.id);
            $(tier).insertBefore($('div.tier.add'));
            if (!$('div.tier.empty').hasClass('hide')) {
              $('div.tier.empty').addClass('hide');
            }
            $('form[name=tier]').trigger('reset');
            $('div.add-tier').addClass('hide');
            $('div.tier.add').removeClass('hide');
          } else {
            if (response.message != null) {
              alert(response.message);
            }
          }
        });
      });
      $('a.show-add-inkind').click(function() {
        $('div.inkind.add').addClass('hide');
        $('div.add-inkind').removeClass('hide');
      });
      $('div.add-inkind a.cancel').click(function() {
        $('div.add-inkind form').trigger('reset');
        $('div.add-inkind').addClass('hide');
        $('div.inkind.add').removeClass('hide');
      });
      $('div.inkind a.delete').click(function() {
        var id;
        if (confirm('Are you sure you want to delete this inkind donation request?')) {
          id = $(this).attr('data-id');
          Blazon.deleteJSON("/inkinds/" + id + "/", {}, (function(_this) {
            return function(response) {
              if ((response == null) || (response.status == null)) {
                $(_this).closest('div.inkind').remove();
              } else {
                if (response.message != null) {
                  alert(response.message);
                }
              }
            };
          })(this));
        }
      });
      $('div.add-inkind a.add').click(function() {
        var params;
        params = $('form[name=inkind]').serializeObject();
        Blazon.postJSON('/inkinds/', params, function(response) {
          var inkind, price;
          if (response.id != null) {
            inkind = $('div.inkind.template').clone(true);
            $(inkind).removeClass('template').removeClass('hide');
            price = (response.price / 100).toFixed(2);
            $(inkind).find('h3').text(response.name);
            $(inkind).find('div.bottom').text(response.description);
            $(inkind).find('a.delete').attr('data-id', response.id);
            $(inkind).insertBefore($('div.inkind.add'));
            if (!$('div.inkind.empty').hasClass('hide')) {
              $('div.inkind.empty').addClass('hide');
            }
            $('form[name=inkind]').trigger('reset');
            $('div.add-inkind').addClass('hide');
            $('div.inkind.add').removeClass('hide');
          } else {
            if (response.message != null) {
              alert(response.message);
            }
          }
        });
      });
      $('div.send-emails a.send').click(function() {
        var params;
        params = $('form[name=emails]').serializeObject();
        params.emails = params.emails.split(',');
        Blazon.postJSON('/campaigns/send_emails/', params, function(response) {
          if (response.length > 0) {
            alert('The emails have been sent to your potential sponsors/donors!');
            $('form[name=emails]').trigger('reset');
          } else {
            if (response.message != null) {
              alert(response.message);
            }
          }
        });
      });
    }
  };

  this.Blazon.index.create.init();

}).call(this);
