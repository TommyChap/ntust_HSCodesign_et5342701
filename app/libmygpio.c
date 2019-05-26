#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int my_gpio_fd = 0;

int init(){
        my_gpio_fd = open("/dev/mygpio", O_RDWR);
        if(my_gpio_fd < 0) {
                return -1;
        }
        return 0;
}

int Read(int select){
        char buf[1];
        if(my_gpio_fd){
                read(my_gpio_fd, buf, select);
                return buf[0];
        }else{
                printf("Device not open\n");
		return -1;
        }
}

int Write(int data, int select){
        char buf[1];
        if(my_gpio_fd){
                buf[0] = data;
                return write(my_gpio_fd, buf, select);
        }else{
                printf("Device not open\n");
                return -1;
        }
}

