function solution(n) {
    var answer = '';
    // for(let i =1; i<=n; i++){
    //     i % 2 == 1 ? answer += '수': answer +='박';
    // }
    
    const watermelon = '수박';
// // n : 2 '수박수박'
// // n : 3 '수박수박수박'
// answer = watermelon.repeat(Number(n)).slice(0,n);

    let repeatNum = Number(n)/2;
//n : 2 '수박'
//n : 3 '수박'
    answer = watermelon.repeat(repeatNum);
    if(n %2 == 1){
      answer += '수';
    }
    return answer;
}
