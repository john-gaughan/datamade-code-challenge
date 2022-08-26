/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

// function logFormContent() {
//    console.log(form.value);
// };
// const form = document.getElementById("address");
// form.addEventListener("input", (event) => {
//    event.preventDefault();
//    logFormContent();
// });

// for (var [key, value] of formData.entries()) { 
//   console.log(key, value);
// }

window.addEventListener("load", () => {
  var url = "api/parse/"
  const form = document.getElementById("address-form");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(form);
  });

  form.addEventListener('formdata', (e) => {
    const data = e.formData;
    for (const value of data.values()) {
      console.log(value)
    }
    const XHR = new XMLHttpRequest();
    XHR.addEventListener("load", (event) => {
      alert(event.target.responseText);
    });
    XHR.addEventListener("error", (event) => {
      log.textContext = `${log.textContext}${event.type}: ${event.message}\n`
    });

    XHR.open("GET", url);
    XHR.send(data);
  });
});
