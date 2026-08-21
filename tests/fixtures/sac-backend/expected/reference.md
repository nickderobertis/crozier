# Reference
## Solicitudes
<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">listar_solicitudes</a>(...) -> SolicitudesPaginadasResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retorna una lista paginada de solicitudes académicas. Soporta filtrado por estado,
tipo, prioridad y usuario asignado.
**Rol requerido:** `SOLICITANTE`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.listar_solicitudes(
    responsable=5,
    page=0,
    size=20,
    sort="fechaHoraRegistro,desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**estado:** `typing.Optional[EstadoSolicitud]` — Filtrar por estado de solicitud
    
</dd>
</dl>

<dl>
<dd>

**tipo:** `typing.Optional[TipoSolicitud]` — Filtrar por tipo de solicitud
    
</dd>
</dl>

<dl>
<dd>

**prioridad:** `typing.Optional[Prioridad]` — Filtrar por nivel de prioridad
    
</dd>
</dl>

<dl>
<dd>

**responsable:** `typing.Optional[int]` — Filtrar por ID del usuario asignado
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Número de página (basado en cero)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Número de elementos por página
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Campo y dirección de ordenamiento (ej. fechaHoraRegistro,desc)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">crear_solicitud</a>(...) -> SolicitudResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registra una nueva solicitud académica en el sistema con estado `REGISTRADA`.
**Rol requerido:** `GESTOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CanalOrigen
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.crear_solicitud(
    solicitante_nombre="María González",
    solicitante_correo="maria.gonzalez@uniquindio.edu.co",
    solicitante_telefono="3001234567",
    solicitante_identificacion="1094567890",
    asunto="Cancelación de Cálculo II por motivos médicos",
    descripcion="Solicito cancelación de Cálculo II debido a intervención quirúrgica que me impide asistir antes del cierre del período.",
    canal_origen=CanalOrigen.SAC,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**solicitante_nombre:** `str` — Nombre completo del solicitante
    
</dd>
</dl>

<dl>
<dd>

**solicitante_correo:** `str` — Correo electrónico del solicitante
    
</dd>
</dl>

<dl>
<dd>

**solicitante_telefono:** `str` — Número de teléfono del solicitante
    
</dd>
</dl>

<dl>
<dd>

**solicitante_identificacion:** `str` — Número de identificación del solicitante
    
</dd>
</dl>

<dl>
<dd>

**asunto:** `str` — Asunto o título breve de la solicitud
    
</dd>
</dl>

<dl>
<dd>

**descripcion:** `str` — Descripción detallada de la solicitud académica
    
</dd>
</dl>

<dl>
<dd>

**canal_origen:** `CanalOrigen` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">obtener_solicitud_por_id</a>(...) -> SolicitudResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retorna el detalle completo de una solicitud académica.
**Rol requerido:** `SOLICITANTE`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.obtener_solicitud_por_id(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID único de solicitud
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">clasificar_solicitud</a>(...) -> SolicitudResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Establece el tipo, prioridad y justificación de prioridad para una solicitud.
Cambia el estado a `CLASIFICADA`.
**Rol requerido:** `GESTOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TipoSolicitud, Prioridad
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.clasificar_solicitud(
    id=1,
    tipo=TipoSolicitud.CANCELACION,
    prioridad=Prioridad.ALTA,
    nota_clasificacion="CANCELACION cerca de fecha límite – requiere atención inmediata",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID único de solicitud
    
</dd>
</dl>

<dl>
<dd>

**tipo:** `TipoSolicitud` 
    
</dd>
</dl>

<dl>
<dd>

**prioridad:** `Prioridad` 
    
</dd>
</dl>

<dl>
<dd>

**nota_clasificacion:** `str` — Nota o justificación para la clasificación y prioridad asignada
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">cambiar_estado_solicitud</a>(...) -> SolicitudResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transiciona una solicitud a un nuevo estado siguiendo el ciclo de vida válido:
`REGISTRADA → CLASIFICADA → EN_ATENCION → ATENDIDA → CERRADA`.
Cualquier transición inválida retorna `400 Bad Request`.
**Rol requerido:** `GESTOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EstadoSolicitud
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.cambiar_estado_solicitud(
    id=1,
    nuevo_estado=EstadoSolicitud.EN_ATENCION,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID único de solicitud
    
</dd>
</dl>

<dl>
<dd>

**nuevo_estado:** `EstadoSolicitud` 
    
</dd>
</dl>

<dl>
<dd>

**nota:** `typing.Optional[str]` — Nota opcional sobre el cambio de estado
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">asignar_responsable</a>(...) -> AsignacionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asigna un usuario como la persona responsable de una solicitud.
El usuario debe estar activo.
**Rol requerido:** `GESTOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.asignar_responsable(
    id=1,
    responsable_id=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID único de solicitud
    
</dd>
</dl>

<dl>
<dd>

**responsable_id:** `int` — ID del usuario a asignar como responsable
    
</dd>
</dl>

<dl>
<dd>

**nota_asignacion:** `typing.Optional[str]` — Nota opcional sobre la asignación
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">cerrar_solicitud</a>(...) -> SolicitudResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cierra una solicitud. La solicitud debe estar en estado `ATENDIDA`.
Se requiere una observación de cierre. Una vez cerrada, la solicitud no puede modificarse.
**Rol requerido:** `GESTOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.cerrar_solicitud(
    id=1,
    resolucion="Se aprobó la cancelación de Cálculo II por el comité académico.",
    notas_cierre="Solicitud resuelta – cancelación aprobada por el comité académico",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID único de solicitud
    
</dd>
</dl>

<dl>
<dd>

**resolucion:** `str` — Resolución obligatoria explicando cómo se resolvió la solicitud
    
</dd>
</dl>

<dl>
<dd>

**notas_cierre:** `typing.Optional[str]` — Notas adicionales opcionales sobre el cierre
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.solicitudes.<a href="src/fern/solicitudes/client.py">obtener_historial_solicitud</a>(...) -> typing.List[HistorialResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retorna el rastro de auditoría completo de todas las acciones realizadas en una solicitud,
ordenado cronológicamente.
**Rol requerido:** `SOLICITANTE`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.solicitudes.obtener_historial_solicitud(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID único de solicitud
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Usuarios
<details><summary><code>client.usuarios.<a href="src/fern/usuarios/client.py">iniciar_sesion</a>(...) -> IniciarSesionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint público. Valida credenciales y retorna un token JWT Bearer
con el rol del usuario codificado.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usuarios.iniciar_sesion(
    nombre_usuario="jgarcia",
    contrasena="S3cur3P@ss!",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nombre_usuario:** `str` — Nombre de usuario
    
</dd>
</dl>

<dl>
<dd>

**contrasena:** `str` — Contraseña del usuario
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.usuarios.<a href="src/fern/usuarios/client.py">registrar_solicitante</a>(...) -> UsuarioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint público. Permite a cualquier persona registrarse con rol `SOLICITANTE`.
El rol es asignado automáticamente por el sistema.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usuarios.registrar_solicitante(
    nombre_completo="Carlos Pérez",
    nombre_usuario="cperez",
    contrasena="MiClave@2026",
    email="carlos.perez@uniquindio.edu.co",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nombre_completo:** `str` — Nombre completo del solicitante
    
</dd>
</dl>

<dl>
<dd>

**nombre_usuario:** `str` — Nombre de usuario único
    
</dd>
</dl>

<dl>
<dd>

**contrasena:** `str` — Contraseña (será encriptada del lado del servidor)
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Correo electrónico del solicitante
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.usuarios.<a href="src/fern/usuarios/client.py">listar_usuarios</a>() -> typing.List[UsuarioResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retorna una lista de todos los usuarios activos del sistema.
**Rol requerido:** `ADMINISTRADOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usuarios.listar_usuarios()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.usuarios.<a href="src/fern/usuarios/client.py">crear_usuario</a>(...) -> UsuarioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Crea una nueva cuenta de usuario en el sistema.
**Rol requerido:** `ADMINISTRADOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, RolUsuario
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usuarios.crear_usuario(
    nombre_completo="Ana Pérez",
    nombre_usuario="aperez",
    contrasena="N3wUs3r@2026",
    email="ana.perez@uniquindio.edu.co",
    rol=RolUsuario.GESTOR,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nombre_completo:** `str` — Nombre completo del usuario
    
</dd>
</dl>

<dl>
<dd>

**nombre_usuario:** `str` — Nombre de usuario único
    
</dd>
</dl>

<dl>
<dd>

**contrasena:** `str` — Contraseña (será encriptada del lado del servidor)
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Correo electrónico del usuario
    
</dd>
</dl>

<dl>
<dd>

**rol:** `RolUsuario` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.usuarios.<a href="src/fern/usuarios/client.py">cambiar_estado_usuario</a>(...) -> UsuarioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cambia el estado activo de una cuenta de usuario.
**Rol requerido:** `ADMINISTRADOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usuarios.cambiar_estado_usuario(
    id=5,
    activo=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID del usuario
    
</dd>
</dl>

<dl>
<dd>

**activo:** `bool` — true para activar, false para desactivar
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IA
<details><summary><code>client.ia.<a href="src/fern/ia/client.py">sugerir_clasificacion</a>(...) -> SugerirClasificacionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analiza el texto descriptivo de una solicitud y sugiere el tipo de solicitud y su
nivel de prioridad utilizando un modelo de lenguaje externo (LLM).

**Importante:** Las sugerencias deben ser confirmadas o ajustadas por un usuario
humano antes de aplicarse al sistema. El sistema opera con plena funcionalidad
sin este endpoint (RF-11).

**Rol requerido:** `GESTOR`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ia.sugerir_clasificacion(
    descripcion="Necesito cancelar Cálculo II porque tuve una cirugía y no puedo asistir antes del cierre del período.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**descripcion:** `str` — Texto descriptivo de la solicitud a analizar por el modelo de lenguaje
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ia.<a href="src/fern/ia/client.py">generar_resumen_solicitud</a>(...) -> ResumenSolicitudResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Genera un resumen textual del estado actual y el historial completo de una solicitud
utilizando un modelo de lenguaje externo (LLM), para facilitar la comprensión rápida
del caso por parte de los responsables.

**Importante:** Este endpoint es completamente opcional. El sistema opera con
plena funcionalidad sin él (RF-11). Si el LLM no está disponible, se retorna
`503 Service Unavailable` y se puede consultar el historial directamente mediante
`GET /api/v1/solicitudes/{id}/historial`.

**Rol requerido:** `SOLICITANTE`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ia.generar_resumen_solicitud(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID único de solicitud
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

