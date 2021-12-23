console.log("main");

var Engine = function(objects){
    this.objects = objects;
    this.count = 0;
    this.FPS = 60;
    this.lastUpdate = Date.now();
    this.m = 0;
    this.callback = null;
};

Engine.prototype.Loop = function(){
    var lag = 0;
    var MPU = 1000 / this.FPS;
    var LIMIT_LAG = 1000 * MPU;
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
};

Engine.prototype.Start = function(){
    console.log("Start");
};

Engine.prototype.Update = function(){
    console.log("Update");
};

Engine.prototype.Render = function(delta){

};

Engine.prototype.addCallback = function(callback){
    this.callback = callback;
};


var engine = new Engine();
engine.addCallback(function(engine){
    console.log(this.count * this.FPS);
});
engine.Loop();
