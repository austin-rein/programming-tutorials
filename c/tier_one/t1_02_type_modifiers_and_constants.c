#include <stdio.h>

int main(void) {
    const int MULTIPLIER = 5;

    unsigned int user_num;

    printf("Enter a number: ");
    scanf("%u", &user_num);

    int calculated_num = user_num * MULTIPLIER;
   
    printf("Your new number is : %d\n", calculated_num);    
    printf("Size of your number: %zu bytes\n", sizeof(user_num));
    printf("Size of the new number: %zu bytes\n", sizeof(calculated_num));

    return 0;
}