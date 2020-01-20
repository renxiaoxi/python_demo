const reversestring = require('./reversestring.js')

test('string should be reversed',()=>{
    expect(reversestring('hEllo')).toBe('olleh')
})

test('reversestring exists',() => {
    expect(reversestring).toBeDefined()
});