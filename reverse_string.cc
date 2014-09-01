#include <string>

#include <iostream>

using namespace std;

void rev(char *str) {
    int i;
    int size = strlen(str);

    for(i = 0; i < size / 2; i++) {
      char c = str[i];
      str[i] = str[size - i -1];
      str[size - i - 1] = c;
    }
}

int main(int argc, char** args) {
  char *s;
  int max_size = 10;

  s = (char*) malloc(max_size*sizeof(char));
  strcpy(s, "Ola\0");

  rev(s);

  std::cout << s << "\n";

  return 0;
}
