#include <stdio.h>

int main(void) {
    int user_num;

    printf("Enter a number: ");
    scanf("%d", &user_num);

    for (int i = 1; i <= 10; i++) {
        int calculated_num = user_num * i;
        printf("%d x %d = %d\n", user_num, i, calculated_num);
    }

    while (user_num > 0) {
        printf("%d...\n", user_num);
        user_num--;
    }

    printf("Blastoff\n");

    return 0;
}