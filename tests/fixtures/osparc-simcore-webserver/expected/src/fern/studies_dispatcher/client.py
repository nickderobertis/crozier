

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_task_get import EnvelopeTaskGet
from .raw_client import AsyncRawStudiesDispatcherClient, RawStudiesDispatcherClient


class StudiesDispatcherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStudiesDispatcherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStudiesDispatcherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStudiesDispatcherClient
        """
        return self._raw_client

    def dispatch_study(
        self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Start an async clone of a published study into the requesting user's account

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.studies_dispatcher.dispatch_study(
            study_id="study_id",
        )
        """
        _response = self._raw_client.dispatch_study(study_id, request_options=request_options)
        return _response.data


class AsyncStudiesDispatcherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStudiesDispatcherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStudiesDispatcherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStudiesDispatcherClient
        """
        return self._raw_client

    async def dispatch_study(
        self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Start an async clone of a published study into the requesting user's account

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.studies_dispatcher.dispatch_study(
                study_id="study_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dispatch_study(study_id, request_options=request_options)
        return _response.data
