@Blazon = 

  index: {}

  init: () ->
    $('a.create-campaign-start-btn').click () ->
      $('div#create-campaign').slideToggle()
      return
    return

@Blazon.init()