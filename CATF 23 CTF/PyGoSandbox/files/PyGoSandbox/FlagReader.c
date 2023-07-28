#include <unistd.h>

int main() {
    const char* command = "cat /root/flag.txt";
    setuid(0);
    system(command);
    return 0;
}

