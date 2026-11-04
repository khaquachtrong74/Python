# Python Practice

Python coursework and side experiments. Mixed bag on purpose — this is where exercises get
thrown, so folder quality varies.

> For the Python that actually matters, see
> [**CXR-Align**](https://github.com/khaquachtrong74/CXR-Align) (PyTorch, MIMIC-CXR
> contrastive alignment) and [**Fake-News-Detection**](https://github.com/khaquachtrong74/Fake-News-Detection) (BERT).

## Contents

| Path | What it is |
|---|---|
| `Practice/Cutting-edge-Program/` | Django + DRF (`courseapp`, `saleappv1`) — models, serializers, views, migrations |
| `Practice/TechProgram/` | course exercises, `Buoi01` onwards |
| `Programming-WebApp/pizzaproject/` | Django project |
| `Programming-WebApp/todolist-project/` | Django + DRF backend, JS frontend |
| `convert_pth_to_onnx.py` | PyTorch checkpoint → ONNX export |
| `Utility/speed_test.py` | small utility scripts |

## Stack

Django 5.2 · Django REST Framework · drf-yasg · MySQL (`PyMySQL` / `mysqlclient`) ·
Pillow · Django CKEditor

## Running (Django projects)

```bash
cd Practice/Cutting-edge-Program/session/courseapp
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Notes

- Each subproject has its own dependencies; there is no repo-level `requirements.txt`.
- Some `.idea/` editor folders are committed.

## ⚠️ `Practice/DDoS.py`

This file is a five-line infinite loop against a user-supplied URL:

```python
target = input()
while True:
    r = requests.get(target)
```

It is a script written while learning what `requests` does, **not** a tool. It has no rate
limiting, no target restriction and no purpose other than hammering a host. Do not run it
against anything you do not own — that is a denial-of-service attack and is illegal in most
jurisdictions.
