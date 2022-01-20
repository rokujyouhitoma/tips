class ExDate {
    now() {
        return Date.now();
    }
}


class TokenBucket {
    constructor(date, hearing_time, b) {
        this.date = date;
        let now = date.now();
        this.hearing_time = hearing_time;
        this.MAX_B = b;
        this.b = b;
        this.last_updated_at = now;
    }

    hearing() {
        let now = this.date.now();
        let delta = now - this.last_updated_at;
        let v = Math.round(delta / this.hearing_time);
        if (0 < v && this.b < this.MAX_B) {
            this.b = (this.b + v < this.MAX_B) ? this.b + v : this.MAX_B;
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

let token_bucket = new TokenBucket(new ExDate(), 100, 100);

let h1 = document.createElement("h1")
document.body.appendChild(h1);


let button = document.createElement("button")
button.innerText = "hi";
button.addEventListener("click", function(){
    token_bucket.remove_token(10);
    console.log(token_bucket.b);
});
document.body.appendChild(button);
