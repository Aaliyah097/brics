const Http = new XMLHttpRequest();
const url = "/api/organizations/my/";
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText); // => получим массив данных в формате JSON
};

document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".team_brics__finance_strange");
  const downBtn = document.querySelector("#arrow_button_down");
  const newsBlock = document.querySelector(".news_concept");

  downBtn.addEventListener("click", () => {
    newsBlock.scrollIntoView({
      behavior: "smooth",
    });
  });

  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const column = this.closest(".team_brics__column");
      column.classList.toggle("open");

      const content = column.querySelector(".container-finance");
      if (content) {
        if (column.classList.contains("open")) {
          content.style.maxHeight = content.scrollHeight + "px";
          content.style.opacity = "1";
        } else {
          content.style.maxHeight = "0";
          content.style.opacity = "0";
        }
      }
    });
  });
});
