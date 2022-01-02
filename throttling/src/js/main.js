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
        this.instanciatedAt = now;
        this.lastUpdatedAt = now;
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
            var elapsed = now - this.lastUpdatedAt;
            this.lastUpdatedAt = now;
            lag += elapsed;
            if(LIMIT_LAG < lag){
                lag = 0;
                return;
            }
            while(MPU <= lag){
                this.OnUpdate();
                lag -= MPU;
            }
            this.OnRender(lag / MPU);
            if (this.count % this.FPS === 0) {
                this.callback(this);
            }
        }.bind(this);
        this.OnStart();
        loop();
    }

    OnStart() {
        console.log("Start");
    }

    OnUpdate() {
    }

    OnRender(delta) {
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
    var value = this.lastUpdatedAt - this.instanciatedAt;
    console.log(value);
    h1.innerText = value;
});
engine.Loop();
