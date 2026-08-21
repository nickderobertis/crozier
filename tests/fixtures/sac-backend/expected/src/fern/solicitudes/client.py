

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.asignacion_response import AsignacionResponse
from ..types.canal_origen import CanalOrigen
from ..types.estado_solicitud import EstadoSolicitud
from ..types.historial_response import HistorialResponse
from ..types.prioridad import Prioridad
from ..types.solicitud_response import SolicitudResponse
from ..types.solicitudes_paginadas_response import SolicitudesPaginadasResponse
from ..types.tipo_solicitud import TipoSolicitud
from .raw_client import AsyncRawSolicitudesClient, RawSolicitudesClient


OMIT = typing.cast(typing.Any, ...)


class SolicitudesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSolicitudesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSolicitudesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSolicitudesClient
        """
        return self._raw_client

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
    ) -> SolicitudesPaginadasResponse:
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
        SolicitudesPaginadasResponse
            Lista paginada de solicitudes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.solicitudes.listar_solicitudes(
            responsable=5,
            page=0,
            size=20,
            sort="fechaHoraRegistro,desc",
        )
        """
        _response = self._raw_client.listar_solicitudes(
            estado=estado,
            tipo=tipo,
            prioridad=prioridad,
            responsable=responsable,
            page=page,
            size=size,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Solicitud creada exitosamente

        Examples
        --------
        from fern import CanalOrigen, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
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
        """
        _response = self._raw_client.crear_solicitud(
            solicitante_nombre=solicitante_nombre,
            solicitante_correo=solicitante_correo,
            solicitante_telefono=solicitante_telefono,
            solicitante_identificacion=solicitante_identificacion,
            asunto=asunto,
            descripcion=descripcion,
            canal_origen=canal_origen,
            request_options=request_options,
        )
        return _response.data

    def obtener_solicitud_por_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Detalle de la solicitud

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.solicitudes.obtener_solicitud_por_id(
            id=1,
        )
        """
        _response = self._raw_client.obtener_solicitud_por_id(id, request_options=request_options)
        return _response.data

    def clasificar_solicitud(
        self,
        id: int,
        *,
        tipo: TipoSolicitud,
        prioridad: Prioridad,
        nota_clasificacion: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Solicitud clasificada exitosamente

        Examples
        --------
        from fern import FernApi, Prioridad, TipoSolicitud

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.solicitudes.clasificar_solicitud(
            id=1,
            tipo=TipoSolicitud.CANCELACION,
            prioridad=Prioridad.ALTA,
            nota_clasificacion="CANCELACION cerca de fecha límite – requiere atención inmediata",
        )
        """
        _response = self._raw_client.clasificar_solicitud(
            id, tipo=tipo, prioridad=prioridad, nota_clasificacion=nota_clasificacion, request_options=request_options
        )
        return _response.data

    def cambiar_estado_solicitud(
        self,
        id: int,
        *,
        nuevo_estado: EstadoSolicitud,
        nota: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Estado cambiado exitosamente

        Examples
        --------
        from fern import EstadoSolicitud, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.solicitudes.cambiar_estado_solicitud(
            id=1,
            nuevo_estado=EstadoSolicitud.EN_ATENCION,
        )
        """
        _response = self._raw_client.cambiar_estado_solicitud(
            id, nuevo_estado=nuevo_estado, nota=nota, request_options=request_options
        )
        return _response.data

    def asignar_responsable(
        self,
        id: int,
        *,
        responsable_id: int,
        nota_asignacion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsignacionResponse:
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
        AsignacionResponse
            Usuario asignado exitosamente

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.solicitudes.asignar_responsable(
            id=1,
            responsable_id=2,
        )
        """
        _response = self._raw_client.asignar_responsable(
            id, responsable_id=responsable_id, nota_asignacion=nota_asignacion, request_options=request_options
        )
        return _response.data

    def cerrar_solicitud(
        self,
        id: int,
        *,
        resolucion: str,
        notas_cierre: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Solicitud cerrada exitosamente

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.solicitudes.cerrar_solicitud(
            id=1,
            resolucion="Se aprobó la cancelación de Cálculo II por el comité académico.",
            notas_cierre="Solicitud resuelta – cancelación aprobada por el comité académico",
        )
        """
        _response = self._raw_client.cerrar_solicitud(
            id, resolucion=resolucion, notas_cierre=notas_cierre, request_options=request_options
        )
        return _response.data

    def obtener_historial_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[HistorialResponse]:
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
        typing.List[HistorialResponse]
            Lista de entradas del historial

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.solicitudes.obtener_historial_solicitud(
            id=1,
        )
        """
        _response = self._raw_client.obtener_historial_solicitud(id, request_options=request_options)
        return _response.data


class AsyncSolicitudesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSolicitudesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSolicitudesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSolicitudesClient
        """
        return self._raw_client

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
    ) -> SolicitudesPaginadasResponse:
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
        SolicitudesPaginadasResponse
            Lista paginada de solicitudes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.listar_solicitudes(
                responsable=5,
                page=0,
                size=20,
                sort="fechaHoraRegistro,desc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listar_solicitudes(
            estado=estado,
            tipo=tipo,
            prioridad=prioridad,
            responsable=responsable,
            page=page,
            size=size,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Solicitud creada exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CanalOrigen

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.crear_solicitud(
                solicitante_nombre="María González",
                solicitante_correo="maria.gonzalez@uniquindio.edu.co",
                solicitante_telefono="3001234567",
                solicitante_identificacion="1094567890",
                asunto="Cancelación de Cálculo II por motivos médicos",
                descripcion="Solicito cancelación de Cálculo II debido a intervención quirúrgica que me impide asistir antes del cierre del período.",
                canal_origen=CanalOrigen.SAC,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crear_solicitud(
            solicitante_nombre=solicitante_nombre,
            solicitante_correo=solicitante_correo,
            solicitante_telefono=solicitante_telefono,
            solicitante_identificacion=solicitante_identificacion,
            asunto=asunto,
            descripcion=descripcion,
            canal_origen=canal_origen,
            request_options=request_options,
        )
        return _response.data

    async def obtener_solicitud_por_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Detalle de la solicitud

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.obtener_solicitud_por_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.obtener_solicitud_por_id(id, request_options=request_options)
        return _response.data

    async def clasificar_solicitud(
        self,
        id: int,
        *,
        tipo: TipoSolicitud,
        prioridad: Prioridad,
        nota_clasificacion: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Solicitud clasificada exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Prioridad, TipoSolicitud

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.clasificar_solicitud(
                id=1,
                tipo=TipoSolicitud.CANCELACION,
                prioridad=Prioridad.ALTA,
                nota_clasificacion="CANCELACION cerca de fecha límite – requiere atención inmediata",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clasificar_solicitud(
            id, tipo=tipo, prioridad=prioridad, nota_clasificacion=nota_clasificacion, request_options=request_options
        )
        return _response.data

    async def cambiar_estado_solicitud(
        self,
        id: int,
        *,
        nuevo_estado: EstadoSolicitud,
        nota: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Estado cambiado exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EstadoSolicitud

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.cambiar_estado_solicitud(
                id=1,
                nuevo_estado=EstadoSolicitud.EN_ATENCION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cambiar_estado_solicitud(
            id, nuevo_estado=nuevo_estado, nota=nota, request_options=request_options
        )
        return _response.data

    async def asignar_responsable(
        self,
        id: int,
        *,
        responsable_id: int,
        nota_asignacion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsignacionResponse:
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
        AsignacionResponse
            Usuario asignado exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.asignar_responsable(
                id=1,
                responsable_id=2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asignar_responsable(
            id, responsable_id=responsable_id, nota_asignacion=nota_asignacion, request_options=request_options
        )
        return _response.data

    async def cerrar_solicitud(
        self,
        id: int,
        *,
        resolucion: str,
        notas_cierre: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolicitudResponse:
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
        SolicitudResponse
            Solicitud cerrada exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.cerrar_solicitud(
                id=1,
                resolucion="Se aprobó la cancelación de Cálculo II por el comité académico.",
                notas_cierre="Solicitud resuelta – cancelación aprobada por el comité académico",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cerrar_solicitud(
            id, resolucion=resolucion, notas_cierre=notas_cierre, request_options=request_options
        )
        return _response.data

    async def obtener_historial_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[HistorialResponse]:
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
        typing.List[HistorialResponse]
            Lista de entradas del historial

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.solicitudes.obtener_historial_solicitud(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.obtener_historial_solicitud(id, request_options=request_options)
        return _response.data
