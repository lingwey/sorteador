// genera ventana emergente con ganador
document.addEventListener("DOMContentLoaded", function() {
    const modalElement = document.getElementById('modalGanador');
    
    if (modalElement && modalElement.dataset.ganador === "true") {
        const myModal = new bootstrap.Modal(modalElement);
        myModal.show();

        // Limpia los parámetros de la URL para que al recargar no salga el modal de nuevo
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});