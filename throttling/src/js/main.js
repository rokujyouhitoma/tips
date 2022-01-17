class ExDate {
    now() {
        return Date.now();
    }
}


class TokenBucket {
    constructor(date, hearing_time, max_token) {
        this.date = date;
        var now = date.now();
        this.hearing_time = hearing_time;
        this.B = max_token;
        this.b = max_token;
        this.instanciated_at = now;
        this.last_updated_at = now;
    }

    hearing() {
        var now = this.date.now();
        var delta = now - this.last_updated_at;
        var v = Math.round(delta / this.hearing_time);
        if (0 < v && this.b < this.B) {
            this.b = (this.b + v < this.B) ? this.b + v : this.B;
            this.last_updated_at = now;
        }
    }

    remove_token(n) {
        this.hearing();
        if (0 <= this.b - n) {
            this.b -= n;
            return true;
        }
        return false;
    }
}

var token_bucket = new TokenBucket(new ExDate(), 100, 100);

var h1 = document.createElement("h1")
document.body.appendChild(h1);


var button = document.createElement("button")
button.innerText = "hi";
button.addEventListener("click", function(){
    token_bucket.remove_token(10);
    console.log(token_bucket.b);
});
document.body.appendChild(button);
