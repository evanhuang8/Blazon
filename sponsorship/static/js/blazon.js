(function() {
  this.Blazon = {
    index: {},
    init: function() {
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
