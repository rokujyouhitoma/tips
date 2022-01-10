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
}

var h1 = document.createElement("h1")
document.body.appendChild(h1);
