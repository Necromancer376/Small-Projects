#include<iostream>
#include<fstream>
#include<string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;


string WordGenerator()
{
    srand (time(NULL));
    int line =  rand() % 213 + 1;

    string word;
    ifstream in("hangman_words.txt");

    for(int i = 0; i < line; ++i)
       getline(in, word);

    return word;
}


string Checker(string word, string input, string question)
{
    int count = 0;
    int l = question.size();
    
    for(int i=0; i<l; i++)
    {
        if(word[i] == input[0])
        {
            question.replace(i, 1, input);
            count++;
        }
    }

    return count>0 ? question : "";
}


void Print(string question, string guessed, int lives, int l)
{
    system("figlet Hangman");
    cout<<endl;
    cout<<"Question: ";
    for(int i=0; i<l; i++)
        cout<<question[i]<<" ";
    cout<<endl;
    cout<<"Guessed letters: "<<guessed<<endl;
    cout<<"Lives: "<<lives<<endl<<endl;
}


int main()
{
    string word = WordGenerator();
    int word_length = word.size();

    int life = 6;
    string input;
    string guessed;
    string question;

    for(int i = 0; i < word_length; i++)
    {
        question = question + "_";
    }

    system("clear");
    
    while(life > 0)
    {
        Print(question, guessed, life, word_length);

        cout<<"Enter letter: ";
        cin>>input;
        cout<<endl;

        string response = Checker(word, input, question);
        

        if(response.empty())
        {
            life--;
            guessed = guessed + input + ",";
        }

        else if(response == word)
        {
            system("clear");
            system("figlet You Won");

            break;
        }
        else
        {
            question = response;

        }
        system("clear");
    }
    if(life == 0)
    {
        system("figlet Game Over");
        cout<<"Answer: "<<word<<endl;
    }
}

