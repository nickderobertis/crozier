

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.report_envelope import ReportEnvelope
from ..types.report_list import ReportList
from .raw_client import AsyncRawResultsClient, RawResultsClient


class ResultsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawResultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawResultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawResultsClient
        """
        return self._raw_client

    def campagneresultaten_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportEnvelope:
        """
        The results of a campaign.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.results.campagneresultaten_opvragen(
            campaign_id="njhgaf61ye",
        )
        """
        _response = self._raw_client.campagneresultaten_opvragen(campaign_id, request_options=request_options)
        return _response.data

    def alle_resultaten_opvragen(self, *, request_options: typing.Optional[RequestOptions] = None) -> ReportList:
        """
        The results of all campaigns in an array of list objects. The report objects have been ordered in an array with the name 'data'.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportList
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.results.alle_resultaten_opvragen()
        """
        _response = self._raw_client.alle_resultaten_opvragen(request_options=request_options)
        return _response.data


class AsyncResultsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawResultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawResultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawResultsClient
        """
        return self._raw_client

    async def campagneresultaten_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportEnvelope:
        """
        The results of a campaign.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.results.campagneresultaten_opvragen(
                campaign_id="njhgaf61ye",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagneresultaten_opvragen(campaign_id, request_options=request_options)
        return _response.data

    async def alle_resultaten_opvragen(self, *, request_options: typing.Optional[RequestOptions] = None) -> ReportList:
        """
        The results of all campaigns in an array of list objects. The report objects have been ordered in an array with the name 'data'.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportList
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.results.alle_resultaten_opvragen()


        asyncio.run(main())
        """
        _response = await self._raw_client.alle_resultaten_opvragen(request_options=request_options)
        return _response.data
