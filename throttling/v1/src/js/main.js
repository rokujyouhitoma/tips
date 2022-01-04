
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

class TokenBucket {
    constructor(max_token) {
        this.b = max_token;
        this.token = max_token;
    }

    add_token() {
        if (this.token < this.b) {
            this.token += 1;
            return true;
        }
        return false;
    }

    remove_token(n) {
        if (0 <= this.token - n) {
            this.token -= n;
            return true;
        }
        return false;
    }

    update() {
        return this.add_token();
    }
}

token_bucket = new TokenBucket(100);
console.log(token_bucket);

// main
var h1 = document.createElement("h1")
var h2 = document.createElement("h2")
var button = document.createElement("button");
button.innerText = "Consume 10 tokens";
button.addEventListener("click", function(){
    token_bucket.remove_token(10);
});
document.body.appendChild(h1);
document.body.appendChild(h2);
document.body.appendChild(button);

var engine = new Engine(new ExDate());
engine.addCallback(function(engine){
    token_bucket.update();
    h2.innerText = "tokens: " + token_bucket.token;

    var value = this.lastUpdatedAt - this.instanciatedAt;
    h1.innerText = "time:" + value;
});
engine.Loop();
