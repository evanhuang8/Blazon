(function() {
  this.Blazon.index.campaign = {
    init: function() {
      $('div.inkind-choices div.donation').click(function() {
        if (!$(this).hasClass('active')) {
          $(this).addClass('active');
          $(this).find('div.details').removeClass('hide');
        }
      });
      $('div.monetary-choices div.donation').click(function() {
        $('div.monetary-choices div.donation').not(this).removeClass('active');
        $(this).toggleClass('active');
      });
      $('a.cancel-donation-btn').click(function(event) {
        event.stopPropagation();
        $(this).closest('.details').addClass('hide');
        $(this).closest('.donation').removeClass('active');
      });
    }
  };

  this.Blazon.index.campaign.init();

}).call(this);
