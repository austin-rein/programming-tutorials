#include <stdio.h>

int main(void) {
    char user_initial;
    int user_age;
    float user_wage;

    printf("Enter your initial: ");
    scanf("%c", &user_initial);

    printf("Enter your age: ");
    scanf("%d", &user_age);

    printf("Enter your wage: ");
    scanf("%f", &user_wage);

    printf("You entered: %c %d %.2f\n", user_initial, user_age, user_wage);
    return 0;
}