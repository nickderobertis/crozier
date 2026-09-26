

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.visualize_session_id_get_response import VisualizeSessionIdGetResponse
from .raw_client import AsyncRawVisualizationClient, RawVisualizationClient


class VisualizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVisualizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVisualizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVisualizationClient
        """
        return self._raw_client

    def get_structured_visualization_data_for_a_session(
        self,
        session_id: str,
        *,
        reload: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VisualizeSessionIdGetResponse:
        """
        Get structured visualization data for a session

        Parameters
        ----------
        session_id : str
            Session ID

        reload : typing.Optional[bool]
            Force regeneration of visualization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VisualizeSessionIdGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.visualization.get_structured_visualization_data_for_a_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.get_structured_visualization_data_for_a_session(
            session_id, reload=reload, request_options=request_options
        )
        return _response.data


class AsyncVisualizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVisualizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVisualizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVisualizationClient
        """
        return self._raw_client

    async def get_structured_visualization_data_for_a_session(
        self,
        session_id: str,
        *,
        reload: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VisualizeSessionIdGetResponse:
        """
        Get structured visualization data for a session

        Parameters
        ----------
        session_id : str
            Session ID

        reload : typing.Optional[bool]
            Force regeneration of visualization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VisualizeSessionIdGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.visualization.get_structured_visualization_data_for_a_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_structured_visualization_data_for_a_session(
            session_id, reload=reload, request_options=request_options
        )
        return _response.data
