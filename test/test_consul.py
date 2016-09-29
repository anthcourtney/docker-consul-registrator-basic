import consul
import pytest

def services(host):
  c = consul.Consul(host=host)
  index, services = c.catalog.services()
  return services

def test_redis_registration():
  assert services('consul').has_key('redis') == True

def test_fake_service_registration():
  assert services('consul').has_key('fake_service') == False
