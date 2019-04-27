#include <stdexcept>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stack>

std::string inputFile(const std::string& filename)
{
    std::string commands;
    std::ifstream file(filename);

    if (!file.is_open())
        throw std::runtime_error("Failed to open '" + filename + "'.");

    while (file.good()) {
        commands.push_back(file.get());
    }

    return commands;
}

extern "C" void interpret(char* commands_str)
{
    std::string commands(commands_str);

    std::vector<int> data(1, 0);
    std::vector<int>::iterator dataPtr = data.begin();

    std::string::const_iterator instructionPtr = commands.begin();
    std::stack<std::string::const_iterator> instructionStack;

    while (instructionPtr != commands.end())
    {
        switch (*instructionPtr)
        {
        case '<':
        {
            dataPtr--;
            break;
        }
        case '>':
        {
            dataPtr++;
            if (dataPtr == data.end()) {
                data.push_back(0);
                dataPtr = data.end()-1;
            }
            break;
        }
        case '+':
        {
            (*dataPtr) += 1;
            break;
        }
        case '-':
        {
            (*dataPtr) -= 1;
            break;
        }
        case '.':
        {
            std::cout << char(*dataPtr);
            break;
        }
        case ',':
        {
            char input;
            std::cin >> input;
            *dataPtr = input;
        }
        case '[':
        {
            instructionStack.push(instructionPtr);

            if (*dataPtr == 0)
            {
                auto startInstructionPtr = instructionPtr;
                while (++instructionPtr != commands.end())
                {
                    if (*instructionPtr == '[')
                        instructionStack.push(instructionPtr);
                    else if (*instructionPtr == ']')
                    {
                        if (instructionStack.empty())
                            throw std::runtime_error("Found a ']' that did not have a matching '['!");

                        auto tempInstructionPtr = instructionStack.top();
                        instructionStack.pop();

                        if (startInstructionPtr == tempInstructionPtr)
                            break;
                    }
                }
            }
            break;
        }
        case ']':
        {
            if (instructionStack.empty())
                throw std::runtime_error("Found a ']' that did not have a matching '['!");

            if (*dataPtr != 0)
                instructionPtr = instructionStack.top();
            else
                instructionStack.pop();

            break;
        }
        default:
            break;
        }

        instructionPtr++;
    }

    if (!instructionStack.empty())
        throw std::runtime_error("Found a '[' that did not have a matching ']'!");
}