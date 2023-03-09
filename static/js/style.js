let button = document.querySelector('.del')

function show() {
    prompt('Уверен? ')
}

for (let i in button) {
    button[i].onclick = function () {
        show();
    }
}


$(document).ready(function() {
    $('.js-example-basic-single').select2();
    $('.js-example-basic-multiple').select2();
});

