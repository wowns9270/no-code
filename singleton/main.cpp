class Singleton
{

public:
    static Singleton& getInstance()
    {
        static Singleton so;
        return so;
    }

    Singleton (const Singleton &tmp) = delete;
    Singleton& operator =(const Singleton &tmp) = delete;


};


int main()
{
    Singleton& s = Singleton::getInstance();
    return 0;
}