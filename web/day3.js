let myname="Riya"
let age=20
const college="AIML"

function sayhello(){
  let output=document.getElementById("output")
  output.innerHTML=`Hello! I am ${myname},${age} years old.<br>
                    Studying ${college}.`
}

function showAge(){
  let output=document.getElementById("output")
  let a=15
  let b=4
  output.innerHTML=`Current age:${age} <br>
                    In 5 years:${age+5}<br>
                    Birth Year:${2025-age}  `
}

function calculate(){
  let output=document.getElementById("output")
  let a=15
  let b=4
  output.innerHTML=`
    ${a}+${b}=${a+b} <br>
    ${a}-${b}=${a-b} <br>
    ${a}*${b}=${a*b} <br>
    ${a}/${b}=${(a/b).toFixed(2)}
    `
}

function changeColor(){
  let colors=["#0f0f0f","#1a0a2e,","#0a1628","#1a1a0a"]
  let random=colors[Math.floor(Math.random()*colors.length)]
  document.body.style.backgroundColor=random
  document.getElementById("output").innerHTML=`Background changed to ${random}`
}