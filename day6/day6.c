#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int hash(char* name);
int intPower(int num, int power);

int main(int argc, char** argv)
{
    int lineCount = 0;
    int totalPossibleVertices = 0;
    int i;
    char line[9];
    memset(line, '\0', 9);

    int fd = open("input.txt", O_RDONLY);

    while(read(fd, line, 8) > 0)
    {
        lineCount++;
        totalPossibleVertices += 2;

        printf("%s\n", line);
    }

    lseek(fd, 0, SEEK_SET);

    printf("%d\n", lineCount);

    for(i = 0; i < lineCount; i++)
    {
        char orbitedVertex[4], orbitingVertex[4];
        orbitedVertex[3] = '\0';
        orbitingVertex[3] = '\0';

        read(fd, orbitedVertex, 3);
        read(fd, NULL, 1);
        read(fd, orbitingVertex, 3);
        read(fd, NULL, 1);

        printf("%s)%s\n", hash(orbitedVertex), hash(orbitingVertex));
    }
}

int hash(char* name)
{
    int j, k, result;
    k = 0;
    result = 0;

    for(j = strlen(name) - 1; j >= 0; j--)
    {
        if(name[j] >= '0' && name[j] <= '9')
            result += (name[j] - '0') * intPower(100, k);
        else if(name[j] >= 'A' && name[j] <= 'Z')
            result += (name[j] - 'A' + 10) * intPower(100, k);
    }

    return result;
}

int intPower(int num, int power)
{
    int result = 1;
    while(power > 0)
    {
        result *= num;
        power--;
    }

    return result;
}