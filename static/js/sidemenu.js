window.addEventListener("DOMContentLoaded", () => {
    let mediaQuery = window.matchMedia("(max-width: 720px)")

    if (mediaQuery.matches) {
        toggleSideMenu()
    }

})

const toggleSideMenu = () => {

    const sideMenuContent = document.querySelector("#side_menu")
    console.log(sideMenuContent)

    sideMenuContent.parentElement.textContent = ''
    document.querySelector("#sidebar-content").innerHTML = sideMenuContent.innerHTML
}


/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
