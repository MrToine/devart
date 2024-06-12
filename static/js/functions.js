function hide(id) {
    let htmlChange = document.getElementById('show-' + id);
    htmlChange.style.display = "none";
    htmlChange.id = `hide-${id}`;
    let buttonChange = document.getElementById(id);
    buttonChange.onclick = function() { show(id); };
}

function show(id) {
    let htmlChange = document.getElementById('hide-' + id);
    htmlChange.style.display = "block";
    htmlChange.id = `show-${id}`;
    let buttonChange = document.getElementById(id);
    buttonChange.onclick = function() { hide(id); };
}