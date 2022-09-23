#include <iostream>
#include "lib.hpp"

int main()
{
  std::cout << ">> Calculator of Body Mass Index <<\n\n";

  float bmi, weight, height;

  std::cout << "Whats your weight? (kg) > ";
  std::cin >> weight;

  std::cout << "Whats your height? (cm) > ";
  std::cin >> height;

  bmi = calcBMI(weight, height);

  std::cout << "\n-> " << bmi << "\n";

  return 0;
}
