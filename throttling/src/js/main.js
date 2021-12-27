class ExDate {
    now() {
        return Date.now();
    }
}

class Engine {
    constructor(date) {
        var now = date.now();
        this.Date = date;
        this.count = 0;
        this.FPS = 60;
        this.instanciateAt = now;
        this.lastUpdate = now;
        this.callback = null;
    }

    Loop() {
        var lag = 0;
        const MPU = 1000 / this.FPS;
        const LIMIT_LAG = 1000 * MPU;
        var loop = function(){
            if(0 <= this.count){
                setTimeout(loop, MPU);
                this.count++;
            }
            var now = this.Date.now();
            var elapsed = now - this.lastUpdate;
            this.lastUpdate = now;
            lag += elapsed;
            if(LIMIT_LAG < lag){
                lag = 0;
                return;
            }
            while(MPU <= lag){
                this.Update();
                lag -= MPU;
            }
            this.Render(lag / MPU);
            if (this.count % this.FPS === 0) {
                this.callback(this);
            }
        }.bind(this);
        this.Start();
        loop();
    }

    Start() {
        console.log("Start");
    }

    Update() {
        //console.log("Update");
    }

    Render(delta) {
    }

    addCallback(callback) {
        this.callback = callback;
    }

}


// main
var h1 = document.createElement("h1")
document.body.appendChild(h1);

var engine = new Engine(new ExDate());
engine.addCallback(function(engine){
    //var value = this.count * this.FPS;
    var value = this.lastUpdate - this.instanciateAt;
    console.log(value);
    h1.innerText = value;
});
engine.Loop();
