@Blazon.index.register = 

  init: () ->
    $('a.save-profile').click () ->
      params = $('form[name=profile]').serializeObject()
      Blazon.post "/user/edit/#{params.id}/", params, (response) ->
        if not response.status?
          window.location.href = '/'
        else
          if response.message?
            alert response.message
          console.log response.message
        return 
      return
    return

@Blazon.index.register.init()