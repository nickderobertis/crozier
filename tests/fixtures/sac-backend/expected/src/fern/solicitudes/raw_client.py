

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.asignacion_response import AsignacionResponse
from ..types.canal_origen import CanalOrigen
from ..types.error_response import ErrorResponse
from ..types.estado_solicitud import EstadoSolicitud
from ..types.historial_response import HistorialResponse
from ..types.prioridad import Prioridad
from ..types.solicitud_response import SolicitudResponse
from ..types.solicitudes_paginadas_response import SolicitudesPaginadasResponse
from ..types.tipo_solicitud import TipoSolicitud
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSolicitudesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listar_solicitudes(
        self,
        *,
        estado: typing.Optional[EstadoSolicitud] = None,
        tipo: typing.Optional[TipoSolicitud] = None,
        prioridad: typing.Optional[Prioridad] = None,
        responsable: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SolicitudesPaginadasResponse]:
        """
        Retorna una lista paginada de solicitudes académicas. Soporta filtrado por estado,
        tipo, prioridad y usuario asignado.
        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        estado : typing.Optional[EstadoSolicitud]
            Filtrar por estado de solicitud

        tipo : typing.Optional[TipoSolicitud]
            Filtrar por tipo de solicitud

        prioridad : typing.Optional[Prioridad]
            Filtrar por nivel de prioridad

        responsable : typing.Optional[int]
            Filtrar por ID del usuario asignado

        page : typing.Optional[int]
            Número de página (basado en cero)

        size : typing.Optional[int]
            Número de elementos por página

        sort : typing.Optional[str]
            Campo y dirección de ordenamiento (ej. fechaHoraRegistro,desc)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SolicitudesPaginadasResponse]
            Lista paginada de solicitudes
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/solicitudes",
            method="GET",
            params={
                "estado": estado,
                "tipo": tipo,
                "prioridad": prioridad,
                "responsable": responsable,
                "page": page,
                "size": size,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudesPaginadasResponse,
                    parse_obj_as(
                        type_=SolicitudesPaginadasResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crear_solicitud(
        self,
        *,
        solicitante_nombre: str,
        solicitante_correo: str,
        solicitante_telefono: str,
        solicitante_identificacion: str,
        asunto: str,
        descripcion: str,
        canal_origen: CanalOrigen,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SolicitudResponse]:
        """
        Registra una nueva solicitud académica en el sistema con estado `REGISTRADA`.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        solicitante_nombre : str
            Nombre completo del solicitante

        solicitante_correo : str
            Correo electrónico del solicitante

        solicitante_telefono : str
            Número de teléfono del solicitante

        solicitante_identificacion : str
            Número de identificación del solicitante

        asunto : str
            Asunto o título breve de la solicitud

        descripcion : str
            Descripción detallada de la solicitud académica

        canal_origen : CanalOrigen

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SolicitudResponse]
            Solicitud creada exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/solicitudes",
            method="POST",
            json={
                "solicitanteNombre": solicitante_nombre,
                "solicitanteCorreo": solicitante_correo,
                "solicitanteTelefono": solicitante_telefono,
                "solicitanteIdentificacion": solicitante_identificacion,
                "asunto": asunto,
                "descripcion": descripcion,
                "canalOrigen": canal_origen,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def obtener_solicitud_por_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SolicitudResponse]:
        """
        Retorna el detalle completo de una solicitud académica.
        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        id : int
            ID único de solicitud

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SolicitudResponse]
            Detalle de la solicitud
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def clasificar_solicitud(
        self,
        id: int,
        *,
        tipo: TipoSolicitud,
        prioridad: Prioridad,
        nota_clasificacion: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SolicitudResponse]:
        """
        Establece el tipo, prioridad y justificación de prioridad para una solicitud.
        Cambia el estado a `CLASIFICADA`.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        tipo : TipoSolicitud

        prioridad : Prioridad

        nota_clasificacion : str
            Nota o justificación para la clasificación y prioridad asignada

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SolicitudResponse]
            Solicitud clasificada exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/clasificar",
            method="PATCH",
            json={
                "tipo": tipo,
                "prioridad": prioridad,
                "notaClasificacion": nota_clasificacion,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cambiar_estado_solicitud(
        self,
        id: int,
        *,
        nuevo_estado: EstadoSolicitud,
        nota: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SolicitudResponse]:
        """
        Transiciona una solicitud a un nuevo estado siguiendo el ciclo de vida válido:
        `REGISTRADA → CLASIFICADA → EN_ATENCION → ATENDIDA → CERRADA`.
        Cualquier transición inválida retorna `400 Bad Request`.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        nuevo_estado : EstadoSolicitud

        nota : typing.Optional[str]
            Nota opcional sobre el cambio de estado

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SolicitudResponse]
            Estado cambiado exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/estado",
            method="PATCH",
            json={
                "nuevoEstado": nuevo_estado,
                "nota": nota,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def asignar_responsable(
        self,
        id: int,
        *,
        responsable_id: int,
        nota_asignacion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AsignacionResponse]:
        """
        Asigna un usuario como la persona responsable de una solicitud.
        El usuario debe estar activo.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        responsable_id : int
            ID del usuario a asignar como responsable

        nota_asignacion : typing.Optional[str]
            Nota opcional sobre la asignación

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsignacionResponse]
            Usuario asignado exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/asignar",
            method="POST",
            json={
                "responsableId": responsable_id,
                "notaAsignacion": nota_asignacion,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsignacionResponse,
                    parse_obj_as(
                        type_=AsignacionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cerrar_solicitud(
        self,
        id: int,
        *,
        resolucion: str,
        notas_cierre: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SolicitudResponse]:
        """
        Cierra una solicitud. La solicitud debe estar en estado `ATENDIDA`.
        Se requiere una observación de cierre. Una vez cerrada, la solicitud no puede modificarse.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        resolucion : str
            Resolución obligatoria explicando cómo se resolvió la solicitud

        notas_cierre : typing.Optional[str]
            Notas adicionales opcionales sobre el cierre

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SolicitudResponse]
            Solicitud cerrada exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/cerrar",
            method="PATCH",
            json={
                "resolucion": resolucion,
                "notasCierre": notas_cierre,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def obtener_historial_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[HistorialResponse]]:
        """
        Retorna el rastro de auditoría completo de todas las acciones realizadas en una solicitud,
        ordenado cronológicamente.
        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        id : int
            ID único de solicitud

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[HistorialResponse]]
            Lista de entradas del historial
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/historial",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[HistorialResponse],
                    parse_obj_as(
                        type_=typing.List[HistorialResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSolicitudesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listar_solicitudes(
        self,
        *,
        estado: typing.Optional[EstadoSolicitud] = None,
        tipo: typing.Optional[TipoSolicitud] = None,
        prioridad: typing.Optional[Prioridad] = None,
        responsable: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SolicitudesPaginadasResponse]:
        """
        Retorna una lista paginada de solicitudes académicas. Soporta filtrado por estado,
        tipo, prioridad y usuario asignado.
        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        estado : typing.Optional[EstadoSolicitud]
            Filtrar por estado de solicitud

        tipo : typing.Optional[TipoSolicitud]
            Filtrar por tipo de solicitud

        prioridad : typing.Optional[Prioridad]
            Filtrar por nivel de prioridad

        responsable : typing.Optional[int]
            Filtrar por ID del usuario asignado

        page : typing.Optional[int]
            Número de página (basado en cero)

        size : typing.Optional[int]
            Número de elementos por página

        sort : typing.Optional[str]
            Campo y dirección de ordenamiento (ej. fechaHoraRegistro,desc)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SolicitudesPaginadasResponse]
            Lista paginada de solicitudes
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/solicitudes",
            method="GET",
            params={
                "estado": estado,
                "tipo": tipo,
                "prioridad": prioridad,
                "responsable": responsable,
                "page": page,
                "size": size,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudesPaginadasResponse,
                    parse_obj_as(
                        type_=SolicitudesPaginadasResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crear_solicitud(
        self,
        *,
        solicitante_nombre: str,
        solicitante_correo: str,
        solicitante_telefono: str,
        solicitante_identificacion: str,
        asunto: str,
        descripcion: str,
        canal_origen: CanalOrigen,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SolicitudResponse]:
        """
        Registra una nueva solicitud académica en el sistema con estado `REGISTRADA`.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        solicitante_nombre : str
            Nombre completo del solicitante

        solicitante_correo : str
            Correo electrónico del solicitante

        solicitante_telefono : str
            Número de teléfono del solicitante

        solicitante_identificacion : str
            Número de identificación del solicitante

        asunto : str
            Asunto o título breve de la solicitud

        descripcion : str
            Descripción detallada de la solicitud académica

        canal_origen : CanalOrigen

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SolicitudResponse]
            Solicitud creada exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/solicitudes",
            method="POST",
            json={
                "solicitanteNombre": solicitante_nombre,
                "solicitanteCorreo": solicitante_correo,
                "solicitanteTelefono": solicitante_telefono,
                "solicitanteIdentificacion": solicitante_identificacion,
                "asunto": asunto,
                "descripcion": descripcion,
                "canalOrigen": canal_origen,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def obtener_solicitud_por_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SolicitudResponse]:
        """
        Retorna el detalle completo de una solicitud académica.
        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        id : int
            ID único de solicitud

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SolicitudResponse]
            Detalle de la solicitud
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def clasificar_solicitud(
        self,
        id: int,
        *,
        tipo: TipoSolicitud,
        prioridad: Prioridad,
        nota_clasificacion: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SolicitudResponse]:
        """
        Establece el tipo, prioridad y justificación de prioridad para una solicitud.
        Cambia el estado a `CLASIFICADA`.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        tipo : TipoSolicitud

        prioridad : Prioridad

        nota_clasificacion : str
            Nota o justificación para la clasificación y prioridad asignada

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SolicitudResponse]
            Solicitud clasificada exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/clasificar",
            method="PATCH",
            json={
                "tipo": tipo,
                "prioridad": prioridad,
                "notaClasificacion": nota_clasificacion,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cambiar_estado_solicitud(
        self,
        id: int,
        *,
        nuevo_estado: EstadoSolicitud,
        nota: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SolicitudResponse]:
        """
        Transiciona una solicitud a un nuevo estado siguiendo el ciclo de vida válido:
        `REGISTRADA → CLASIFICADA → EN_ATENCION → ATENDIDA → CERRADA`.
        Cualquier transición inválida retorna `400 Bad Request`.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        nuevo_estado : EstadoSolicitud

        nota : typing.Optional[str]
            Nota opcional sobre el cambio de estado

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SolicitudResponse]
            Estado cambiado exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/estado",
            method="PATCH",
            json={
                "nuevoEstado": nuevo_estado,
                "nota": nota,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def asignar_responsable(
        self,
        id: int,
        *,
        responsable_id: int,
        nota_asignacion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AsignacionResponse]:
        """
        Asigna un usuario como la persona responsable de una solicitud.
        El usuario debe estar activo.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        responsable_id : int
            ID del usuario a asignar como responsable

        nota_asignacion : typing.Optional[str]
            Nota opcional sobre la asignación

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsignacionResponse]
            Usuario asignado exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/asignar",
            method="POST",
            json={
                "responsableId": responsable_id,
                "notaAsignacion": nota_asignacion,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsignacionResponse,
                    parse_obj_as(
                        type_=AsignacionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cerrar_solicitud(
        self,
        id: int,
        *,
        resolucion: str,
        notas_cierre: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SolicitudResponse]:
        """
        Cierra una solicitud. La solicitud debe estar en estado `ATENDIDA`.
        Se requiere una observación de cierre. Una vez cerrada, la solicitud no puede modificarse.
        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        id : int
            ID único de solicitud

        resolucion : str
            Resolución obligatoria explicando cómo se resolvió la solicitud

        notas_cierre : typing.Optional[str]
            Notas adicionales opcionales sobre el cierre

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SolicitudResponse]
            Solicitud cerrada exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/cerrar",
            method="PATCH",
            json={
                "resolucion": resolucion,
                "notasCierre": notas_cierre,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SolicitudResponse,
                    parse_obj_as(
                        type_=SolicitudResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def obtener_historial_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[HistorialResponse]]:
        """
        Retorna el rastro de auditoría completo de todas las acciones realizadas en una solicitud,
        ordenado cronológicamente.
        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        id : int
            ID único de solicitud

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[HistorialResponse]]
            Lista de entradas del historial
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/solicitudes/{encode_path_param(id)}/historial",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[HistorialResponse],
                    parse_obj_as(
                        type_=typing.List[HistorialResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
