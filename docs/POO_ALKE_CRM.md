## Programación Orientada a Objetos en el Proyecto Alke CRM (MVP)

Curso: Desarrollo de Aplicaciones Fullstack Python Trainee (AM)
Institución: SENCE
OTEC: Pixelab
Profesor: Ariel Rosenamnn
Alumno: Roberto Otárola

1. Introducción

La Programación Orientada a Objetos (POO) es un paradigma de desarrollo de software basado en la modelación de entidades del dominio mediante objetos que encapsulan estado y comportamiento. En el proyecto Alke CRM (MVP), la POO constituye el eje estructural del sistema, permitiendo construir una arquitectura modular, extensible, mantenible y escalable.

El sistema modela clientes de distintos tipos (Regular, Premium y Corporativo) aplicando principios formales de abstracción, encapsulación, herencia y polimorfismo.

2. Principios Fundamentales Aplicados
2.1 Abstracción

Se define una clase abstracta Cliente como representación genérica del concepto cliente:

class Cliente(ABC):

Esto permite:

Modelar atributos comunes (uid, nombre, email, teléfono)

Definir contrato obligatorio mediante métodos abstractos

Desacoplar lógica de negocio de implementación concreta

2.2 Encapsulación

Los atributos se definen como privados:

self._nombre
self._email

El acceso se controla mediante @property, garantizando:

Protección de invariantes

Validaciones internas

Integridad del dominio

Esto evita que la UI o la capa de persistencia violen reglas del negocio.

2.3 Herencia

Se implementan subclases:

ClienteRegular

ClientePremium

ClienteCorporativo

Todas heredan de Cliente:

class ClientePremium(Cliente):

Esto permite reutilización de código y especialización de comportamiento.

2.4 Polimorfismo

Cada subclase implementa comportamiento diferenciado:

def mostrar_info(self):

El sistema trata objetos como tipo base Cliente, pero ejecuta comportamiento específico según el tipo real.

Esto es evidente en el método _mapear_fila_a_objeto() del Repository, donde se reconstruyen objetos dinámicamente.

3. Patrones de Diseño Aplicados
3.1 Repository Pattern

Se implementa ClienteRepository como capa de acceso a datos.

Responsabilidades:

Aislar SQLite del dominio

Centralizar operaciones CRUD

Traducir errores técnicos a excepciones de negocio

Esto cumple con el principio de separación de responsabilidades.

3.2 Factory Interno

El método _mapear_fila_a_objeto() actúa como factory:

if tipo == 'ClienteCorporativo':

Permite reconstrucción polimórfica desde persistencia.

4. Manejo de Excepciones como Modelo de Dominio

Se define una jerarquía de excepciones:

ClientAlreadyExistsError

ClientNotFoundError

Esto desacopla el dominio de errores técnicos de SQLite y mejora la claridad semántica.

5. Validaciones como Protección del Dominio

Las validaciones de email y teléfono se ejecutan en el constructor del modelo:

validar_email(self._email)

Esto garantiza que ningún objeto inválido pueda existir en memoria.

Es una aplicación práctica del principio:

“Los objetos deben proteger su propio estado.”

6. Beneficios Arquitectónicos Obtenidos

La aplicación de POO en el proyecto permitió:

Alta cohesión

Bajo acoplamiento

Extensibilidad futura (ej: nuevos tipos de cliente)

Testabilidad independiente

Claridad estructural

7. Justificación de Enfoque MVP

Debido a restricción temporal, se priorizó:

Núcleo de negocio

Persistencia

Validaciones

Arquitectura sólida

Se postergaron:

GUI

Integraciones externas

Sin comprometer la calidad del diseño orientado a objetos.

8. Conclusión

El proyecto Alke CRM (MVP) implementa de manera rigurosa los principios de la POO, aplicando además patrones arquitectónicos modernos como Repository y Factory.

La estructura lograda permite evolucionar el sistema hacia una versión completa con interfaz y servicios externos sin necesidad de reestructuración profunda del núcleo.

El diseño es consistente con buenas prácticas profesionales y cumple los objetivos académicos del módulo #4.
