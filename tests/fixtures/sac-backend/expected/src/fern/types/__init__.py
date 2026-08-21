



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .asignacion_response import AsignacionResponse
    from .canal_origen import CanalOrigen
    from .error_response import ErrorResponse
    from .estado_solicitud import EstadoSolicitud
    from .historial_response import HistorialResponse
    from .ia_no_disponible_response import IaNoDisponibleResponse
    from .iniciar_sesion_response import IniciarSesionResponse
    from .prioridad import Prioridad
    from .resumen_solicitud_response import ResumenSolicitudResponse
    from .rol_usuario import RolUsuario
    from .solicitud_response import SolicitudResponse
    from .solicitudes_paginadas_response import SolicitudesPaginadasResponse
    from .sugerir_clasificacion_response import SugerirClasificacionResponse
    from .tipo_solicitud import TipoSolicitud
    from .usuario_response import UsuarioResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AsignacionResponse": ".asignacion_response",
    "CanalOrigen": ".canal_origen",
    "ErrorResponse": ".error_response",
    "EstadoSolicitud": ".estado_solicitud",
    "HistorialResponse": ".historial_response",
    "IaNoDisponibleResponse": ".ia_no_disponible_response",
    "IniciarSesionResponse": ".iniciar_sesion_response",
    "Prioridad": ".prioridad",
    "ResumenSolicitudResponse": ".resumen_solicitud_response",
    "RolUsuario": ".rol_usuario",
    "SolicitudResponse": ".solicitud_response",
    "SolicitudesPaginadasResponse": ".solicitudes_paginadas_response",
    "SugerirClasificacionResponse": ".sugerir_clasificacion_response",
    "TipoSolicitud": ".tipo_solicitud",
    "UsuarioResponse": ".usuario_response",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AsignacionResponse",
    "CanalOrigen",
    "ErrorResponse",
    "EstadoSolicitud",
    "HistorialResponse",
    "IaNoDisponibleResponse",
    "IniciarSesionResponse",
    "Prioridad",
    "ResumenSolicitudResponse",
    "RolUsuario",
    "SolicitudResponse",
    "SolicitudesPaginadasResponse",
    "SugerirClasificacionResponse",
    "TipoSolicitud",
    "UsuarioResponse",
]
