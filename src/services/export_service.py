import json
import csv
import os
from typing import List
from src.models.cliente import Cliente
from src.core.constants import FilePaths

class ExportService:
    @staticmethod
    def exportar_json(clientes: List[Cliente], filepath: str = FilePaths.EXPORT_JSON) -> str:
        """Exporta la lista de objetos cliente a un archivo JSON."""
        try:
            # Asegurar que el directorio existe
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # Convertir objetos a diccionarios
            data = [c.to_dict() for c in clientes]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            return filepath
        except Exception as e:
            raise Exception(f"Error al exportar JSON: {str(e)}")

    @staticmethod
    def exportar_csv(clientes: List[Cliente], filepath: str = FilePaths.EXPORT_CSV) -> str:
        """Exporta la lista de objetos cliente a un archivo CSV."""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            if not clientes:
                return filepath

            # Obtenemos los headers del primer cliente (incluyendo campos dinámicos como 'empresa')
            # Para CSV necesitamos normalizar los campos (todos deben tener los mismos headers)
            fieldnames = ['uid', 'nombre', 'email', 'telefono', 'tipo', 'empresa', 'descuento']
            
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                writer.writeheader()
                
                for cliente in clientes:
                    writer.writerow(cliente.to_dict())
            
            return filepath
        except Exception as e:
            raise Exception(f"Error al exportar CSV: {str(e)}")
        