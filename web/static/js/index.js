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
  const UpBtn = document.querySelector("#arrow_button_up");
  const newsBlock = document.querySelector(".news_concept");
  const mainPage = document.querySelector(".main-page");

  downBtn.addEventListener("click", () => {
    newsBlock.scrollIntoView({
      behavior: "smooth",
    });
  });

  UpBtn.addEventListener("click", () => {
    mainPage.scrollIntoView({
      behavior: "smooth",
    });
  });

  document.querySelectorAll(".has-submenu").forEach(function (item) {
    item.addEventListener("click", function (e) {
      if (e.target.closest(".submenu")) return;

      document
        .querySelectorAll(".has-submenu.open")
        .forEach(function (openItem) {
          if (openItem !== item) {
            openItem.classList.remove("open");
          }
        });

      item.classList.toggle("open");

      e.stopPropagation();
    });
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".has-submenu")) {
      document
        .querySelectorAll(".has-submenu.open")
        .forEach(function (openItem) {
          openItem.classList.remove("open");
        });
    }
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
