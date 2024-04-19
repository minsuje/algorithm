function solution(phone_number) {
    var answer = '';
    let newNum = '';
    
    newNum = phone_number.split("")
    for(let i = 0; i < newNum.length-4 ; i++){
        newNum[i] = "*"
    }
    answer = newNum.join("")
  
    return answer;
}