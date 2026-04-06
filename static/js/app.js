document.querySelectorAll(".flash").forEach((item) => {
    setTimeout(() => {
        item.style.opacity = "0";
        item.style.transform = "translateY(-4px)";
    }, 3200);
});

const mobileMenuToggle = document.querySelector(".mobile-menu-toggle");
const mobileMenuPanel = document.querySelector(".mobile-menu-panel");

if (mobileMenuToggle && mobileMenuPanel) {
    mobileMenuToggle.addEventListener("click", () => {
        const isOpen = mobileMenuToggle.classList.toggle("is-open");
        mobileMenuPanel.hidden = !isOpen;
        mobileMenuToggle.setAttribute("aria-expanded", String(isOpen));
    });
}
