const sections = document.querySelectorAll('section')
const bubble = document.querySelector('.bubble')
const gradients = [
    'linear-gradient(to right top,#348F50,#56B4D3)',
    'linear-gradient(to right top,#f46b45,#eea849)',
    'linear-gradient(to right top,#6441A5,#2a0845)'
]

const options = {
    threshod : .7
}

let observer = new IntersectionObserver(navCheck, options)

function navCheck(entries){
    entries.forEach(entry => {
        const className = entry.target.className;
        const activeAnchor = document.querySelector(`[data-page=${className}]`)
    })
}

sections.forEach(section => {
    observer.observe(section)
})