# Self-Supervised Pretraining

A lightweight, CPU-friendly self-supervised learning project using SimCLR-style contrastive learning. The model learns image representations without class labels and exposes the workflow through a simple Django portfolio demo.

## Features

- SimCLR-style contrastive pretraining
- Two augmented views per image
- NT-Xent contrastive loss
- Compact CNN encoder for CPU-only machines
- CIFAR-10 downloaded with `requests`
- Embedding visualization and cosine-similarity retrieval
- Django web app for interview demonstration
- No `src/`, preprocessing directory, or training module scripts

## Structure

```text
Self-Supervised-Pretraining/
├── data/
│   └── README.md
├── models/
│   └── README.md
├── notebooks/
│   └── 01_SimCLR_Self_Supervised_Pretraining.ipynb
├── self_supervised_web/
│   ├── templates/index.html
│   ├── __init__.py
│   ├── apps.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/css/style.css
├── CHANGELOG.md
├── CONTRIBUTE.md
├── manage.py
├── requirements.txt
└── README.md
```

## Dataset

The notebook downloads CIFAR-10 from the University of Toronto mirror. Only a configurable subset is loaded for CPU-friendly experimentation. Labels are ignored during pretraining.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Run `notebooks/01_SimCLR_Self_Supervised_Pretraining.ipynb`. The notebook saves the encoder as `models/simclr_encoder.pth`.

Then start Django:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Profiles

GitHub: https://github.com/InfinitePraveen  
LinkedIn: https://www.linkedin.com/in/infinitepraveen/

## License

For learning, experimentation, and portfolio demonstration.
