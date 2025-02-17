document.addEventListener("DOMContentLoaded", function () {
            const menuToggle = document.getElementById("menu-toggle"); // Tlačítko hamburgeru
            const navLinks = document.getElementById("nav-links"); // Navigační seznam

            if (menuToggle && navLinks) {
                menuToggle.addEventListener("click", function () {
                    navLinks.classList.toggle("show"); // Přepínání třídy pro zobrazení/skrytí
                });
            } else {
                console.error("Hamburger menu nebo navigace nebyla nalezena!");
            }
        });