#include <iostream>

using namespace std;

int main()
{
	//całkowite:

	//2^16 = 65536
	short iloscUczniow; //16bit - signed
	unsigned short a; //0..65535
	signed short b; //-32768..32767

	int c; //32 bit. 2^32  -2mld...2mld
	unsigned int d; //0..4mld

	//ANSI C:
	// 16bit <= sizeof(short) <= sizeof(int) <= sizeof(long)
	// sizeof(short) < sizeof(long)

	c = 2000000;
	c *= 2000;
	cout << c << endl;

	d = 2000000;
	d *= 2000;
	cout << d << endl;

	a = 65535;
	cout << a << endl;
	a += 2;
	cout << a << endl;

}