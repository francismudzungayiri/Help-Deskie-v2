let btns = document.querySelectorAll(".btn");
let panes = document.querySelectorAll(".pane");

btns.forEach((btn, index) => {
  btn.addEventListener("click", () => {
    btns.forEach((x) => {
      x.classList.remove("font-bold");
      x.classList.remove("border-l-4");
    });
    panes.forEach((content) => {
      content.classList.add("hidden");
    });

    btn.classList.add("border-l-4");
    btn.classList.replace("font-light", "font-bold");

    let targetTab = btn.getAttribute("data-tab");
    document.getElementById(targetTab).classList.remove("hidden");

    // checking if index is 0
    if (index == 0) {
      btn.classList.add("font-bold");
    }
  });
});

// ADD TEAM MEMBER MODAL
let user_btn = document.querySelector("#add-user-btn");
let user_modal = document.querySelector("#add-user-modal");
let close_modal = document.querySelector("#modal-close");

user_btn.addEventListener("click", () => {
  user_modal.classList.replace("hidden", "flex");
});
close_modal.addEventListener("click", () => {
  user_modal.classList.replace("flex", "hidden");
});
