from django.shortcuts import render
from django.http import HttpResponse

def views(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def location(request):
    return render(request, 'main/location.html')

def exer1(request):
    result = None
    if request.method == "POST":
        a = float(request.POST.get("a"))
        b = float(request.POST.get("b"))
        c = float(request.POST.get("c"))
        d = float(request.POST.get("d"))

        if (a <= c and b <= d) or (b <= c and a <= d):
            result = "Да, прямоугольник может поместиться."
        else:
            result = "Нет, прямоугольник не помещается."

    return render(request, "main/exer1.html", {"result": result})

def exer2(request):
    data = {
        "student": {
            "name": "Васясин Дмитрий Алексеевич",
            "phone": "89036225363",
            "email": "davasyasin@edu.hse.ru",
            "photo": "main/img/ya.jpg"
        },
        "program": {
            "name": "Мировая Экономика",
            "description": """Цель программы - подготовка специалистов, способных свободно ориентироваться 
            в многообразии теоретических и прикладных проблем, которые ставятся перед экономистом динамичными изменениями, 
            происходящими в современном мире. Выпускники умеют анализировать товарные и валютные рынки, разбираются 
            в формах внешнеэкономической деятельности и закономерностях интеграционных процессов в современном мире, 
            знакомы с условиями повышения конкурентоспособности товаров и услуг и принципами работы международных 
            экономических организаций."""
        },
        "supervisor": {
            "name": "Щербакова Алина Вячеславовна",
            "email": "scherbakova@edu.hse.ru",
            "photo": "main/img/akadem.jpg"
        },
        "manager": {
            "name": "Заяц Елена Игоревна",
            "email": "zayac@edu.hse.ru",
            "photo": "main/img/maneger.jpg"
        },
        "classmates": [
            {"name": "Илон Маск", "email": "musk@edu.hse.ru", "phone": "+1 525-355-5656", "photo": "main/img/ilon.jpg"},
            {"name": "Марк Цукерберг", "email": "zuck@edu.hse.ru", "phone": "+1 555-123-4567", "photo": "main/img/chuk.jpg"}
        ],
    }
    return render(request, "main/exer2.html", data)
