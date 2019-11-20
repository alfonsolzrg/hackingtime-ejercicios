# Server assignment problem

# server_list = [1,2,3]
# create_server() -> 4
# server_list = [1,2,3,4]
# delete_server(2)
# server_list = [1,3,4]
# create_server() -> 2
# server_list = [1,2,3,4]


import unittest

class ServerAssigner():
  _servers = []
  
  def get_servers(self):
    return self._servers
  
  def create_server(self):
    pass

  def delete_server(self, pos):
    pass


class TestServerAssignment(unittest.TestCase):
  
  def test_server_assignment(self):
    # Add first test
    sa = ServerAssigner()
    server = sa.create_server()
    self.assertEqual(server, 1)
    
    server = sa.create_server()
    self.assertEqual(server, 2)
    
    server = sa.create_server()
    self.assertEqual(server, 3)
    
    sa.delete_server(2)
    
    server = sa.create_server()
    self.assertEqual(server, 2)
    
      
unittest.main()