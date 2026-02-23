#include <stdio.h>
#define MAX_READINGS 10

int find_maxiumum(int readings[MAX_READINGS], int current_num_readings);
float calculate_average(int readings[MAX_READINGS], int current_num_readings);

int main(void) {
    int user_input;
    int num_readings = 0;
    int readings[MAX_READINGS];
    int current_num_readings = 0;

    do {
        printf("1. Enter new data\n2. Display maximum value\n3. Calculate average\n4. Exit\n");
        scanf("%d", &user_input);

        switch (user_input) {
            case 1:
                printf("How many readings would you like to enter");
                scanf("%d", &num_readings);

                if (num_readings > MAX_READINGS || (num_readings + current_num_readings) > MAX_READINGS) {
                    printf("Number of readings exceeds max readings");
                    break;
                }
                else{
                    for (int i = 0; i < num_readings; i++) {
                        printf("Enter the new reading: ");
                        scanf("%d", &readings[current_num_readings]);
                        current_num_readings++;
                    }
                }
                break;

            case 2:
                if (current_num_readings == 0){
                    printf("The array is empty, exiting\n");
                    break;
                }
                printf("%d\n", find_maxiumum(readings, current_num_readings));
                break;
            case 3:
                if (current_num_readings == 0){
                    printf("The array is empty, exiting\n");
                    break;
                }
                printf("%f\n", calculate_average(readings, current_num_readings));
                break;
            case 4:
                printf("Exiting\n");
                break;
            default:
                printf("Invalid input\n");
            }
    } while (user_input != 4);
    
    return 0;
}

int find_maxiumum(int readings[MAX_READINGS], int current_num_readings) {
    int maximum_reading = readings[0];
    for (int i = 0; i < current_num_readings; i++) {
        if (readings[i] > maximum_reading){ 
            maximum_reading = readings[i];
        }
    }
    return maximum_reading;
}

float calculate_average(int readings[MAX_READINGS], int current_num_readings) {
    float total_of_readings = 0.0;
    for (int i = 0; i < current_num_readings; i++) {
        total_of_readings += readings[i];
    }
    return (total_of_readings / current_num_readings);
}