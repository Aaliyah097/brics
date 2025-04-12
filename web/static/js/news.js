document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".news-view__setting__list").forEach((list) => {
    list.addEventListener("click", (e) => {
      if (e.target.tagName !== "LI") return;

      list.querySelectorAll("li").forEach((item) => {
        item.classList.remove("active-item");
      });

      e.target.classList.add("active-item");
    });
  });
});

function openNews(id) {
  const url = `/news/${id}/`;
  window.open(url, "_blank");
}
