function solution(n)
{
    var answer = 0;
    // 숫자 -> 문자열 배열 ( for 문 반복 )
    let arr = String(n).split('');
//     // forEach문
    
//     arr.forEach((a) => answer += Number(a));
    
//     //for문
//     for(let i = 0; i < arr.length; i++){
//         answer += Number(arr[i]);
//     }
    
    // while문, 숫자로 계산 시
    while(n>=10){
        //123%10 => 3
        answer += n%10; // 일의 자리
        n = parseInt(n/10); // parseInt : 숫자로 바꾼 값에서 정수 값만
    }
    answer += n;
    
    
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')

    return answer;
}