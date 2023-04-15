// Show one page and hide the two others
function showpage(page) {

    // Hide all of the divs:
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });

    // Show the div provided in the argument:
    document.querySelector(`#${page}`).style.display = 'block';

}

// Wait for the page to  load:
document.addEventListener('DOMContentLoaded',  () => {

    // Select all buttons: 
    document.querySelectorAll('button').forEach(button => {

        // When a button is clicked, switch to that page:
        button.onclick = function(){
            showpage(this.dataset.page);
        };

    })

});