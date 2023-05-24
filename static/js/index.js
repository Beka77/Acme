let btn = document.querySelector(".mobile-btn");
let body = document.querySelector("body");
const burgerFunc = (menuClassName, showClassName) => {
  let menu = document.querySelector(`.${menuClassName}`);

  if (menu.className.includes(showClassName)) {
    menu.className = menuClassName;
  } else {
    menu.className += ` ${showClassName}`;
  }
};
const backDropFunc = (menuClassName, showClassName) => {
  let menu = document.querySelector(`.${menuClassName}`);

  if (menu.className.includes(showClassName)) {
    menu.className = menuClassName;
  } else {
    menu.className += ` ${showClassName}`;
  }
};

btn.addEventListener("click", () => {
  burgerFunc("header__menu", "header__menu-show");
  backDropFunc("body", "on");
});
