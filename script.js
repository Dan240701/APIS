const nombre = document.querySelector('#nombre');
const habilidades = document.querySelector('#habilidades');

fetch('https://pokeapi.co/api/v2/pokemon/pikachu')
.then(response => {
    if (!response.ok) {
        throw new Error('No se pudo establecer una conexión');
    }
    return response.json();
})
.then(data => {
    console.log(data);
    nombre.textContent = data.forms[0].name;
    habilidades.textContent = data.abilities[0].ability.name;
})
.catch(error => {
    console.error('El error es:', error);
    
})