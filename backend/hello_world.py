from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import string
import random

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}
def randomId():
  alphabet_string = string.ascii_lowercase
  alphabet_list = list(alphabet_string)
  prefix = ''
  for x in range(3):
      prefix += alphabet_list[random.randint(0,25)]
  suffix = '' 
  for x in range(3):
   suffix += str(random.randint(0,9))
   

  return prefix + suffix



@app.route('/')
def get_user_list():
   return users

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_jobname = request.args.get('job')  
      if search_username and search_jobname:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_jobname:
               subdict['users_list'].append(user)
      elif search_username:
         subdict = { 'users_list' : [] }
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)         
      elif search_jobname:
         subdict = { 'users_list' : [] }
         for user in users['users_list']:
            if user['job'] == search_jobname:
               subdict['users_list'].append(user)             
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id']=randomId()     
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
   
   if request.method == 'DELETE':
      resp = jsonify()
      for user in users['users_list']:
         if user['id'] == id:
            users['users_list'].remove(user)
            resp.status_code = 204
            return resp
   resp.status_code = 404
   return resp
   

   
      
         
  
