var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        if (e.target.className == "fold-button folded") {
            e.target.innerHTML = "свернуть";
            e.target.className = "fold-button";
            var displayState = "block";
        } else {
            e.target.innerHTML = "развернуть";
            e.target.className = "fold-button folded";
            var displayState = "none";
        }
        event.target
            .parentElement
            .getElementsByClassName('articlein')[0]
            .style.display = displayState;
    });
    foldBtns[i].addEventListener("click", function(event) {
        console.log("you clicked ", event.target);
    });
}

