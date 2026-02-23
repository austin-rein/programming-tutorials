#include <stdio.h>

double celsius_to_fahrenheit(double temperature);
double fahrenheit_to_celsius(double temperature);

int main(void) {
    double user_celsius_temperature;
    double user_fahrenheit_temperature;

    printf("Enter the celsius temperature: ");
    scanf("%lf", &user_celsius_temperature);

    printf("Enter the fahrenheit temperature: ");
    scanf("%lf", &user_fahrenheit_temperature);

    double converted_celsius_temperature = celsius_to_fahrenheit(user_celsius_temperature);
    double converted_fahrenheit_temperature = fahrenheit_to_celsius(user_fahrenheit_temperature);
   
    printf("Your converted celsius to fahrenheit temperature is: %.2f\n", converted_celsius_temperature);
    printf("Your converted fahrenheit to celsius temperature is: %.2f\n", converted_fahrenheit_temperature);

    return 0;
}

double celsius_to_fahrenheit(double temperature) {
    return ((temperature * 1.8) + 32.0);
}
double fahrenheit_to_celsius(double temperature) {
    return ((temperature - 32.0) / 1.8);
}
