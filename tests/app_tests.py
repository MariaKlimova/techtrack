import unittest



import sys
sys.path.insert(0,"/home/maria/quack")


from app import app
from flask import jsonify

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def dumps(self):
        rv = self.app.get('/')
        self.assertEqual( 200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)
        #pass
    def test_form(self):
        rv = self.app.post('/form/', data={ 'first_name':"Jesse",'last_name':"Pinkman"})
        self.assertEqual(b'{"first_name":"Jesse","last_name":"Pinkman"}\n',rv.data)

    def test_chats(self):
        rv = self.app.get('/chats/')
        
        self.assertEqual( 200, rv.status_code)
        self.assertEqual( "application/json", rv.mimetype)
        self.assertEqual(b'{"chats":["a","b","c"],"mimetype":"application/json","status_code":"200 OK"}\n', rv.data)
        
        rv = self.app.post();
        self.assertEqual(405, rv.status_code)     
       
 
    def test_contacts(self):
        rv = self.app.get('/contacts/')
        
        self.assertEqual( 200, rv.status_code)
        self.assertEqual( "application/json", rv.mimetype)
        self.assertEqual(b'{"contacts":["1","2","3"],"mimetype":"application/json","status_code":"200 OK"}\n', rv.data)

        rv = self.app.post('/contacts/');
        self.assertEqual(405, rv.status_code)
          
    def test_new_chat(self):
        rv = self.app.post('/new_chat/', data={'chat':'my'})
        
        self.assertEqual(b'{"chat":"my"}\n', rv.data)
        self.assertEqual( 200, rv.status_code)
        self.assertEqual( "application/json", rv.mimetype)

    def test_login(self):
        rv = self.app.post('/login/', data={'login':"1", 'password': "123"});
        self.assertEqual(b'{"final":"correct","mimetype":"application/json","status_code":"200 OK"}\n', rv.data) 
        self.assertEqual( 200, rv.status_code)
        self.assertEqual( "application/json", rv.mimetype)

        rv = self.app.post('/login/', data={'login':"1", 'password': "1d23"});
        self.assertEqual(b'{"final":"wrong password","mimetype":"application/json","status_code":"200 OK"}\n', rv.data)
        self.assertEqual( 200, rv.status_code)
        self.assertEqual( "application/json", rv.mimetype)

    

    def tearDown(self):
        pass
        
 
    class JSONRPCTEST( unittest.TestCase):
        def setUp(self):
            self.app = app.test_client()

        def test_get_name(self):
            rv = self.app.post('/api/', data={'jsonrpc': '2.0', 'method': 'print_name', 'params': [], 'id': 1})
            self.assertEqual('', rv.data)

if __name__ == "__main__":
    unittest.main()
