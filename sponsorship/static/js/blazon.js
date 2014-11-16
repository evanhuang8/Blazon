(function() {
  this.Blazon = {
    index: {},
    init: function() {
      $('a.create-campaign-start-btn').click(function() {
        $('div#create-campaign').slideToggle();
      });
    }
  };

  this.Blazon.init();

}).call(this);
