"""
Sistema Alke CRM - MVP (CLI Version)
Integra Servicios, Modelos y Persistencia.
"""
import sys
import os
from typing import Dict

# Añadir directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.cliente_service import ClienteService
from src.services.export_service import ExportService
from src.core.exceptions import AlkeCRMException

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n=== 🚀 ALKE CRM (MVP) ===")
    print("1. Agregar Cliente Regular")
    print("2. Agregar Cliente Premium")
    print("3. Agregar Cliente Corporativo")
    print("4. Ver Todos los Clientes")
    print("5. Exportar a JSON")
    print("6. Exportar a CSV")
    print("7. Salir")
    return input("Seleccione una opción: ")

def capturar_datos_basicos() -> Dict[str, str]:
    print("\n--- Ingrese Datos ---")
    return {
        "nombre": input("Nombre: "),
        "email": input("Email: "),
        "telefono": input("Teléfono: ")
    }

def main():
    service = ClienteService()
    
    while True:
        try:
            opcion = mostrar_menu()
            
            if opcion == '7':
                print("¡Éxito en la presentación! Cerrando...")
                break
            
            elif opcion in ['1', '2', '3']:
                datos = capturar_datos_basicos()
                tipo = ""
                
                if opcion == '1':
                    tipo = 'regular'
                elif opcion == '2':
                    tipo = 'premium'
                    print("Nota: Se aplicará descuento automático de Premium.")
                elif opcion == '3':
                    tipo = 'corporativo'
                    datos['empresa'] = input("Nombre de la Empresa: ")

                nuevo_cliente = service.crear_cliente(tipo, datos)
                print(f"\n✅ Cliente creado: {nuevo_cliente.nombre}")

            elif opcion == '4':
                clientes = service.obtener_todos()
                print(f"\n--- Listado ({len(clientes)}) ---")
                for c in clientes:
                    print(c.mostrar_info())

            elif opcion == '5':
                clientes = service.obtener_todos()
                path = ExportService.exportar_json(clientes)
                print(f"\n💾 Exportado JSON en: {path}")

            elif opcion == '6':
                clientes = service.obtener_todos()
                path = ExportService.exportar_csv(clientes)
                print(f"\n💾 Exportado CSV en: {path}")
                
        except AlkeCRMException as e:
            print(f"\n❌ Error de Negocio: {e}")
        except Exception as e:
            print(f"\n❌ Error Inesperado: {e}")
            
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()
