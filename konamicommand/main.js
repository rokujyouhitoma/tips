class Tape {
    constructor(acceptors) {
        this.pointer = 0;
        this.acceptors = acceptors;
    }
    record(v) {
        if (0 <= this.pointer && this.pointer < this.acceptors.length && this.acceptors[this.pointer] === v) {
            this.pointer++;
        } else {
            this.reset();
        }
    }
    hasEnd() {
        return this.pointer === this.acceptors.length;
    }
    reset() {
        this.pointer = 0;
    }
}

// ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a', 'Enter'];
const tape = new Tape([38,38,40,40,37,39,37,39,66,65,13]);

function showImage() {
   var img = document.createElement("img");
   img.src = "https://pbs.twimg.com/profile_images/206948941/wall-e_400x400.jpg";
   img.height = 100;
   img.width = 100;
   document.body.appendChild(img);
   setTimeout(function(){
      img.parentNode.removeChild(img);
   }, 1000);
}

document.addEventListener("keydown", (event) => {
    tape.record(event.keyCode);
    if (tape.hasEnd()){
        tape.reset();
        showImage();
    }
}, false);
