import json
from django.test import TestCase, Client
from sponsorship.models import *

class UserTestCase(TestCase):

  def test_user_create_auth(self):
    # Create user
    client = Client()
    response = client.post('/user/create/', {
      'email': 'johndoe@example.com',
      'password': 'password1',
      'first_name': 'John',
      'last_name': 'Doe'
    })
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(content['status'], 'OK')
    # Authenticate user
    client = Client()
    response = client.get('/user/auth/', {
      'email': 'johndoe@example.com',
      'password': 'password1'
    })
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(content['status'], 'OK')
    return

  def test_user_uniqueness(self):
    # Create user
    client = Client()
    response = client.post('/user/create/', {
      'email': 'johndoe@example.com',
      'password': 'password1',
      'first_name': 'John',
      'last_name': 'Doe'
    })
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(content['status'], 'OK')
    # Create user
    client = Client()
    response = client.post('/user/create/', {
      'email': 'johndoe@example.com',
      'password': 'password1',
      'first_name': 'John',
      'last_name': 'Doe'
    })
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(content['status'], 'FAIL')
    return

class CampaignTestCase(TestCase):

  def setUp(self):
    User.objects.create_user('johndoe@example.com', 'John', 'Doe', 'password1')
    self.client = Client()
    self.client.get('/user/auth/', {
      'email': 'johndoe@example.com',
      'password': 'password1'
    })
    return

  def test_create_edit_delete(self):
    # Create
    response = self.client.post('/campaigns/', json.dumps({
      'name': 'Test Campaign',
      'description': 'Campaign description'
    }), content_type = 'application/json')
    self.assertEqual(response.status_code, 201)
    content = json.loads(response.content)
    self.assertTrue(content.has_key('id'))
    id = str(content['id'])
    self.assertEqual(content['name'], 'Test Campaign')
    self.assertEqual(content['description'], 'Campaign description')
    # Edit
    response = self.client.post('/campaigns/' + id + '/', json.dumps({
      'name': 'Renamed Campaign',
      'description': 'Another description'
    }), content_type = 'application/json')
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(content['name'], 'Renamed Campaign')
    self.assertEqual(content['description'], 'Another description')
    # Delete
    response = self.client.delete('/campaigns/' + id + '/')
    self.assertEqual(response.status_code, 204)
    self.assertTrue(not Campaign.objects.filter(id = id).exists())
    return

class TierTestCase(TestCase):

  def setUp(self):
    User.objects.create_user('johndoe@example.com', 'John', 'Doe', 'password1')
    self.client = Client()
    self.client.get('/user/auth/', {
      'email': 'johndoe@example.com',
      'password': 'password1'
    })
    response = self.client.post('/campaigns/', json.dumps({
      'name': 'Test Campaign',
      'description': 'Campaign description'
    }), content_type = 'application/json')
    content = json.loads(response.content)
    self.campaign = str(content['id'])
    return

  def test_create_edit_delete(self):
    # Create
    response = self.client.post('/tiers/', json.dumps({
      'campaign': self.campaign,
      'name': 'Golden tier',
      'description': 'Golden tier description',
      'price': 200000
    }), content_type = 'application/json')
    self.assertEqual(response.status_code, 201)
    content = json.loads(response.content)
    self.assertTrue(content.has_key('id'))
    id = str(content['id'])
    # Edit
    response = self.client.post('/tiers/' + id + '/', json.dumps({
      'campaign': self.campaign,
      'name': 'Silver tier',
      'description': 'Silver tier description',
      'price': 100000
    }), content_type = 'application/json')
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(content['name'], 'Silver tier')
    self.assertEqual(content['description'], 'Silver tier description')
    self.assertEqual(content['price'], 100000)
    # Delete
    response = self.client.delete('/tiers/' + id + '/')
    self.assertEqual(response.status_code, 204)
    self.assertTrue(not Tier.objects.filter(id = id).exists())
    return

class InkindTestCase(TestCase):

  def setUp(self):
    User.objects.create_user('johndoe@example.com', 'John', 'Doe', 'password1')
    self.client = Client()
    self.client.get('/user/auth/', {
      'email': 'johndoe@example.com',
      'password': 'password1'
    })
    response = self.client.post('/campaigns/', json.dumps({
      'name': 'Test Campaign',
      'description': 'Campaign description'
    }), content_type = 'application/json')
    content = json.loads(response.content)
    self.campaign = str(content['id'])
    return

  def test_create_edit_delete(self):
    # Create
    response = self.client.post('/inkinds/', json.dumps({
      'campaign': self.campaign,
      'name': 'Gift certificate',
      'description': 'Gift certificate you can donate'
    }), content_type = 'application/json')
    self.assertEqual(response.status_code, 201)
    content = json.loads(response.content)
    self.assertTrue(content.has_key('id'))
    id = str(content['id'])
    # Edit
    response = self.client.post('/inkinds/' + id + '/', json.dumps({
      'campaign': self.campaign,
      'name': 'Store voucher',
      'description': 'Store voucher you can provide'
    }), content_type = 'application/json')
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(content['name'], 'Store voucher')
    self.assertEqual(content['description'], 'Store voucher you can provide')
    # Delete
    response = self.client.delete('/inkinds/' + id + '/')
    self.assertEqual(response.status_code, 204)
    self.assertTrue(not Inkind.objects.filter(id = id).exists())
    return

class PromptTestCase(TestCase):

  def setUp(self):
    User.objects.create_user('johndoe@example.com', 'John', 'Doe', 'password1')
    self.client = Client()
    self.client.get('/user/auth/', {
      'email': 'johndoe@example.com',
      'password': 'password1'
    })
    response = self.client.post('/campaigns/', json.dumps({
      'name': 'Test Campaign',
      'description': 'Campaign description'
    }), content_type = 'application/json')
    content = json.loads(response.content)
    self.campaign = str(content['id'])
    response = self.client.post('/tiers/', json.dumps({
      'campaign': self.campaign,
      'name': 'Golden tier',
      'description': 'Golden tier description',
      'price': 200000
    }), content_type = 'application/json')
    content = json.loads(response.content)
    self.tier = str(content['id'])
    response = self.client.post('/inkinds/', json.dumps({
      'campaign': self.campaign,
      'name': 'Gift certificate',
      'description': 'Gift certificate you can donate'
    }), content_type = 'application/json')
    content = json.loads(response.content)
    self.inkind = str(content['id'])
    return

  def test_send_emails(self):
    response = self.client.post('/campaigns/send_emails/', json.dumps({
      'campaign': self.campaign,
      'emails': [
        'a@example.com',
        'b@example.com',
        'c@example.com'
      ]
    }), content_type = 'application/json')
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content)
    self.assertEqual(len(content), 3)
    return