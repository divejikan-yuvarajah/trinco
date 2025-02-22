#include <stdio.h>
#include <stdlib.h>

int main()
{
    //variables declaration
    char name[20];
    int a,b;
    float c,f;
    //variables initialization
    char val[]="Welcome";
    a=10;
    //Defining Constants
    const float x=3.73;
    //Inteaction with the user
    printf("Enter Your name:");
    scanf("%s",name);
    printf("%s\n",val);

    printf("Your name is %s\n",name);
    c=90.0*3.0;
    printf("Value of c:%f\n",c);
    printf("value of X:%f\n",x);

    //using the escape sequances
    printf("Hello\tWorld\n\n");
    printf("You\nare\nlearning\n\'c\'language\n\"Do you know C language\"");

    return 0;
}
