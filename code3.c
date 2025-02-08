#include <stdio.h>
#include <stdlib.h>

int main()
{
    float radius,area,circumferance;
    const float PI = 3.14;
    radius = 12.0;
    area = 2 * radius * radius;
    circumferance = 2 * PI * radius;
    printf("Area of the circle :%f\n",area);
    printf("circumferance of the circle :%f\n",circumferance);
    return 0;
}
