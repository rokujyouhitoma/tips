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
        this.instanciated_at = now;
        this.last_updated_at = now;
        this.callback = null;
    }

    start() {
        var lag = 0;
        const MPU = 1000 / this.FPS;
        const LIMIT_LAG = 1000 * MPU;
        var loop = function(){
            if(0 <= this.count){
                setTimeout(loop, MPU);
                this.count++;
            }
            var now = this.Date.now();
            var elapsed = now - this.lastUpdated_at;
            this.lastUpdated_at = now;
            lag += elapsed;
            if(LIMIT_LAG < lag){
                lag = 0;
                return;
            }
            while(MPU <= lag){
                this.update();
                lag -= MPU;
            }
            this.render(lag / MPU);
            if (this.count % this.FPS === 0) {
                this.callback(this);
            }
        }.bind(this);
        loop();
    }

    update() {
    }

    render(delta) {
    }

    add_callback(callback) {
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

// main
var h1 = document.createElement("h1")
document.body.appendChild(h1);

var engine = new Engine(new ExDate());
engine.add_callback(function(engine){
    var value = this.lastUpdated_at - this.instanciated_at;
    h1.innerText = "time:" + value;
});
engine.start();
