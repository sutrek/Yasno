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
    let template = `
    <div class="card mb-3" style="max-width: 540px;">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="{КАРТИНКА}" class="img-fluid rounded-start" alt="Photo">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{ГОРОД}</h5>
        <p class="card-text">{ПОГОДА}</p>
        <p class="card-text"><small class="text-body-secondary">{ПОСЛЕДНЕЕОБНОВЛЕНИЕ}</small></p>
      </div>
    </div>
  </div>
</div>`;

    let weather = await get_weather();
    let container = document.getElementById("weather");
    weather.forEach(element => {
        let weather = template
            .replace("{ГОРОД}", element.name)
            .replace("{ПОГОДА}", element.description)
            .replace("{КАРТИНКА}", element.photo)
            .replace("{ПОСЛЕДНЕЕОБНОВЛЕНИЕ}", element.DCF);  
        container.innerHTML += weather;
    });
}

render_weather();