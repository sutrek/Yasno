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
    let template = '<tr>'
        + '<th scope="row">{id}</th>'
        + '<td>{ГОРОД}</td>'
        + '<td>{ПОГОДА}</td>'
        + '<td>{ОСАДКИ}</td>'
        + '<td><img src="{КАРТИНКА}" width="50px" class="img-fluid rounded-start" alt="..."></td>'
        + '<td>'
        + '<button class="btn btn-danger me-2" onclick="delete_weather({id})"><img src="/static/assets/buttondel.png" alt=""></button>'
        + '<a class="btn btn-warning" href="form.html?id={id}"><img src="/static/assets/buttonedit.png" alt=""></a>'
        + '</td>'
        + '</tr>'


    let weather = await get_weather();
    let container = document.getElementById("weather");
    weather.forEach(element => {
        let weather = template
        .replaceAll("{id}", element.id)
        .replace("{ГОРОД}", element.city)
         .replace("{ПОГОДА}", element.Temperature)
         .replace("{ОСАДКИ}", element.falllout)
         .replace("{КАРТИНКА}", element.photo)
        container.innerHTML += weather;
    });
}

render_weather();

async function delete_weather(id) {
    let response = await fetch("http://localhost:8000/api/weather/" + id, { "method": "DELETE" })

    if (response.ok) {
        window.location.reload();
    } else {
        alert("Ошибка HTTP: " + response.status)
    }
}