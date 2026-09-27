

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ip import Ip
from .raw_client import AsyncRawIpEnrichmentClient, RawIpEnrichmentClient


class IpEnrichmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIpEnrichmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIpEnrichmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIpEnrichmentClient
        """
        return self._raw_client

    def ip_enrich(
        self,
        *,
        ip: str,
        return_ip_location: typing.Optional[bool] = None,
        return_ip_metadata: typing.Optional[bool] = None,
        return_person: typing.Optional[bool] = None,
        return_if_unmatched: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ip:
        """
        Parameters
        ----------
        ip : str
            IP that will be enriched.

        return_ip_location : typing.Optional[bool]
            IP responses will not include location data for the IP by default.  Setting to `true` will return IP specific location info.

        return_ip_metadata : typing.Optional[bool]
            IP responses will not include metadata for the IP by default.  Setting to `true` will return IP specific metadata.

        return_person : typing.Optional[bool]
            Setting to `true` will return person fields associated with the IP.

        return_if_unmatched : typing.Optional[bool]
            Setting to `true` will return IP specific metadata or location data regardless of a company match.

        titlecase : typing.Optional[bool]
            Setting to `true` will titlecase any records returned.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ip
            IP enrich completed.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ip_enrichment.ip_enrich(
            ip="ip",
        )
        """
        _response = self._raw_client.ip_enrich(
            ip=ip,
            return_ip_location=return_ip_location,
            return_ip_metadata=return_ip_metadata,
            return_person=return_person,
            return_if_unmatched=return_if_unmatched,
            titlecase=titlecase,
            pretty=pretty,
            request_options=request_options,
        )
        return _response.data


class AsyncIpEnrichmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIpEnrichmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIpEnrichmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIpEnrichmentClient
        """
        return self._raw_client

    async def ip_enrich(
        self,
        *,
        ip: str,
        return_ip_location: typing.Optional[bool] = None,
        return_ip_metadata: typing.Optional[bool] = None,
        return_person: typing.Optional[bool] = None,
        return_if_unmatched: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ip:
        """
        Parameters
        ----------
        ip : str
            IP that will be enriched.

        return_ip_location : typing.Optional[bool]
            IP responses will not include location data for the IP by default.  Setting to `true` will return IP specific location info.

        return_ip_metadata : typing.Optional[bool]
            IP responses will not include metadata for the IP by default.  Setting to `true` will return IP specific metadata.

        return_person : typing.Optional[bool]
            Setting to `true` will return person fields associated with the IP.

        return_if_unmatched : typing.Optional[bool]
            Setting to `true` will return IP specific metadata or location data regardless of a company match.

        titlecase : typing.Optional[bool]
            Setting to `true` will titlecase any records returned.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ip
            IP enrich completed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ip_enrichment.ip_enrich(
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_enrich(
            ip=ip,
            return_ip_location=return_ip_location,
            return_ip_metadata=return_ip_metadata,
            return_person=return_person,
            return_if_unmatched=return_if_unmatched,
            titlecase=titlecase,
            pretty=pretty,
            request_options=request_options,
        )
        return _response.data
