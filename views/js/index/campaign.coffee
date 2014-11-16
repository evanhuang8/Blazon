@Blazon.index.campaign = 

  init: () ->
    $('div.inkind-choices div.donation').click () ->
      if not $(this).hasClass 'active'
        $(this).addClass 'active'
        $(this).find('div.details').removeClass 'hide'
      return
    $('div.monetary-choices div.donation').click () ->
      $('div.monetary-choices div.donation').not(this).removeClass 'active'
      if $(this).hasClass 'active'
        $('div.payment').addClass 'hide'
      else
        price = $(this).attr 'data-price'
        $('div.payment').removeClass 'hide'
        $('div.payment div.amount').text price
      $(this).toggleClass 'active'
      return
    $('a.cancel-donation-btn').click (event) ->
      event.stopPropagation()
      $(this).closest('.details').addClass 'hide'
      $(this).closest('.donation').removeClass 'active'
      return
    return

@Blazon.index.campaign.init()