# junioraidev

Aplikacja odczytuje z pliku treść artykułu, po czym przekazuje to do AI, gdzie zostaje dokonana analiza artykułu. Później AI zwraca kod html z podziałem artykułu na tytuły i podtytuły oraz akapity. 
Sugeruje też miejsca dodania obrazków wraz z podpisem obrazka i sekcją alt do wygenerowania obrazka.

Uruchomienie aplikacji
Instalujemy Pythona na komputerze, później instalujemy bibliotekę openai poleceniem
pip3 install openai
Potrzebujemy też dostać klucz do API openai, który standardowo nie może być umieszony na stałe w aplikacji ze względów bezpieczeństwa.
Otwieramy konsole Linuxa lub Windowsa
Przechodzimy poleceniam cd do konkretnego katalogu gdzie pobraliśmy aplikacje.

Przykład uruchomienuia:
cd PROJEKTY/python/rekrutaxjaoxido/zadanie
python3 main.py
