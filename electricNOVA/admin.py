from django.contrib import admin
from .models import TipoCargador

admin.site.register(TipoCargador)


from django.contrib import admin
from .models import Estado

admin.site.register(Estado)


from django.contrib import admin
from .models import Electrocasero

admin.site.register(Electrocasero)


from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)


from django.contrib import admin
from .models import Reserva

admin.site.register(Reserva)