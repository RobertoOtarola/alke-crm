"""
Sistema Alke CRM - MVP (CLI Version)
Integra Servicios, Modelos, Persistencia y Logging.
Punto de entrada principal de la aplicación.
"""
import sys
import os
import logging
from typing import Dict

# --- Configuración de Path para ejecución directa ---
# pylint: disable=wrong-import-position
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- Importaciones del Proyecto ---
from src.config.logging_config import setup_logging
from src.services.cliente_service import ClienteService
from src.services.export_service import ExportService
from src.core.exceptions import AlkeCRMException

# --- Configuración Inicial ---
setup_logging()
logger = logging.getLogger(__name__)


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\n=== 🚀 ALKE CRM (MVP v1.0) ===")
    print("1. Agregar Cliente Regular")
    print("2. Agregar Cliente Premium")
    print("3. Agregar Cliente Corporativo")
    print("4. Ver Todos los Clientes")
    print("5. Exportar a JSON")
    print("6. Exportar a CSV")
    print("7. Salir")
    return input("Seleccione una opción: ")


def capturar_datos_basicos() -> Dict[str, str]:
    """Solicita los datos comunes a todos los clientes."""
    print("\n--- Ingrese Datos del Cliente ---")
    return {
        "nombre": input("Nombre: "),
        "email": input("Email: "),
        "telefono": input("Teléfono: ")
    }


def procesar_creacion(service: ClienteService, opcion: str):
    """Maneja la lógica de creación de clientes según la opción seleccionada."""
    datos = capturar_datos_basicos()
    tipo = ""

    if opcion == '1':
        tipo = 'regular'
    elif opcion == '2':
        tipo = 'premium'
        print("ℹ️  Nota: Se aplicará descuento automático de Premium.")
    elif opcion == '3':
        tipo = 'corporativo'
        datos['empresa'] = input("Nombre de la Empresa: ")

    nuevo_cliente = service.crear_cliente(tipo, datos)

    print(f"\n✅ ¡Éxito! Cliente creado: {nuevo_cliente.nombre}")
    # Fix W1203: Uso de lazy formatting (%) en lugar de f-string en logger
    logger.info("Cliente creado: %s (Tipo: %s)", nuevo_cliente.email, tipo)


def procesar_exportacion(service: ClienteService, opcion: str):
    """Maneja la lógica de exportación de datos."""
    clientes = service.obtener_todos()
    path = ""

    if opcion == '5':
        path = ExportService.exportar_json(clientes)
        print(f"\n💾 Exportación exitosa: {path}")
        logger.info("Datos exportados a JSON: %s", path)
    elif opcion == '6':
        path = ExportService.exportar_csv(clientes)
        print(f"\n💾 Exportación exitosa: {path}")
        logger.info("Datos exportados a CSV: %s", path)


def procesar_listado(service: ClienteService):
    """Maneja el listado de clientes en pantalla."""
    clientes = service.obtener_todos()
    print(f"\n--- Listado de Clientes ({len(clientes)}) ---")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for c in clientes:
            print(c.mostrar_info())


def main():
    """Función principal de ejecución."""
    logger.info("Iniciando aplicación Alke CRM MVP")
    service = ClienteService()

    while True:
        try:
            opcion = mostrar_menu()

            if opcion == '7':
                print("\n¡Gracias por usar Alke CRM! Cerrando sistema...")
                logger.info("Cierre de aplicación solicitado por usuario.")
                break

            # Fix R1723: Eliminamos el 'elif' después del break implícito y usamos funciones
            if opcion in ['1', '2', '3']:
                procesar_creacion(service, opcion)

            elif opcion == '4':
                procesar_listado(service)

            elif opcion in ['5', '6']:
                procesar_exportacion(service, opcion)

            else:
                print("\n⚠️ Opción no válida, intente nuevamente.")

        except AlkeCRMException as e:
            print(f"\n❌ Error de Negocio: {e.message}")
            logger.warning("Error controlado: %s", e.message)

        # pylint: disable=broad-exception-caught
        except Exception as e:
            print(f"\n❌ Error Inesperado del Sistema: {e}")
            logger.error("Error crítico no controlado: %s", e, exc_info=True)

        input("\nPresione Enter para continuar...")
        limpiar_pantalla()


if __name__ == "__main__":
    main()
