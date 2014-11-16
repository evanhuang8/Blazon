@Blazon.index.register = 

  init: () ->
    $('a.register').click () ->
      params = $('form[name=register]').serializeObject()
      Blazon.post '/user/create/', params, (response) ->
        if response.status is 'OK'
          window.location.href = '/'
        else
          if response.message?
            alert response.message
          console.log response.message
        return 
      return
    return

@Blazon.index.register.init()