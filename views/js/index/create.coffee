@Blazon.index.create = 

  init: () ->
    $('a.show-add-tier').click () ->
      $('div.tier.add').addClass 'hide'
      $('div.add-tier').removeClass 'hide'
      return
    $('div.add-tier a.cancel').click () ->
      $('div.add-tier form').trigger 'reset'
      $('div.add-tier').addClass 'hide'
      $('div.tier.add').removeClass 'hide'
      return
    $('div.tier a.delete').click () ->
      if confirm 'Are you sure you want to delete this sponsorship tier?'
        id = $(this).attr 'data-id'
        Blazon.deleteJSON "/tiers/#{id}/", {}, (response) =>
          if not response? or not response.status?
            $(@).closest('div.tier').remove()
          else
            if response.message?
              alert response.message
          return
      return
    $('div.add-tier a.add').click () ->
      params = $('form[name=tier]').serializeObject()
      params.price = parseInt(params.price) * 100
      Blazon.postJSON '/tiers/', params, (response) ->
        if response.id?
          tier = $('div.tier.template').clone true
          $(tier).removeClass('template').removeClass 'hide'
          price = (response.price / 100).toFixed 2
          $(tier).find('h3').text "$#{price} #{response.name}"
          $(tier).find('div.bottom').text response.description
          $(tier).find('a.delete').attr 'data-id', response.id
          $(tier).insertBefore $('div.tier.add')
          if not $('div.tier.empty').hasClass 'hide'
            $('div.tier.empty').addClass 'hide'
          $('form[name=tier]').trigger 'reset'
          $('div.add-tier').addClass 'hide'
          $('div.tier.add').removeClass 'hide'
        else
          if response.message?
            alert response.message
        return
      return
    $('a.show-add-inkind').click () ->
      $('div.inkind.add').addClass 'hide'
      $('div.add-inkind').removeClass 'hide'
      return
    $('div.add-inkind a.cancel').click () ->
      $('div.add-inkind form').trigger 'reset'
      $('div.add-inkind').addClass 'hide'
      $('div.inkind.add').removeClass 'hide'
      return
    $('div.inkind a.delete').click () ->
      if confirm 'Are you sure you want to delete this inkind donation request?'
        id = $(this).attr 'data-id'
        Blazon.deleteJSON "/inkinds/#{id}/", {}, (response) =>
          if not response? or not response.status?
            $(@).closest('div.inkind').remove()
          else
            if response.message?
              alert response.message
          return
      return
    $('div.add-inkind a.add').click () ->
      params = $('form[name=inkind]').serializeObject()
      Blazon.postJSON '/inkinds/', params, (response) ->
        if response.id?
          inkind = $('div.inkind.template').clone true
          $(inkind).removeClass('template').removeClass 'hide'
          price = (response.price / 100).toFixed 2
          $(inkind).find('h3').text response.name
          $(inkind).find('div.bottom').text response.description
          $(inkind).find('a.delete').attr 'data-id', response.id
          $(inkind).insertBefore $('div.inkind.add')
          if not $('div.inkind.empty').hasClass 'hide'
            $('div.inkind.empty').addClass 'hide'
          $('form[name=inkind]').trigger 'reset'
          $('div.add-inkind').addClass 'hide'
          $('div.inkind.add').removeClass 'hide'
        else
          if response.message?
            alert response.message
        return
      return
    return

@Blazon.index.create.init()