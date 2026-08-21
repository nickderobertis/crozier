

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
from ..types.error_response import ErrorResponse
from ..types.iniciar_sesion_response import IniciarSesionResponse
from ..types.rol_usuario import RolUsuario
from ..types.usuario_response import UsuarioResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsuariosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def iniciar_sesion(
        self, *, nombre_usuario: str, contrasena: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IniciarSesionResponse]:
        """
        Endpoint público. Valida credenciales y retorna un token JWT Bearer
        con el rol del usuario codificado.

        Parameters
        ----------
        nombre_usuario : str
            Nombre de usuario

        contrasena : str
            Contraseña del usuario

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IniciarSesionResponse]
            Autenticación exitosa
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/usuarios/login",
            method="POST",
            json={
                "nombreUsuario": nombre_usuario,
                "contrasena": contrasena,
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
                    IniciarSesionResponse,
                    parse_obj_as(
                        type_=IniciarSesionResponse,
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

    def registrar_solicitante(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsuarioResponse]:
        """
        Endpoint público. Permite a cualquier persona registrarse con rol `SOLICITANTE`.
        El rol es asignado automáticamente por el sistema.

        Parameters
        ----------
        nombre_completo : str
            Nombre completo del solicitante

        nombre_usuario : str
            Nombre de usuario único

        contrasena : str
            Contraseña (será encriptada del lado del servidor)

        email : str
            Correo electrónico del solicitante

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsuarioResponse]
            Cuenta de solicitante creada exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/usuarios/signup",
            method="POST",
            json={
                "nombreCompleto": nombre_completo,
                "nombreUsuario": nombre_usuario,
                "contrasena": contrasena,
                "email": email,
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
                    UsuarioResponse,
                    parse_obj_as(
                        type_=UsuarioResponse,
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

    def listar_usuarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UsuarioResponse]]:
        """
        Retorna una lista de todos los usuarios activos del sistema.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[UsuarioResponse]]
            Lista de usuarios activos
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/usuarios",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsuarioResponse],
                    parse_obj_as(
                        type_=typing.List[UsuarioResponse],
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

    def crear_usuario(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        rol: RolUsuario,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsuarioResponse]:
        """
        Crea una nueva cuenta de usuario en el sistema.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        nombre_completo : str
            Nombre completo del usuario

        nombre_usuario : str
            Nombre de usuario único

        contrasena : str
            Contraseña (será encriptada del lado del servidor)

        email : str
            Correo electrónico del usuario

        rol : RolUsuario

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsuarioResponse]
            Usuario creado exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/usuarios",
            method="POST",
            json={
                "nombreCompleto": nombre_completo,
                "nombreUsuario": nombre_usuario,
                "contrasena": contrasena,
                "email": email,
                "rol": rol,
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
                    UsuarioResponse,
                    parse_obj_as(
                        type_=UsuarioResponse,
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

    def cambiar_estado_usuario(
        self, id: int, *, activo: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UsuarioResponse]:
        """
        Cambia el estado activo de una cuenta de usuario.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        id : int
            ID del usuario

        activo : bool
            true para activar, false para desactivar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsuarioResponse]
            Estado del usuario actualizado exitosamente
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/usuarios/{encode_path_param(id)}/estado",
            method="PATCH",
            json={
                "activo": activo,
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
                    UsuarioResponse,
                    parse_obj_as(
                        type_=UsuarioResponse,
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


class AsyncRawUsuariosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def iniciar_sesion(
        self, *, nombre_usuario: str, contrasena: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IniciarSesionResponse]:
        """
        Endpoint público. Valida credenciales y retorna un token JWT Bearer
        con el rol del usuario codificado.

        Parameters
        ----------
        nombre_usuario : str
            Nombre de usuario

        contrasena : str
            Contraseña del usuario

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IniciarSesionResponse]
            Autenticación exitosa
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/usuarios/login",
            method="POST",
            json={
                "nombreUsuario": nombre_usuario,
                "contrasena": contrasena,
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
                    IniciarSesionResponse,
                    parse_obj_as(
                        type_=IniciarSesionResponse,
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

    async def registrar_solicitante(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsuarioResponse]:
        """
        Endpoint público. Permite a cualquier persona registrarse con rol `SOLICITANTE`.
        El rol es asignado automáticamente por el sistema.

        Parameters
        ----------
        nombre_completo : str
            Nombre completo del solicitante

        nombre_usuario : str
            Nombre de usuario único

        contrasena : str
            Contraseña (será encriptada del lado del servidor)

        email : str
            Correo electrónico del solicitante

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsuarioResponse]
            Cuenta de solicitante creada exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/usuarios/signup",
            method="POST",
            json={
                "nombreCompleto": nombre_completo,
                "nombreUsuario": nombre_usuario,
                "contrasena": contrasena,
                "email": email,
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
                    UsuarioResponse,
                    parse_obj_as(
                        type_=UsuarioResponse,
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

    async def listar_usuarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UsuarioResponse]]:
        """
        Retorna una lista de todos los usuarios activos del sistema.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[UsuarioResponse]]
            Lista de usuarios activos
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/usuarios",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsuarioResponse],
                    parse_obj_as(
                        type_=typing.List[UsuarioResponse],
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

    async def crear_usuario(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        rol: RolUsuario,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsuarioResponse]:
        """
        Crea una nueva cuenta de usuario en el sistema.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        nombre_completo : str
            Nombre completo del usuario

        nombre_usuario : str
            Nombre de usuario único

        contrasena : str
            Contraseña (será encriptada del lado del servidor)

        email : str
            Correo electrónico del usuario

        rol : RolUsuario

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsuarioResponse]
            Usuario creado exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/usuarios",
            method="POST",
            json={
                "nombreCompleto": nombre_completo,
                "nombreUsuario": nombre_usuario,
                "contrasena": contrasena,
                "email": email,
                "rol": rol,
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
                    UsuarioResponse,
                    parse_obj_as(
                        type_=UsuarioResponse,
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

    async def cambiar_estado_usuario(
        self, id: int, *, activo: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UsuarioResponse]:
        """
        Cambia el estado activo de una cuenta de usuario.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        id : int
            ID del usuario

        activo : bool
            true para activar, false para desactivar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsuarioResponse]
            Estado del usuario actualizado exitosamente
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/usuarios/{encode_path_param(id)}/estado",
            method="PATCH",
            json={
                "activo": activo,
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
                    UsuarioResponse,
                    parse_obj_as(
                        type_=UsuarioResponse,
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
