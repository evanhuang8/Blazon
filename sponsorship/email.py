from mandrill import Mandrill
from django.conf import settings

def sendEmails(to, from_name, subject, template, mergeVars):
  """
  Send an email
  """
  try:
    client = Mandrill(settings.MANDRILL_API_KEY)
    message = {
      'from_email': settings.MANDRILL_FROM_EMAIL,
      'from_name': from_name,
      'headers': {
        'Reply-To': settings.MANDRILL_FROM_EMAIL
      },
      'subject': subject,
      'merge_vars': mergeVars,
      'to': to,
      'track_clicks': True,
      'track_opens': True,
    }
    result = client.messages.send_template(template_name = template, 
                                           template_content = [], 
                                           message = message, 
                                           async = True)
  except Exception as e:
    return False
  else:
    return result

def sendCampaignPrompt(prompt):
  """
  Send prompt email
  """
  to = [{
    'email': prompt.user.email,
    'name': prompt.user.first_name + ' ' + prompt.user.last_name
  }]
  subject = prompt.campaign.name
  template = ''
  mergeVars = [{
    'rcpt': prompt.user.email,
    'vars': []
  }]
  return