function Main() {
    var stats = document.getElementsByClassName('status');
    stats = Array.from(stats)
    function ChangeColor(element) {
        if (element.innerText == 'blocked') {
            console.log('okdas');
            
            element.style.color = 'red';
        } else {
            element.style.color = 'green';
        }
    }
    stats.forEach(ChangeColor)
};

Main();

