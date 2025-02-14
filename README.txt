Översikt av projektet

Denna applikation är en valutakonverterare som läser realtidsdata från ett valutakurs-API och utför valutakonverteringar. Den har även en automatisk uppdateringsfunktion som läser och sparar växelkursdata varje timma.

Hur man startar applikationen

Installera nödvändiga beroenden

För att köra applikationen måste du ha Python installerad och följande Python-bibliotek:

pip install requests schedule

Kör programmet

Starta applikationen genom att köra:

python <filnamn>.py

Användaren kommer att begäras att mata in en basvaluta, en målvaluta och en belopp att konvertera.

Beroenden

requests - För att hämta valutakurser från API:et

json - För att hantera och lagra data
time - För att hantera tidsstämplar och schemaläggning

schedule - För att köra automatiserade uppdateringar

threading - För att hantera bakgrundsuppgifter

Beskrivning av kursmoment

Projektet innehåller följande moment:

API användning - Programmet laddar ner valutakurser från en extern källa (Exchange Rate API), vilket ger en indikation om hur man importerar externa tjänster i Python.

Filhantering - Historiken över konverteringar lagras i en JSON-fil, vilket ger användaren en möjlighet att titta på tidigare transaktioner.

Schemaläggning och trådar - En bakgrundsstråd körs av en schemalagd funktion som laddar ner och sparar valutakurser varje timme, vilket ger en indikation om hur man hanterar data i bakgrunden.

Felhantering - Programmet hanterar API-fel och icke giltiga inmatningar, vilket förbättrar stabiliteten.

Dessa moment valdes för att ge en brett grepp om hur man skapar en praktisk applikation med externa data, samtidig bearbetning av bakgrundsuppgifter och robust kodstruktur.