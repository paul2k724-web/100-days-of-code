template 
PROJECT NAME:

Goal:
What problem does this solve?

Inputs:
(User input, APIs, files)

Outputs:
(Console, email, SMS, GUI)

Failure cases:
(Internet down, bad input, API error)

Modules:
(File names and responsibilities)

Data storage:
(JSON, CSV, API)

Run style:
(Once / Scheduled / Continuous)

structure 
sentinel/
│
├── main.py               # Entry point
├── scheduler.py          # Runs tasks safely
├── config.py             # Constants & env vars
│
├── services/
│   ├── weather_service.py
│   ├── stock_service.py
│   ├── iss_service.py
│
├── notifiers/
│   ├── console_notifier.py
│   ├── email_notifier.py
│
├── utils/
│   ├── logger.py
│   ├── retry.py
│
└── logs/
    └── sentinel.log
