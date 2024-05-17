# Python Batch Job Repository

## Overview

This repository contains a Python-based batch job system following Domain-Driven Design (DDD) principles. It includes update operations for user information and task information.

## Requirements

- Python 3.11
- MySQL
- Docker (for devcontainer)
- GitHub Actions (for CI/CD)

## Setup

1. Clone the repository
   ```bash
   git clone <repository_url>
   cd batch-job-repo
   ```
2. start dev container

## run command

```
$ python src/cli.py update_user <user_id> <new_email>
$ python src/cli.py update_task <task_id> <new_status>
```

## riposotory

batch-job-repo/
├── .devcontainer/
│ ├── devcontainer.json
│ └── Dockerfile
├── .github/
│ └── workflows/
│ └── deploy.yml
├── src/
│ ├── domain/
│ │ ├── **init**.py
│ │ ├── models/
│ │ │ ├── **init**.py
│ │ │ ├── task.py
│ │ │ └── user.py
│ │ └── repositories/
│ │ ├── **init**.py
│ │ ├── task_repository.py
│ │ └── user_repository.py
│ ├── infrastructure/
│ │ ├── **init**.py
│ │ ├── db.py
│ │ └── mysql_repository.py
│ ├── application/
│ │ ├── **init**.py
│ │ ├── update_user_service.py
│ │ └── update_task_service.py
│ ├── cli.py
│ └── main.py
├── requirements.txt
└── README.md
