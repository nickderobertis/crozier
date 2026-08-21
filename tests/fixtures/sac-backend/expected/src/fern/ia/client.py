

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.resumen_solicitud_response import ResumenSolicitudResponse
from ..types.sugerir_clasificacion_response import SugerirClasificacionResponse
from .raw_client import AsyncRawIaClient, RawIaClient


OMIT = typing.cast(typing.Any, ...)


class IaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIaClient
        """
        return self._raw_client

    def sugerir_clasificacion(
        self, *, descripcion: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SugerirClasificacionResponse:
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
        SugerirClasificacionResponse
            Sugerencias de clasificación generadas exitosamente

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ia.sugerir_clasificacion(
            descripcion="Necesito cancelar Cálculo II porque tuve una cirugía y no puedo asistir antes del cierre del período.",
        )
        """
        _response = self._raw_client.sugerir_clasificacion(descripcion=descripcion, request_options=request_options)
        return _response.data

    def generar_resumen_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResumenSolicitudResponse:
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
        ResumenSolicitudResponse
            Resumen generado exitosamente

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ia.generar_resumen_solicitud(
            id=1,
        )
        """
        _response = self._raw_client.generar_resumen_solicitud(id, request_options=request_options)
        return _response.data


class AsyncIaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIaClient
        """
        return self._raw_client

    async def sugerir_clasificacion(
        self, *, descripcion: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SugerirClasificacionResponse:
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
        SugerirClasificacionResponse
            Sugerencias de clasificación generadas exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ia.sugerir_clasificacion(
                descripcion="Necesito cancelar Cálculo II porque tuve una cirugía y no puedo asistir antes del cierre del período.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sugerir_clasificacion(
            descripcion=descripcion, request_options=request_options
        )
        return _response.data

    async def generar_resumen_solicitud(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResumenSolicitudResponse:
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
        ResumenSolicitudResponse
            Resumen generado exitosamente

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ia.generar_resumen_solicitud(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generar_resumen_solicitud(id, request_options=request_options)
        return _response.data
