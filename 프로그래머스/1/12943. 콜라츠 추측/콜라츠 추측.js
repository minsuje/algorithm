function solution(num) {
    var answer = 0;
    let blank = 0;
    if (num === 1) {
        answer = 0;
    } else {
        while(num != 1) {
            if (num%2 === 0){
                num  = num/2
                blank++;
            } else if (num%2 !== 0){
                num = num*3 + 1
                blank++;
            }
            answer = blank;
        }
        
    }
    
    if(blank > 500) {
        answer = -1
    }
         
    return answer;
}