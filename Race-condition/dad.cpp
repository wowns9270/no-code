#include<fcntl.h>
#include<stdlib.h>
#include<cstdio>
#include<iostream>
#include<unistd.h>
#include<semaphore.h>

int main()
{
    int fd;
    std::cout <<"Dad comes home." << std::endl;

// #######################################
    sem_t * mutex;
    mutex = sem_open("mutex", O_CREAT, 0666, 1);
    sem_wait(mutex);
// #######################################

    std::cout <<"Dad checks the fridge." << std::endl;

    fd = open("fridge", O_CREAT|O_RDWR|O_APPEND, 0777);
    if(lseek(fd, 0 , SEEK_END) == 0)
    {
        std::cout <<"Dad goes to buy milk..." << std::endl;
        sleep(2);

        write(fd, "milk ", 5);

        std::cout <<"Dad puts milk in fridge and leaves" << std::endl;
        if(lseek(fd,0, SEEK_END) > 5)
        {
            std::cout <<"What a waste of food! The fridge can not hold so much milk" << std::endl;
        }
        while(true)
        {
            std::cout <<"wait" << std::endl;
        }
    }
    else
    {
        std::cout <<"Dad closes the fridge and leaves"<< std::endl;
    }

// #######################################
    sem_post(mutex);
    sem_close(mutex);
// #######################################

    sem_unlink("mutex");

    close(fd);
    return 0;
}