#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int angle) {
    int ans = angle;
    return ans<90?1:ans==90?2:ans<180?3:4;
}