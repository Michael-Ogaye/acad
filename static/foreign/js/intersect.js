
let services=document.querySelectorAll('.features article')

let observer=new IntersectionObserver((entries,observer)=>{
    entries.forEach((entry,index)=>{
        if (entry.isIntersecting){

            setTimeout(()=>{
                entry.target.style.opacity='1'
                entry.target.style.transform='translateX(0)'
            
                    }, index*250)
            

        }
       
        
    })
},{threshold:0.5})

services.forEach((serv)=>{
    observer.observe(serv)
})