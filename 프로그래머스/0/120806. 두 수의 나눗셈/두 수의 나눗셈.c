#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    int answer = 0;
    double a = 0;
    a = (double)num1/num2 * 1000;
    answer = a;
    return answer;
}