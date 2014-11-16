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

  postJSON: (url, params, cb) ->
    xhr = $.ajax url, 
      data: JSON.stringify params
      contentType: 'application/json'
      type: 'POST'
    xhr.done (data) ->
      cb? data
      return
    xhr.fail () ->
      res =
        status: 'FAIL'
        message: 'Oops, something is not right here!'
      cb? res
      return
    return

  deleteJSON: (url, params, cb) ->
    xhr = $.ajax url, 
      data: JSON.stringify params
      contentType: 'application/json'
      type: 'DELETE'
    xhr.done (data) ->
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
      Blazon.postJSON '/campaigns/', params, (response) ->
        if response.status?
          alert "Campaign Creation Error"
        else
          window.location.href = "/create/#{response.id}/"
        return
      return
    $('a.create-campaign-start-btn').click () ->
      $('div#create-campaign').slideToggle(200)
      return
    $('a.cancel-campaign-start-btn').click () ->
      $('div#create-campaign').slideUp(200)
      return
    return

@Blazon.init()