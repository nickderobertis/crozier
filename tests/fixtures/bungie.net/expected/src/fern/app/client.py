

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAppClient, RawAppClient
from .types.app_get_application_api_usage_response import AppGetApplicationApiUsageResponse
from .types.app_get_bungie_applications_response import AppGetBungieApplicationsResponse


class AppClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppClient
        """
        return self._raw_client

    def getapplicationapiusage(
        self,
        application_id: int,
        *,
        end: typing.Optional[dt.datetime] = None,
        start: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppGetApplicationApiUsageResponse:
        """
        Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

        Parameters
        ----------
        application_id : int
            ID of the application to get usage statistics.

        end : typing.Optional[dt.datetime]
            End time for query. Goes to now if not specified.

        start : typing.Optional[dt.datetime]
            Start time for query. Goes to 24 hours ago if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppGetApplicationApiUsageResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.app.getapplicationapiusage(
            application_id=1,
        )
        """
        _response = self._raw_client.getapplicationapiusage(
            application_id, end=end, start=start, request_options=request_options
        )
        return _response.data

    def getbungieapplications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppGetBungieApplicationsResponse:
        """
        Get list of applications created by Bungie.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppGetBungieApplicationsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.app.getbungieapplications()
        """
        _response = self._raw_client.getbungieapplications(request_options=request_options)
        return _response.data


class AsyncAppClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppClient
        """
        return self._raw_client

    async def getapplicationapiusage(
        self,
        application_id: int,
        *,
        end: typing.Optional[dt.datetime] = None,
        start: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppGetApplicationApiUsageResponse:
        """
        Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

        Parameters
        ----------
        application_id : int
            ID of the application to get usage statistics.

        end : typing.Optional[dt.datetime]
            End time for query. Goes to now if not specified.

        start : typing.Optional[dt.datetime]
            Start time for query. Goes to 24 hours ago if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppGetApplicationApiUsageResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.app.getapplicationapiusage(
                application_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getapplicationapiusage(
            application_id, end=end, start=start, request_options=request_options
        )
        return _response.data

    async def getbungieapplications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppGetBungieApplicationsResponse:
        """
        Get list of applications created by Bungie.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppGetBungieApplicationsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.app.getbungieapplications()


        asyncio.run(main())
        """
        _response = await self._raw_client.getbungieapplications(request_options=request_options)
        return _response.data
