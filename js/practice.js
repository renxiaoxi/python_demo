

console.log('trunkArr')

// let arr = [1,2,3,4,5,6,7]
// num = 3
// //console.log(arr.length)
// section = Math.ceil(arr.length / 3)
// //console.log(section)
// let newArr = []
// for(let i = 0; i < section; i++ ){
//     // newArr.push(arr.slice(i*num,))
//     newArr.push(arr.slice(i*num,num*(i+1)))
//     console.log(i*num,num*(i+1)-1)
// }
// // console.log(arr.slice(1,3))
// console.log(newArr)


// const trunkArr = (arr,num) => {
//     let trunk = Math.ceil(arr.length / num)
//     let newArr = []
//     for(let i=0; i<trunk; i++){
//         newArr.push(arr.slice(i*num, num*(i+1)))
//     }
//     return newArr
// }
//  let arr = [23,34,222,234,677,23,1234]
// // console.log(trunkArr(arr,5))


// let arr_a = [5,6,7,8];
// let arr_b = []
// arr_a.forEach(val=>{
//     console.log(val)
//     arr_b.push([val])
// })
// // for(let i=0;i<arr_a.length;i++){
// //     arr_b.push(arr_a[i])
// // }

// // arr1.push([2]);
// // arr1.push([3]);
// // console.log(arr_b)

// const arr_a = [[1,2],[3,4],5,6]
// const last_1 = [arr_a[arr_a.length-1]]
// console.log(last_1)
// last_1.push(5)
// console.log(arr_a)

// return false

const chunkArray = (arr, len) => {
    // Init chunked arr
    const chunkedArr = [];
  
    // Loop through arr
    arr.forEach((val,index) => {
      // Get last element
      console.log('\n')
      console.log('index',index)
      console.log('cArray_st1',chunkedArr)
      const last = chunkedArr[chunkedArr.length - 1];
        console.log('last_st1',last)
        console.log('cArray_st2-3',chunkedArr)
      // Check if last and if last length is equal to the chunk len
      if (!last || last.length === len) {
         // console.log('!',val)
        chunkedArr.push([val]);
        
        console.log('cArray_st2',chunkedArr)
      } else {
        //console.log('-',val)
        console.log('cArray_st2-4',chunkedArr)
        last.push(val);
        console.log('cArray_st2-5',chunkedArr)
        console.log('last_st2',last)
      }
      console.log('chunkedArr_final', chunkedArr)
      console.log('last_final', last)
    });
  
    return chunkedArr;
  };

  let arr = [1,2,3,4,5,6,7]
  console.log(chunkArray(arr,3))

return false
// var f = ({a:b} = {222:333}) => ({a:b})
// console.log(f())

// var f = ([a, b] = [1, 2], {x: c} = {x: a + b}) => a + b + c;
// console.log(f()); // 6
// let ab,ba

// ({ab,ba}={ab:1,ba:2})
// console.log(ab)

// var [ab,abb,abbb,...rest] = [1,2,3,5]
// console.log(ab)
let {name:sname}={fname:'sherry',name:'s'}
console.log(sname)

// const x = [1,2,3,4,5,6]
// const [y,z,...rest] = x;
// console.log(y)
// console.log(z)
// console.log(rest)

// let [sherry, eric] =  [2,3]
// [sherry, eric] = [eric, sherry]
// console.log(sherry)
// let [sherry, eric] = [188,288]
// setTimeout(()=>{
//     [sherry, eric] = [eric, sherry]
//     console.log(sherry)

// },1000)


return false;
// const object1 = {
//     property1: 42
//   };
  
//   object1[Symbol.unscopables] = {
//     property1: false
//   };
  
//   with (object1) {
//     console.log(property1);
//     // expected output: Error: property1 is not defined
//   }

// function f(){
//     return Array.from(arguments)
// }
// console.log(f(1,2,3))
// Since the array is initialized with `undefined` on each position,
// the value of `v` below will be `undefined`
// console.log(Array.from({length: 5}, (v, i) => i+''+v))

// const set = new Set(['12','s','c','12','as','s'])
// console.log(set)


// console.log(Array.of(7))
// console.log(Array(7))
// console.log(Array.isArray(Array.of(1,3,3)))
// console.log(Array.isArray(new Uint8Array(0)))

const fruits = ['apple','pear','banana','kiwi']
const food = ['vegetable','pork','meat','egg',...fruits]
console.log(food)



return false 

var arr2 = [1, 2, [3, 4, [5, 6]]];
arr2.flat();
console.log(arr2.flat().flat())

return false;
function a(arg){
    return Object.prototype.toString.call(arg)
}

console.log(a([12,34]))
x = new Array(1)
console.log(Object.prototype.toString(x))
console.log(x.prototype.toString())
return false

var favorite_person = ["Albert Camus", "WangYangming"]
// favorite_person.shift('hello')
// console.log(favorite_person)

favorite_person.splice(1,2,'aaa')
console.log(favorite_person)
favorite_person.push('Marx')
console.log(favorite_person)
favorite_person.unshift('good')
// good abbert camus aaa marx
console.log(favorite_person)
console.log(Object.keys(favorite_person))

console.log(Object.values(favorite_person))
console.log(Object.entries(favorite_person))

console.log('freeze now')
//Object.freeze(favorite_person)
favorite_person.push('bbb')
console.log(favorite_person)

return false
//break

// for argv
const argv = process.argv.slice(2)


//for different function
switch(argv[0]){
    case 'this':
        // method -> obj
        // function -> global (windows / global)
        const universe = {
            name:'sherry',
            powers : ['fire','water','wind'],
            showPower(){
                this.powers.forEach(function(power){  //function is global
                    console.log(this.name,power)
                    
                },this) // => universe
            }
        }

        universe.inputPower = function(){
            console.log(this)
        }



        universe.showPower()
        //universe.inputPower()

        function addition(title){
            this.title = title
            console.log(this)
        }
        addition()

        var operator = new addition('b') //obj
        console.log(process.argv)
        break;
    case 'array':
        console.log('show arrary')
        console.log('show array method: reduce')
        let powers = ['snow','rain','wind','shine','fog']
        let arr1 = arr.reduce((currentTotal,item)=>currentTotal[item]=1,0)
        console.log('The total of ARR1 is ', arr1)
    break;
    case 'scope':
            var xxx = 'aaa';
            (function(){
                console.log(typeof xxx)
                if(typeof xxx === 'undefined'){
                    var xxx = 'Jack'
                    console.log(xxx)
                }else{
                    console.log(xxx)
                }
            })()
    default:
        // global.globalString = 'sherry'
        // console.log(global)
        console.log('thank for using it, bye')
}












return false;

var a = [5, 4, 3, 2, 1];
console.log(a.concat(0).reverse().join(""))
// method -> obj
// function -> global (windows / global)

const universe = {
    name:'sherry',
    powers : ['fire','water','wind'],
    showPower(){
        this.powers.forEach(function(power){  //function is global
            console.log(this.name,power)
            
        },this) // => universe
    }
}

universe.inputPower = function(){
    console.log(this)
}



universe.showPower()
//universe.inputPower()

function addition(title){
    this.title = title
    console.log(this)
}
addition()

var operator = new addition('b') //obj
console.log(process.argv)



