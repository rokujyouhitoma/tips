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
        this.b = max_token;
        this.token = max_token;
        this.instanciated_at = now;
        this.last_updated_at = now;
    }

    hearing() {
        var now = this.date.now();
        var delta = now - this.last_updated_at;
        var v = delta % this.hearing_time;
        var hearing_token = (this.token + v > this.b) ?  this.b: this.token + v;
        this.token = hearing_token;
        this.last_updated_at = now;
    }

    remove_token(n) {
        this.hearing();
        if (0 <= this.token - n) {
            this.token -= n;
            return true;
        }
        return false;
    }
}

var token_bucket = new TokenBucket(new ExDate(), 16, 100);

var h1 = document.createElement("h1")
document.body.appendChild(h1);


var button = document.createElement("button")
button.innerText = "hi";
button.addEventListener("click", function(){
    token_bucket.remove_token(10);
    console.log(token_bucket.token);
});
document.body.appendChild(button);
