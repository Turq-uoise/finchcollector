from django.shortcuts import render

finches = [
    {
        "species": "Zebra Finch",
        "color": "Gray",
        "beak_length": 1.5,
        "wing_span": 9.8,
        "weight": 15.2,
    },
    {
        "species": "Gouldian Finch",
        "color": "Multicolored",
        "beak_length": 1.2,
        "wing_span": 10.5,
        "weight": 12.7,
    },
    {
        "species": "Society Finch",
        "color": "White",
        "beak_length": 1.4,
        "wing_span": 8.9,
        "weight": 14.1,
    }
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })