from django.shortcuts import render

def home(request):
    return render(request, "index.html", {
        "project_name": "Self-Supervised Pretraining",
        "method": "SimCLR-style Contrastive Learning",
        "dataset": "CIFAR-10 (small CPU-friendly subset)",
    })
