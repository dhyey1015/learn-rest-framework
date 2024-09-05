const contentContainer = document.getElementById('content-container')
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
    let bodyyy= JSON.stringify(loginObjectData)

    const options = {
        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body : bodyyy
    }

    fetch(loginEndpoint, options)

    .then(response =>{
        return response.json()
    })

    .then(authData => {
        handleAuthData(authData, getProductList)
    })

    .catch(error =>{
        console.log(error)
    }
    )
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)

    if (callback){
        callback()
    }

}

function writeToContainer(data){
    if (contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4)+ "</pre>" 
    }
}

function getFetchOptions(method, body){
    return {
        method : method === null ? "GET": method,
        headers : {
            "Content-Type" : "application/json",
            "Authorization" : `Bearer ${localStorage.getItem('access')}`
        },
        body : body ? body : null
    }
}

function isTokenNotvalid(jsonData){
    if (jsonData.code && jsonData.code === "token_not_valid"){
        alert("please login again")
    }
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()
    
    fetch(endpoint, options)
    .then(response => {
        return response.json()
    })
    .then(data =>{
        console.log(data)
        const validData = isTokenNotvalid(data)
        if (validData)
        writeToContainer(data)
    })
}
