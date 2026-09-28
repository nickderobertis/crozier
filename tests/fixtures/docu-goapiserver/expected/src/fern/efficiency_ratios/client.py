

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.efficiency_ratio import EfficiencyRatio
from .raw_client import AsyncRawEfficiencyRatiosClient, RawEfficiencyRatiosClient


class EfficiencyRatiosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEfficiencyRatiosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEfficiencyRatiosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEfficiencyRatiosClient
        """
        return self._raw_client

    def get_efficiency_ratios_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EfficiencyRatio]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns ratios sorted by school_name ascending. No school_id filter or pagination is implemented.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EfficiencyRatio]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.efficiency_ratios.get_efficiency_ratios_v3(
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_efficiency_ratios_v3(company_id=company_id, request_options=request_options)
        return _response.data


class AsyncEfficiencyRatiosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEfficiencyRatiosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEfficiencyRatiosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEfficiencyRatiosClient
        """
        return self._raw_client

    async def get_efficiency_ratios_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EfficiencyRatio]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns ratios sorted by school_name ascending. No school_id filter or pagination is implemented.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EfficiencyRatio]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.efficiency_ratios.get_efficiency_ratios_v3(
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_efficiency_ratios_v3(
            company_id=company_id, request_options=request_options
        )
        return _response.data
