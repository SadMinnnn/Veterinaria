from django.shortcuts import render, redirect
from .models import historiaclinica
from .models import recetarmedicamentos
from .models import ventasmedicamentos
from .models import registrar
from .models import registrarmascota
from django.contrib.auth.decorators import login_required


def ConsultarVentasMedicamentos(request):    
    VentasMedicamentos=ventasmedicamentos.objects.all() 
    return render(request,"ConsultarVentasMedicamentos.html", {'VentasMedicamentos':VentasMedicamentos})


def ConsultarRecetarMedicamentos(request):    
    RecetarMedicamentos=recetarmedicamentos.objects.all()
    return render(request,"ConsultarRecetarMedicamentos.html", {'RecetarMedicamentos':RecetarMedicamentos})


def ConsultarMascotasRegistradas(request):    
    RegistrarMascota=registrarmascota.objects.all()
    return render(request,"ConsultarMascotasRegistradas.html", {'RegistrarMascota':RegistrarMascota})

def ConsultarHistoriaClinica(request):    
    HistoriaClinica=historiaclinica.objects.all()
    return render(request,"ConsultarHistoriaClinica.html", {'HistoriaClinica':HistoriaClinica})


def MedicoVeterinario(request):  
    return render(request,'MedicoVeterinario.html')
        
def Registrar(request):
    if request.method=='POST':
        Usuario= request.POST['Usuario']
        Contra= request.POST['Contra']
        Tipo= request.POST['Tipo']
        registrar(Usuario=Usuario, Contra=Contra, Tipo=Tipo).save()    
        return render(request,'Registrar.html')
    else:
        return render(request,'Registrar.html')


def IniciarSesion(request):
    if request.method=='POST':
        try:
            Confirmar = registrar.objects.get(Usuario=request.POST['Usuario'], Contra=request.POST['Contra'])
            print("Usuario=", Confirmar)
            request.session['Usuario']=Confirmar.Usuario
            if Confirmar.Tipo==1:
                return redirect('Registrar')
            if Confirmar.Tipo==2:
                return redirect('MedicoVeterinario')
            if Confirmar.Tipo==3:
                return redirect('VentasMedicamentos')
            if Confirmar.Tipo==4:
                return render(request, 'VentasMedicamentos')
        except registrar.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos')
    return render(request,'IniciarSesion.html')



def RegistrarMascota(request):
    if request.method=='POST':
        Nombre= request.POST['Nombre']
        CedulaD= request.POST['CedulaD']
        Edad= request.POST['Edad']
        Especie= request.POST['Especie']
        Raza= request.POST['Raza']
        Color= request.POST['Color']
        Tamaño= request.POST['Tamaño']
        Peso= request.POST['Peso']
        registrarmascota(Nombre=Nombre, CedulaD=CedulaD, Edad=Edad, Especie=Especie, Raza=Raza, Color=Color, Tamaño=Tamaño, Peso=Peso).save()    
        return render(request,'RegistrarMascota.html')
    else:
        return render(request,'RegistrarMascota.html')

def ActualizarRegistrarMascota(request):
    if request.method == 'POST':
        Nombre= request.POST.get("Nombre")
        CedulaD= request.POST.get("CedulaD")
        Edad= request.POST.get("CedulaD")
        Especie= request.POST.get("Especie")
        Raza= request.POST.get("Raza")
        Color= request.POST.get("Color")
        Tamaño= request.POST.get("Tamaño")
        Peso= request.POST.get("Peso")

        try:
            masco = RegistrarMascota.objects.get(Nombre=Nombre)
            masco.Nombre = Nombre
            masco.CedulaD = CedulaD
            masco.Edad = Edad
            masco.Especie = Especie
            masco.Raza = Raza
            masco.Color = Color
            masco.Tamaño = Tamaño
            masco.Peso = Peso
            masco.save()
            return redirect('RegistrarMascota') 
        except RegistrarMascota.DoesNotExist:
            mensaje = 'No se encontró ninguna factura con el nombre: ' + Nombre
            return render(request, 'RegistrarMascota.html', {'mensaje': mensaje})
    return render(request, 'RegistrarMascota.html')

