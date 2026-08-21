

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
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.ia_no_disponible_response import IaNoDisponibleResponse
from ..types.resumen_solicitud_response import ResumenSolicitudResponse
from ..types.sugerir_clasificacion_response import SugerirClasificacionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def sugerir_clasificacion(
        self, *, descripcion: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SugerirClasificacionResponse]:
        """
        Analiza el texto descriptivo de una solicitud y sugiere el tipo de solicitud y su
        nivel de prioridad utilizando un modelo de lenguaje externo (LLM).

        **Importante:** Las sugerencias deben ser confirmadas o ajustadas por un usuario
        humano antes de aplicarse al sistema. El sistema opera con plena funcionalidad
        sin este endpoint (RF-11).

        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        descripcion : str
            Texto descriptivo de la solicitud a analizar por el modelo de lenguaje

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SugerirClasificacionResponse]
            Sugerencias de clasificación generadas exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/ia/sugerir-clasificacion",
            method="POST",
            json={
                "descripcion": descripcion,
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
                    SugerirClasificacionResponse,
                    parse_obj_as(
                        type_=SugerirClasificacionResponse,
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        IaNoDisponibleResponse,
                        parse_obj_as(
                            type_=IaNoDisponibleResponse,
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

    def generar_resumen_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResumenSolicitudResponse]:
        """
        Genera un resumen textual del estado actual y el historial completo de una solicitud
        utilizando un modelo de lenguaje externo (LLM), para facilitar la comprensión rápida
        del caso por parte de los responsables.

        **Importante:** Este endpoint es completamente opcional. El sistema opera con
        plena funcionalidad sin él (RF-11). Si el LLM no está disponible, se retorna
        `503 Service Unavailable` y se puede consultar el historial directamente mediante
        `GET /api/v1/solicitudes/{id}/historial`.

        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        id : int
            ID único de solicitud

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResumenSolicitudResponse]
            Resumen generado exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/ia/solicitudes/{encode_path_param(id)}/resumen",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResumenSolicitudResponse,
                    parse_obj_as(
                        type_=ResumenSolicitudResponse,
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        IaNoDisponibleResponse,
                        parse_obj_as(
                            type_=IaNoDisponibleResponse,
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


class AsyncRawIaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def sugerir_clasificacion(
        self, *, descripcion: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SugerirClasificacionResponse]:
        """
        Analiza el texto descriptivo de una solicitud y sugiere el tipo de solicitud y su
        nivel de prioridad utilizando un modelo de lenguaje externo (LLM).

        **Importante:** Las sugerencias deben ser confirmadas o ajustadas por un usuario
        humano antes de aplicarse al sistema. El sistema opera con plena funcionalidad
        sin este endpoint (RF-11).

        **Rol requerido:** `GESTOR`

        Parameters
        ----------
        descripcion : str
            Texto descriptivo de la solicitud a analizar por el modelo de lenguaje

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SugerirClasificacionResponse]
            Sugerencias de clasificación generadas exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/ia/sugerir-clasificacion",
            method="POST",
            json={
                "descripcion": descripcion,
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
                    SugerirClasificacionResponse,
                    parse_obj_as(
                        type_=SugerirClasificacionResponse,
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        IaNoDisponibleResponse,
                        parse_obj_as(
                            type_=IaNoDisponibleResponse,
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

    async def generar_resumen_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResumenSolicitudResponse]:
        """
        Genera un resumen textual del estado actual y el historial completo de una solicitud
        utilizando un modelo de lenguaje externo (LLM), para facilitar la comprensión rápida
        del caso por parte de los responsables.

        **Importante:** Este endpoint es completamente opcional. El sistema opera con
        plena funcionalidad sin él (RF-11). Si el LLM no está disponible, se retorna
        `503 Service Unavailable` y se puede consultar el historial directamente mediante
        `GET /api/v1/solicitudes/{id}/historial`.

        **Rol requerido:** `SOLICITANTE`

        Parameters
        ----------
        id : int
            ID único de solicitud

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResumenSolicitudResponse]
            Resumen generado exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/ia/solicitudes/{encode_path_param(id)}/resumen",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResumenSolicitudResponse,
                    parse_obj_as(
                        type_=ResumenSolicitudResponse,
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        IaNoDisponibleResponse,
                        parse_obj_as(
                            type_=IaNoDisponibleResponse,
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
