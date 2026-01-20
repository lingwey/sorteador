// genera ventana emergente con ganador
document.addEventListener("DOMContentLoaded", function() {
    const modalElement = document.getElementById('modalGanador');
    
    if (modalElement && modalElement.dataset.ganador === "true") {
        const myModal = new bootstrap.Modal(modalElement);
        myModal.show();
    }
});