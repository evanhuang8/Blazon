@Blazon.index.login = 

  init: () ->
    $('a.login').click () ->
      params = $('form[name=login]').serializeObject()
      Blazon.post '/user/auth/', params, (response) ->
        if response.status is 'OK'
          window.location.href = '/'
        else
          if response.message?
            alert response.message
          console.log response.message
        return 
      return
    return

@Blazon.index.login.init()