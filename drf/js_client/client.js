const loginFrom = document.getElementById('login-form')
const baseEndpoint = "http://127.0.0.1:8000/api"

if(loginFrom){
    //handle this login form
    loginFrom.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`

    let loginFromData = new FormData(loginFrom)
    let loginObjectData = Object.fromEntries(loginFromData)
    console.log(loginObjectData)

    const options = {
        method : "POST",
        headers : {
            "ContentType" : "application/json"
        },
        body : JSON.stringify(loginObjectData)
    }

    fetch(loginEndpoint, options)

    .then(response =>{
        console.log(response)
        return response.json()
    })

    .then(x =>{
        console.log(x)
    })

    .catch(error =>{
        console.log(error)
    }

    )
}