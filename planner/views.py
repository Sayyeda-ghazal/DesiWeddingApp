from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from planner.models import Menu, EventType
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful. Welcome!")
            return redirect('home')
        else:
            messages.error(request, "Signup failed. Password is too similar to username")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if the user is already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def home(request):
    return render(request, "home.html")

def event_selection(request):
    events = EventType.objects.all()
    for event in events:
        event.event_list = [event.strip() for event in event.name]
    return render(request, 'event_selection.html', {"events": events})

def menus(request):
    menus = Menu.objects.all()

    for menu in menus:
        menu.item_list = [item.strip() for item in menu.items.split(',')]

    return render(request, 'menus.html', {'menus': menus})

@login_required
def get_quote(request):
    events = EventType.objects.all()
    menus = Menu.objects.all()

    estimated_cost = None
    event_name = request.GET.get('event', '')
    menu_name = request.GET.get('menu', '')
    selected_services = []

    service_prices = {
        'Catering': 5000,
        'Photography': 7000,
        'Decor': 3000,
        'Venue': 10000,
    }

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, "Please log in to generate a quote.")
            return redirect(f'/accounts/login/?next={request.path}')

        selected_event_id = request.POST.get('event')
        selected_menu_id = request.POST.get('menu')
        date = request.POST.get('date')
        guests = int(request.POST.get('guests', 0))
        services = request.POST.getlist('services')

        try:
            menu = Menu.objects.get(id=selected_menu_id)
            base_price = menu.price_per_guest
        except Menu.DoesNotExist:
            base_price = 0

        selected_services = [(s, service_prices.get(s, 0)) for s in services]
        service_fee = sum(price for _, price in selected_services)

        estimated_cost = guests * base_price + service_fee

    return render(request, 'get_quote.html', {
        'events': events,
        'menus': menus,
        'estimated_cost': estimated_cost,
        'event_name': event_name,
        'menu_name': menu_name,
        'selected_services': selected_services,  
    })
