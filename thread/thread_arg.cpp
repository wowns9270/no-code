#include<iostream>
#include<thread>
#include<string>

void gogo(int x, std::string& s)
{
    std::cout << x << " " << s << std::endl;
}

int main()
{
    std::string str = "hello2";
    std::thread t1(gogo, 10, std::ref(str));

    t1.join();
}