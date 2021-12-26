class Engine {
    constructor(objects) {
        this.objects = objects;
        this.count = 0;
        this.FPS = 60;
        this.lastUpdate = Date.now();
        this.m = 0;
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
            var now = Date.now();
            var elapsed = now - this.lastUpdate;
            this.m += elapsed;
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
        console.log("Update");
    }

    Render(delta) {
    }

    addCallback(callback) {
        this.callback = callback;
    }

}


var engine = new Engine();
engine.addCallback(function(engine){
    console.log(this.count * this.FPS);
});
engine.Loop();
