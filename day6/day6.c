#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char** argv)
{
    int lines = 0;

    int fd = open("input.txt", O_RDONLY);

    char line[9];
    line[8] = '\0';

    while(read(fd, line, 8) == 8)
    {
        lines++;
    }

    lseek(fd, 0, SEEK_SET);

    read(fd, line, 8);
    printf("%s\n", line);
}