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
    int i;
    char line[9];
    memset(line, '\0', 9);

    int fd = open("input.txt", O_RDONLY);
    int bytesRead = 0;
    int currentBytes = 0;

    do
    {
        bytesRead = 0;

        while(bytesRead + (currentBytes = read(fd, line + bytesRead, 8 - bytesRead)) < 8 && currentBytes != 0)
            bytesRead += currentBytes;

        if(currentBytes > 0)
            lineCount++;
    } while (currentBytes != 0);

    lseek(fd, 0, SEEK_SET);

    for(i = 0; i < lineCount; i++)
    {
        char orbitedVertex[4], orbitingVertex[4];
        memset(orbitedVertex, '\0', 4);
        memset(orbitingVertex, '\0', 4);

        currentBytes = 0;

        bytesRead = 0;

        while(bytesRead + (currentBytes = read(fd, line + bytesRead, 8 - bytesRead)) < 8 && currentBytes != 0)
            bytesRead += currentBytes;

        orbitedVertex[0] = line[0];
        orbitedVertex[1] = line[1];
        orbitedVertex[2] = line[2];

        orbitingVertex[0] = line[4];
        orbitingVertex[1] = line[5];
        orbitingVertex[2] = line[6];

        //printf("%s)%s\n", orbitedVertex, orbitingVertex);

        printf("%d)%d\n", hash(orbitedVertex), hash(orbitingVertex));
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

        k++;
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