def EliminarRegistrarMascota(request):
    if request.method == 'POST':
        Nombre= request.POST.get("Nombre")
        try:
            ElimMas = registrarmascota.objects.get(Nombre=Nombre)
            ElimMas.delete()
            return redirect('RegistrarMascota') 
        except registrarmascota.DoesNotExist:
            mensaje = 'No se encontró ningún registro con el ID: ' + str(Nombre)
    return render(request, 'RegistrarMascota.html', {'mensaje': mensaje})

def HistoriaClinica(request):
    if request.method=='POST':
        IdOrden= request.POST.get("IdOrden")
        MedicoVQA= request.POST.get("MedicoVQA")
        MotivoC= request.POST.get("MotivoC")
        FechaH= request.POST.get("FechaH")
        Sintomatologia= request.POST.get("Sintomatologia")
        Diagonostico= request.POST.get("Diagonostico")
        Medicamentov= request.POST.get("Medicamentov")
        DosisM= request.POST.get("DosisM")
        HistorialV= request.POST.get("HistorialV")
        MedicamentoA= request.POST.get("MedicamentoA")
        DetalleP= request.POST.get("DetalleP")
        AnulaciónO= request.POST.get("AnulaciónO")
        
        HistoriaClinica=historiaclinica(IdOrden=IdOrden,MedicoVQA=MedicoVQA,MotivoC=MotivoC,FechaH=FechaH,Sintomatologia=Sintomatologia,Diagonostico=Diagonostico,Medicamentov=Medicamentov,DosisM=DosisM,HistorialV=HistorialV,MedicamentoA=MedicamentoA,DetalleP=DetalleP,AnulaciónO=AnulaciónO)
        HistoriaClinica.save()
        return render(request,'HistoriaClinica.html',{'mensaje':'Se genero una orden con la ID: '+IdOrden})     
    return render(request,"HistoriaClinica.html")



def ActualizarHistoriaClinica(request):
    if request.method == 'POST':
        IdOrden = request.POST.get("IdOrden")
        MedicoVQA = request.POST.get("MedicoVQA")
        MotivoC = request.POST.get("MotivoC")
        FechaH = request.POST.get("FechaH")
        Sintomatologia = request.POST.get("Sintomatologia")
        Diagonostico = request.POST.get("Diagonostico")
        Medicamentov = request.POST.get("Medicamentov")
        DosisM = request.POST.get("DosisM")
        HistorialV = request.POST.get("HistorialV")
        MedicamentoA = request.POST.get("MedicamentoA")
        DetalleP = request.POST.get("DetalleP")
        AnulaciónO = request.POST.get("AnulaciónO")

        try:
            historial = HistoriaClinica.objects.get(IdOrden=IdOrden)
            historial.IdOrden = IdOrden
            historial.MedicoVQA = MedicoVQA
            historial.MotivoC = MotivoC
            historial.FechaH = FechaH
            historial.Sintomatologia = Sintomatologia
            historial.Diagonostico = Diagonostico
            historial.Medicamentov = Medicamentov
            historial.DosisM = DosisM
            historial.HistorialV = HistorialV
            historial.MedicamentoA = MedicamentoA
            historial.DetalleP = DetalleP
            historial.AnulaciónO = AnulaciónO
            historial.save()
            return redirect('RegistrarMascota') 
        except HistoriaClinica.DoesNotExist:
            mensaje = 'No se encontró ninguna factura con el ID: ' + IdOrden
            return render(request, 'HistoriaClinica.html', {'mensaje': mensaje})
    return render(request, 'HistoriaClinica.html')

def EliminarHistoriaClinica(request):
    if request.method == 'POST':
        IdOrden= request.POST.get("IdOrden")
        try:
            ElimHis = historiaclinica.objects.get(IdOrden=IdOrden)
            ElimHis.delete()
            return redirect('HistoriaClinica') 
        except historiaclinica.DoesNotExist:
            mensaje = 'No se encontró ningún registro con el ID: ' + str(IdOrden)
    return render(request, 'HistoriaClinica.html', {'mensaje': mensaje})


def VentasMedicamentos(request):
    if request.method=='POST':
        IdFactura= request.POST.get("IdFactura")
        IdDueño= request.POST.get("IdDueño")
        IdMascota= request.POST.get("IdMascota")
        IdOrden= request.POST.get("IdOrden")
        NombreP= request.POST.get("NombreP")
        FechaV= request.POST.get("FechaV")
        Valor= request.POST.get("Valor")
        Cantidad= request.POST.get("Cantidad")
        
        VentasMedicamentos=ventasmedicamentos(IdFactura=IdFactura,IdDueño=IdDueño,IdMascota=IdMascota,IdOrden=IdOrden,NombreP=NombreP,FechaV=FechaV,Valor=Valor,Cantidad=Cantidad)
        VentasMedicamentos.save()
        return render(request,'VentasMedicamentos.html',{'mensaje':'Se genero una factura con la ID: '+IdFactura})     
    return render(request,"VentasMedicamentos.html")

    
