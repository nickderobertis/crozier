

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.iniciar_sesion_response import IniciarSesionResponse
from ..types.rol_usuario import RolUsuario
from ..types.usuario_response import UsuarioResponse
from .raw_client import AsyncRawUsuariosClient, RawUsuariosClient


OMIT = typing.cast(typing.Any, ...)


class UsuariosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsuariosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsuariosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsuariosClient
        """
        return self._raw_client

    def iniciar_sesion(
        self, *, nombre_usuario: str, contrasena: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IniciarSesionResponse:
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
        IniciarSesionResponse
            Autenticación exitosa

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usuarios.iniciar_sesion(
            nombre_usuario="jgarcia",
            contrasena="S3cur3P@ss!",
        )
        """
        _response = self._raw_client.iniciar_sesion(
            nombre_usuario=nombre_usuario, contrasena=contrasena, request_options=request_options
        )
        return _response.data

    def registrar_solicitante(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsuarioResponse:
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
        UsuarioResponse
            Cuenta de solicitante creada exitosamente

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usuarios.registrar_solicitante(
            nombre_completo="Carlos Pérez",
            nombre_usuario="cperez",
            contrasena="MiClave@2026",
            email="carlos.perez@uniquindio.edu.co",
        )
        """
        _response = self._raw_client.registrar_solicitante(
            nombre_completo=nombre_completo,
            nombre_usuario=nombre_usuario,
            contrasena=contrasena,
            email=email,
            request_options=request_options,
        )
        return _response.data

    def listar_usuarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsuarioResponse]:
        """
        Retorna una lista de todos los usuarios activos del sistema.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsuarioResponse]
            Lista de usuarios activos

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usuarios.listar_usuarios()
        """
        _response = self._raw_client.listar_usuarios(request_options=request_options)
        return _response.data

    def crear_usuario(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        rol: RolUsuario,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsuarioResponse:
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
        UsuarioResponse
            Usuario creado exitosamente

        Examples
        --------
        from fern import FernApi, RolUsuario

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usuarios.crear_usuario(
            nombre_completo="Ana Pérez",
            nombre_usuario="aperez",
            contrasena="N3wUs3r@2026",
            email="ana.perez@uniquindio.edu.co",
            rol=RolUsuario.GESTOR,
        )
        """
        _response = self._raw_client.crear_usuario(
            nombre_completo=nombre_completo,
            nombre_usuario=nombre_usuario,
            contrasena=contrasena,
            email=email,
            rol=rol,
            request_options=request_options,
        )
        return _response.data

    def cambiar_estado_usuario(
        self, id: int, *, activo: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> UsuarioResponse:
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
        UsuarioResponse
            Estado del usuario actualizado exitosamente

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usuarios.cambiar_estado_usuario(
            id=5,
            activo=False,
        )
        """
        _response = self._raw_client.cambiar_estado_usuario(id, activo=activo, request_options=request_options)
        return _response.data


class AsyncUsuariosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsuariosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsuariosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsuariosClient
        """
        return self._raw_client

    async def iniciar_sesion(
        self, *, nombre_usuario: str, contrasena: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IniciarSesionResponse:
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
        IniciarSesionResponse
            Autenticación exitosa

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usuarios.iniciar_sesion(
                nombre_usuario="jgarcia",
                contrasena="S3cur3P@ss!",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.iniciar_sesion(
            nombre_usuario=nombre_usuario, contrasena=contrasena, request_options=request_options
        )
        return _response.data

    async def registrar_solicitante(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsuarioResponse:
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
        UsuarioResponse
            Cuenta de solicitante creada exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usuarios.registrar_solicitante(
                nombre_completo="Carlos Pérez",
                nombre_usuario="cperez",
                contrasena="MiClave@2026",
                email="carlos.perez@uniquindio.edu.co",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.registrar_solicitante(
            nombre_completo=nombre_completo,
            nombre_usuario=nombre_usuario,
            contrasena=contrasena,
            email=email,
            request_options=request_options,
        )
        return _response.data

    async def listar_usuarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsuarioResponse]:
        """
        Retorna una lista de todos los usuarios activos del sistema.
        **Rol requerido:** `ADMINISTRADOR`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsuarioResponse]
            Lista de usuarios activos

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usuarios.listar_usuarios()


        asyncio.run(main())
        """
        _response = await self._raw_client.listar_usuarios(request_options=request_options)
        return _response.data

    async def crear_usuario(
        self,
        *,
        nombre_completo: str,
        nombre_usuario: str,
        contrasena: str,
        email: str,
        rol: RolUsuario,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsuarioResponse:
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
        UsuarioResponse
            Usuario creado exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RolUsuario

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usuarios.crear_usuario(
                nombre_completo="Ana Pérez",
                nombre_usuario="aperez",
                contrasena="N3wUs3r@2026",
                email="ana.perez@uniquindio.edu.co",
                rol=RolUsuario.GESTOR,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crear_usuario(
            nombre_completo=nombre_completo,
            nombre_usuario=nombre_usuario,
            contrasena=contrasena,
            email=email,
            rol=rol,
            request_options=request_options,
        )
        return _response.data

    async def cambiar_estado_usuario(
        self, id: int, *, activo: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> UsuarioResponse:
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
        UsuarioResponse
            Estado del usuario actualizado exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usuarios.cambiar_estado_usuario(
                id=5,
                activo=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cambiar_estado_usuario(id, activo=activo, request_options=request_options)
        return _response.data
