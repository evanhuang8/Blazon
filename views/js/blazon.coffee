@Blazon = 

  index: {}

  get: (url, params={}, cb) ->
    xhr = $.get url, params, (data) ->
      cb? data
      return
    xhr.fail () ->
      res =
        status: 'FAIL'
        message: 'Oops, something is not right here!'
      cb? res
      return
    return

  post: (url, params={}, cb) ->
    xhr = $.post url, params, (data) ->
      cb? data
      return
    xhr.fail () ->
      res =
        status: 'FAIL'
        message: 'Oops, something is not right here!'
      cb? res
      return
    return

  init: () ->
    # Inject CSRF token for each ajax request
    $.ajaxSetup 
      beforeSend: (xhr, settings) ->
        xhr.setRequestHeader 'X-CSRFToken', csrfToken
        return
    # Global actions
    $('a.create-campaign-btn').click () ->
      params = $(this).closest('form[name=create_campaign]').serializeObject()
      Blazon.post '/campaigns/', params, (response) ->
        console.log response
        return
      return
    $('a.create-campaign-start-btn').click () ->
      $('div#create-campaign').slideToggle()
      return
    $('a.cancel-campaign-start-btn').click () ->
      $('div#create-campaign').slideUp()
      return
    return

@Blazon.init()