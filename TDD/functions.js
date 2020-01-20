const axios = require('axios')

const functions = {
    add:(num1, num2) => num1 + num2,
    isNull:() => null,
    checkValue: x => x,
    createUser:()=>{
        const usr = {firstname:'Sherry'}
        usr['lastname'] = 'Eric';
        return usr
    },
    fetchUsr:()=>
        axios.get('https://jsonplaceholder.typicode.com/users/1').then(res=>res.data).catch(err=>err)
    
}

module.exports = functions

