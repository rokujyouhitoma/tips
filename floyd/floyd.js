/*
 * Floyd's cycle-finding algorithm
 * http://www.siafoo.net/algorithm/10
 **/
function floyd(top) {
    var tortoise = top;
    var hare = top;

    while(true) {
        if(!hare.slice(1) || hare.length === 0) {
            return false; // NO LOOP
        }
        hare = hare.slice(1); // Increment Hare
        //Is Hare at End?
        if(!hare.slice(1) || hare.length === 0) {
            return false; // NO LOOP
        }
        hare = hare.slice(1); // Increment Hare Again                                                                                                                               
        tortoise = tortoise.slice(1);
        // Did Hare Meet Tortoise?
        if(hare[0] === tortoise[0]) {
            return true; // LOOP!
        }
    }
}
