const functions = require("./functions");

// test('2 add 2 is equal to 4', () => {
//     expect(functions.add(2, 2)).toBe(4)
// });

// test('2 add 2 is not equal to 5', () => {
//     expect(functions.add(2, 2)).not.toBe(5)
// });

// test('isNull should be null',()=>{
//     expect(functions.isNull()).toBeNull()
// })

// test("should is falsy", () => {
//   expect(functions.checkValue(null)).toBeFalsy();
// });

// test('create user should return first name and last name', () => {
//     expect(functions.createUser()).toEqual({firstname:'Sherry', lastname:'Eric'})
// })


// // less than 1600

// test('total is less than 1600', ()=>{
//     const load1 = 800,
//     load2 = 500;
//     expect(load1+load2).toBeLessThan(1600)
// })

// //Regex

// test('no I in team', ()=>{
//     expect('teiam').not.toMatch(/T/);
// })
// promise
// test('the first usr is "Leanne Graham"',()=>{
//     expect.assertions(1);
//     //a callback actually got called.
//     return functions.fetchUsr().then(data=>
//         expect(data.name).toBe('Leanne Graham'))
// })

//Async Await
test('the first usr is "Leanne Graham"',async ()=>{
    expect.assertions(1);
    //a callback actually got called.
    const data =  await functions.fetchUsr();
    expect(data.name).toEqual('Leanne Graham')
})

