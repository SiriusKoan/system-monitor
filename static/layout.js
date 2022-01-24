function show(id) {
    for (var i = 0; i < document.getElementById("canvas").children.length; i++) {
        if (document.getElementById("canvas").children[i].id != id) {
            document.getElementById("canvas").children[i].style.display = "none";
        }
        else {
            document.getElementById("canvas").children[i].style.display = "block";
        }
    }
}