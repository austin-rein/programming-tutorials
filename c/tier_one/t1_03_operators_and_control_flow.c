#include <stdio.h>

int main(void) {
    const int minimum_age = 12;
    const int minimum_height = 48;

    int user_age;
    int user_height;
    
    printf("Enter your age: ");
    scanf("%d", &user_age);
    printf("Enter your height in inches: ");
    scanf("%d", &user_height);
  
    if (user_age >= minimum_age && user_height >= minimum_height) {
        printf("You are may ride the ride");
    }
    else if (user_height < minimum_height) {
        printf("You are not tall enough to ride");
    }
    else {
        printf("You are not old enough to ride");
    }

    return 0;
}