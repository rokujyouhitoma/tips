/*
 * Floyd's cycle-finding algorithm
 * http://www.siafoo.net/algorithm/10
 **/
function floyd(top) {
    var tortoise = top;
    var hare = top;

    while(true) {
        if(!hare.slice(1) || hare.length === 0) {
            return false;
        }
        hare = hare.slice(1);
        if(!hare.slice(1) || hare.length === 0) {
            return false;
        }
        hare = hare.slice(1);
        tortoise = tortoise.slice(1);
        if(hare[0] === tortoise[0]) {
            return true;
        }
    }
}
