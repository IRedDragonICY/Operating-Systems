#include <iostream>
#include <fstream>
using namespace std;
int main() {
// Open an output file for spooling
ofstream outputFile("output.txt");
if (!outputFile) {
cerr << "Failed to open output file." << endl;
return 1;
}
// Spool data to the output file
for (int i = 1; i <= 10; ++i) {
outputFile << "Line " << i << endl;
}
// Close the output file
outputFile.close();
// Open an input file for spooling
ifstream inputFile("output.txt");
if (!inputFile) {
cerr << "Failed to open input file." << endl;
return 1;
}
// Read and display data from the input file
string line;
while (getline(inputFile, line)) {
cout << "Read from file: " << line << endl;
}
// Close the input file
inputFile.close();
return 0;
}