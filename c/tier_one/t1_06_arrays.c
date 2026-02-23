#include <stdio.h>
#define NUM_GRADES 5

int main(void){
    int grades[NUM_GRADES];

    for (int i = 0; i < NUM_GRADES; i++) {
        printf("Enter your grade: ");
        scanf("%d", &grades[i]);
    }
    
    float total_grades = 0.0f;
    
    for (int i = 0; i < NUM_GRADES; i++) {
        total_grades += grades[i];
    }

    float average_grade = total_grades / NUM_GRADES;

    printf("Your total grade is: %.1f\n", average_grade);

    return 0;
}