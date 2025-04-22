async function get_weather(id) {
    let response = await fetch("http://localhost:8000/api/weather/" + id);
    if (response.ok) {
        let json = await response.json();
        return json;
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function update_form() {
    let params = new URLSearchParams(document.location.search);
    let id = params.get("id");
    if (id == null) {
        document.getElementById("_button").innerText = "Добавить";
        document.getElementById("_button").onclick = add_weather;
        return;
    }
    document.getElementById("_button").innerText = "Редактировать";
    document.getElementById("_button").onclick = edit_weather;
    let weather = await get_weather(id); 
    document.getElementById("city").value = weather["city"];
    document.getElementById("Temperature").value = weather["Temperature"];
    document.getElementById("falllout").value = weather["falllout"];
    document.getElementById("photo").value = weather["photo"];
}

async function edit_weather() {
    let params = new URLSearchParams(document.location.search);
    let id = params.get("id");
    let response = await fetch("http://localhost:8000/api/weather/" + id, {
        method: "PUT",
        body: new FormData(document.getElementById("weather_form"))
    });
    if (response.ok) {
        window.location = "./";
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function add_weather() {
    let response = await fetch("http://localhost:8000/api/weather", {
        method: "POST",
        body: new FormData(document.getElementById("weather_form"))
    });
    if (response.ok) {
        window.location = "./";
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

update_form();