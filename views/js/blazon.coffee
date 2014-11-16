@Blazon = 

  index: {}

  init: () ->
    $('a.create-campaign-start-btn').click () ->
      $('div#create-campaign').slideToggle()
      return
    $('a.cancel-campaign-start-btn').click () ->
      $('div#create-campaign').slideUp()
      return
    return

@Blazon.init()