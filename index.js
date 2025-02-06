document
  .getElementById("comicForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    // Gather the form data
    let introduction = document.getElementById("introduction").value;
    let storyline = document.getElementById("storyline").value;
    let climax = document.getElementById("climax").value;
    let moral = document.getElementById("moral").value;

    // Make POST request to the Google Colab API
    let response = await fetch(
      "https://a2e6-34-105-29-63.ngrok-free.app/generate_comic",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ introduction, storyline, climax, moral }),
      }
    );

    // Get the response data
    let data = await response.json();

    // Display the images
    document.getElementById("comicOutput").innerHTML = data.images
      .map((img) => `<img src="${img}" alt="Generated Comic Image">`)
      .join("");
  });
