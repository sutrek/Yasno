async function get_weather() {
    let response = await fetch("http://localhost:8000/api/weather/all");
    if (response.ok) {
        let json = await response.json();
        return json;
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function render_weather() {
    let template =  `
    <tr>
       <th scope="row">{id}</th>
        <th scope="row">{ГОРОД}</th>
        <td>{ПОГОДА}</td>
        <td>{ОСАДКИ}</td>
        <td><img src="{КАРТИНКА}" width="75px" class="img-fluid rounded-start" alt="..."></td>
    </tr>`;
    let weather = await get_weather();
    let container = document.getElementById("weather");
    weather.forEach(element => {
        let weather = template
             .replace("{id}", element.id)
            .replace("{ГОРОД}", element.city)
            .replace("{ПОГОДА}", element.Temperature)
            .replace("{ОСАДКИ}", element.falllout)
            .replace("{КАРТИНКА}", element.photo)
        container.innerHTML += weather;
    });
}

render_weather();