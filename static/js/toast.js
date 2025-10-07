function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    /// Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-blue-50', 'border-blue-400', 'text-blue-700');
        toastComponent.style.border = '1px solid #60a5fa'; 
    } else if (type === 'error') {
        toastComponent.classList.add('bg-purple-50', 'border-purple-400', 'text-purple-700');
        toastComponent.style.border = '1px solid #a855f7'; 
    } else {
        toastComponent.classList.add('bg-slate-50', 'border-slate-300', 'text-slate-700');
        toastComponent.style.border = '1px solid #cbd5e1'; 
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
