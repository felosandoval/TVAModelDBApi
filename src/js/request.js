
//Consumiendo api con Axios, metodo get
axios.get('https://gorest.co.in/public/v1/users').then(response => {
    response.data.data.forEach(element => {
        console.log(element);
        
    });
    console.log(response.data.data)
})