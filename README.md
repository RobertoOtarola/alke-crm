# Alke CRM - Sistema de Gestión de Clientes (MVP) 🚀

## 📋 Descripción del Proyecto
**Alke CRM** es una solución de software robusta y modular desarrollada en Python 3 para la gestión eficiente de clientes de la empresa **Solution Tech**. 

Esta versión corresponde al **Minimum Viable Product (MVP)**, diseñado para validar la lógica de negocio, la arquitectura orientada a objetos y la persistencia de datos segura antes de la implementación de interfaces gráficas complejas.

### 🎯 Objetivo
Proveer una herramienta de línea de comandos (CLI) que permita el ciclo de vida completo de la gestión de clientes (CRUD), asegurando la integridad de los datos mediante validaciones avanzadas y almacenamiento persistente en SQLite.

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Paradigma:** Programación Orientada a Objetos (POO) [Herencia, Polimorfismo, Encapsulación].
* **Base de Datos:** SQLite 3 (Nativo).
* **Intercambio de Datos:** JSON / CSV.
* **Arquitectura:** Repository Pattern + Service Layer.
* **Testing:** Pytest.

---

## ✨ Funcionalidades Principales
1.  **Gestión de Clientes:**
    * Creación de perfiles (Regular, Premium, Corporativo).
    * Validación estricta de emails y teléfonos (Regex).
    * Prevención de duplicados.
2.  **Persistencia Robusta:**
    * Base de datos SQLite como fuente de la verdad.
    * Sistema de logs para auditoría de operaciones.
3.  **Portabilidad:**
    * Exportación de reportes a JSON y CSV.

---

## 🚀 Instalación y Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/alke-crm-mvp.git](https://github.com/tu-usuario/alke-crm-mvp.git)
    cd alke-crm-mvp
    ```

2.  **Crear entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Iniciar el sistema:**
    ```bash
    python src/main.py
    ```

---

## 🏗️ Arquitectura del Sistema
El proyecto sigue una arquitectura por capas para garantizar escalabilidad y mantenibilidad:

* **`src/models`**: Definición de clases y reglas de negocio (POO).
* **`src/persistence`**: Capa de acceso a datos (Repository Pattern). Aísla la lógica SQL.
* **`src/services`**: Lógica de aplicación y orquestación.
* **`src/validators`**: Lógica de validación pura.
* **`src/main.py`**: Interfaz de usuario (CLI).

---

## 🧪 Testing
Para ejecutar las pruebas unitarias:
```bash
pytest tests/ -v