def ActualizarVentasMedicamentos(request):
    if request.method == 'POST':
        IdFactura = request.POST.get("IdFactura")
        IdDueño = request.POST.get("IdDueño")
        IdMascota = request.POST.get("IdMascota")
        IdOrden = request.POST.get("IdOrden")
        NombreP = request.POST.get("NombreP")
        FechaV = request.POST.get("FechaV")
        Valor = request.POST.get("Valor")
        Cantidad = request.POST.get("Cantidad")

        try:
            factura = VentasMedicamentos.objects.get(IdFactura=IdFactura)
            factura.IdDueño = IdDueño
            factura.IdMascota = IdMascota
            factura.IdOrden = IdOrden
            factura.NombreP = NombreP
            factura.FechaV = FechaV
            factura.Valor = Valor
            factura.Cantidad = Cantidad
            factura.save()
            return redirect('VentasMedicamentos') 
        except VentasMedicamentos.DoesNotExist:
            mensaje = 'No se encontró ninguna factura con el ID: ' + IdFactura
            return render(request, 'VentasMedicamentos.html', {'mensaje': mensaje})
    return render(request, 'VentasMedicamentos.html')

def EliminarVentasMedicamentos(request):
    if request.method == 'POST':
        IdFactura= request.POST.get("IdFactura")
        try:
            ElimVenMe = ventasmedicamentos.objects.get(IdFactura=IdFactura)
            ElimVenMe.delete()
            return redirect('VentasMedicamentos') 
        except ventasmedicamentos.DoesNotExist:
            mensaje = 'No se encontró ningún registro con el ID: ' + str(IdFactura)
    return render(request, 'VentasMedicamentos.html', {'mensaje': mensaje})

def RecetarMedicamentos(request):
    if request.method=='POST':
        IdMedico= request.POST.get("IdMedico")
        CedulaD= request.POST.get("CedulaD")
        FechaR= request.POST.get("FechaR")
        NombreMD= request.POST.get("NombreMD")
        CedulaV= request.POST.get("CedulaV")
        
        RecetarMedicamentos=recetarmedicamentos(IdMedico=IdMedico,CedulaD=CedulaD,FechaR=FechaR,NombreMD=NombreMD,CedulaV=CedulaV)
        RecetarMedicamentos.save()
        return render(request,'RecetarMedicamentos.html',{'mensaje':'El : '+IdMedico+' genero una receta'})     
    return render(request,"RecetarMedicamentos.html")


def ActualizarRecetarMedicamentos(request):
    if request.method == 'POST':
        IdMedico= request.POST.get("IdMedico")
        CedulaD= request.POST.get("CedulaD")
        FechaR= request.POST.get("FechaR")
        NombreMD= request.POST.get("NombreMD")
        CedulaV= request.POST.get("CedulaV")

        try:
            receta = RecetarMedicamentos.objects.get(IdMedico=IdMedico)
            receta.IdMedico = IdMedico
            receta.CedulaD = CedulaD
            receta.FechaR = FechaR
            receta.NombreMD = NombreMD
            receta.CedulaV = CedulaV
            receta.save()
            return redirect('RecetarMedicamentos') 
        except RecetarMedicamentos.DoesNotExist:
            mensaje = 'No se encontró ninguna factura con el ID: ' + IdMedico
            return render(request, 'RecetarMedicamentos.html', {'mensaje': mensaje})
    return render(request, 'RecetarMedicamentos.html')

def EliminarRecetarMedicamentos(request):
    if request.method == 'POST':
        IdMedico= request.POST.get("IdMedico")
        try:
            ElimReMed = recetarmedicamentos.objects.get(IdMedico=IdMedico)
            ElimReMed.delete()
            return redirect('RecetarMedicamentos') 
        except recetarmedicamentos.DoesNotExist:
            mensaje = 'No se encontró ningún registro con el ID: ' + str(IdMedico)
    return render(request, 'RecetarMedicamentos.html', {'mensaje': mensaje})

