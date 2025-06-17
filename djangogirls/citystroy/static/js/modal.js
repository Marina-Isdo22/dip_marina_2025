const modal = document.getElementById('modal-profile')
const modalClose = document.getElementById('modal-close')
const modalOverlay = document.getElementById('modal-overlay')
const profileModalBtn = document.getElementById('profile')

profileModalBtn.addEventListener('click', e => {
    const classList = modal.classList;

    console.log(classList);
    if (classList.contains('modal-active')) {
        modal.classList.remove('modal-active');
    } else {
        modal.classList.add('modal-active');
    }
})

modalClose.addEventListener('click', e => {
    modal.classList.remove('modal-active')
})

modalOverlay.addEventListener('click', e => {
    modal.classList.remove('modal-active')
})