const Http = new XMLHttpRequest();
const url='/api/organizations/my/';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText);  // => получим массив данных в формате JSON
}