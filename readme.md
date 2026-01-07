### How to execute
Two steps: run firewall, and execute any attacker's script

1. cd .\app-sim\
2. uvicorn src.main:app --reload
3. (in a different terminal) python .\attacker\attacker.py or python .\attacker\firmware_attacker.py . . .

4. tests: python -m pytest