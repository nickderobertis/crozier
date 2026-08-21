



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AsignacionResponse,
        CanalOrigen,
        ErrorResponse,
        EstadoSolicitud,
        HistorialResponse,
        IaNoDisponibleResponse,
        IniciarSesionResponse,
        Prioridad,
        ResumenSolicitudResponse,
        RolUsuario,
        SolicitudResponse,
        SolicitudesPaginadasResponse,
        SugerirClasificacionResponse,
        TipoSolicitud,
        UsuarioResponse,
    )
    from .errors import (
        BadRequestError,
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        ServiceUnavailableError,
        UnauthorizedError,
    )
    from . import ia, solicitudes, usuarios
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsignacionResponse": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CanalOrigen": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "EstadoSolicitud": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "HistorialResponse": ".types",
    "IaNoDisponibleResponse": ".types",
    "IniciarSesionResponse": ".types",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "Prioridad": ".types",
    "ResumenSolicitudResponse": ".types",
    "RolUsuario": ".types",
    "ServiceUnavailableError": ".errors",
    "SolicitudResponse": ".types",
    "SolicitudesPaginadasResponse": ".types",
    "SugerirClasificacionResponse": ".types",
    "TipoSolicitud": ".types",
    "UnauthorizedError": ".errors",
    "UsuarioResponse": ".types",
    "__version__": ".version",
    "ia": ".ia",
    "solicitudes": ".solicitudes",
    "usuarios": ".usuarios",
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
    "AsyncFernApi",
    "BadRequestError",
    "CanalOrigen",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "EstadoSolicitud",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "HistorialResponse",
    "IaNoDisponibleResponse",
    "IniciarSesionResponse",
    "InternalServerError",
    "NotFoundError",
    "Prioridad",
    "ResumenSolicitudResponse",
    "RolUsuario",
    "ServiceUnavailableError",
    "SolicitudResponse",
    "SolicitudesPaginadasResponse",
    "SugerirClasificacionResponse",
    "TipoSolicitud",
    "UnauthorizedError",
    "UsuarioResponse",
    "__version__",
    "ia",
    "solicitudes",
    "usuarios",
]
