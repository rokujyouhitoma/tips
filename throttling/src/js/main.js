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
        var hearing_token = delta % this.hearing_time;
        console.log(hearing_token);
        if (this.token + hearing_token <= this.b) {
            this.token += hearing_token;
            this.last_updated_at = now;
        } else if (this.token + hearing_token > this.b) {
            this.token = this.b;
            this.last_updated_at = now;
        }
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

var token_bucket = new TokenBucket(new ExDate(), 2, 100);

var h1 = document.createElement("h1")
document.body.appendChild(h1);


var button = document.createElement("button")
button.innerText = "hi";
button.addEventListener("click", function(){
    token_bucket.remove_token(10);
    console.log(token_bucket.token);
});
document.body.appendChild(button);
