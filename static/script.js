const iconCloseBtnError = document.querySelector('#icon-close-error')
const iconCloseBtnSuccess = document.querySelector('#icon-close-success')
const messageBox = document.querySelector('.mensagens')

iconCloseBtnError.addEventListener('click', () => {
  messageBox.style.opacity = '0'
})

iconCloseBtnSuccess.addEventListener('click', () => {
  messageBox.style.opacity = '0'
})


