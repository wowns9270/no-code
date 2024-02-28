#include<iostream>
#include<string>
#include<vector>
#include<memory>

class Student
{

public:
	Student()
		:name("none")
	{
		std::cout << "default empty constructor" << std::endl;
	}

	Student(const std::string &name)
		:name(std::move(name))
	{
		std::cout << "default  constructor" << std::endl;
	}

	~Student()
	{
		std::cout << "default destructor" << std::endl;
	}

	Student(const Student &tmp)
	{
		std::cout << "copy constructor " << std::endl;

		name = tmp.name;
	}

	Student(Student &&tmp) noexcept
	{
		std::cout << "move constructor " << std::endl;

		name = std::move(tmp.name);
	}

	Student& operator =(const Student &tmp)
	{
		std::cout << "copy assignement " << std::endl;
		name = tmp.name;

        return *this;
	}

	Student& operator =(Student &&tmp)
	{
		std::cout << "move assignement" << std::endl;
		name = std::move(tmp.name);

        return *this;
	}



private:

	std::string name;

};

int main()
{
	std::vector<Student> vec;

	vec.emplace_back(Student("t3"));


	vec.emplace_back("t5");

    // t5의 emplace_back 에서 move가 구현되어 있어도 copy constructor가 호출되는 이유는
    // compiler가 exception이 발생할 수도 있기 떄문에 프로그램의 안전을 위해 copy를 호출함.
    // move를 호출하려면 move constructor, move assignement에 noexcept를 써야한다.

    // 현재 move에는 새로운 resource에 대한 요청이 없기 떄문에 가능.
}