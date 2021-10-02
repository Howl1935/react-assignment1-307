import React, { useState, useEffect } from 'react'
import Table from './Table'
import Form from './Form'
import axios from 'axios'


function MyApp() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetchAll().then( result => {
      if(result)
        setCharacters(result);
    });
  }, []);

  async function fetchAll(){
    try {
      const response = await axios.get('http://localhost:5000/users')
      return response.data.users_list
  
    }catch(error){
      //we're actually not catching errors... just logging to console
      console.log(error)
      return false
    }
  }

  async function makePostCall(person){
    try{
      const response = await axios.post('http://localhost:5000/users', person)
      return response
    }catch(error){
      console.log(error)
      return false
    }
  }

  async function removeOneCharacter(id) {

  try{
    const response = await axios.delete('http://localhost:5000/users/' + id)
    if(response.status === 204)
    {
      console.log('success!')
      const updated = characters.filter((character) => {
        //console.log(character.id)
        return character.id !== id
      });
      setCharacters(updated);
    }else{
      console.log('No user deleted')
    }
  }catch(error)
  { 
    console.log(error)
    return false;
  }

  
  }

  function updateList(person) {
    makePostCall(person).then( result => {
      if(result.status === 201)
      setCharacters([...characters, result.data])
    })
  }

  return (
  <div className="container">
      <Table characterData={ characters }  removeCharacter={ removeOneCharacter } />
      <Form handleSubmit={ updateList } />
  </div>
);  

}

export default MyApp;




