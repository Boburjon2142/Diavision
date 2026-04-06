document.querySelectorAll(".flash").forEach((item) => {
    setTimeout(() => {
        item.style.opacity = "0";
        item.style.transform = "translateY(-4px)";
    }, 3200);
});
