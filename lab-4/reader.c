#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
  
int main()
{
    int fd = open("shmfile", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
    ftruncate(fd, 1024);
    char *str = mmap(NULL, 1024, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    close(fd);

    printf("Data read from memory: %s\n",str); 

    munmap(str, 1024);

    return 0;
}