class Tape {
    constructor(commands) {
        this.counter = 0;
        this.commands = commands;
    }
    add(v) {
        if (0 <= this.counter && this.counter < this.commands.length) {
            this.counter = (this.commands[this.counter] == v) ? this.counter + 1 : 0;
        } else {
            this.counter = 0;
        }
    }
    isAccept() {
        return this.counter === this.commands.length;
    }
}
const tape = new Tape([38,38,40,40,37,39,37,39,66,65,13]);
document.addEventListener('keydown', (event) => {
    tape.add(event.keyCode);
    if (tape.isAccept()){
        var img = document.createElement("img");
        img.src = "https://pbs.twimg.com/profile_images/206948941/wall-e_400x400.jpg";
        img.height = 100;
        img.width = 100;
        document.body.appendChild(img);
        setTimeout(function(){
            img.parentNode.removeChild(img);
        }, 1000);
    }
}, false);
