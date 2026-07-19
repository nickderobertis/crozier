

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMetadataClient, RawMetadataClient
from .types.metadata_get_status_response import MetadataGetStatusResponse
from .types.metadata_get_user_response import MetadataGetUserResponse
from .types.metadata_retrieve_current_balances_response import MetadataRetrieveCurrentBalancesResponse
from .types.metadata_send_feedback_request_feature import MetadataSendFeedbackRequestFeature
from .types.metadata_send_feedback_response import MetadataSendFeedbackResponse
from .types.metadata_send_telemetry_request_events_item import MetadataSendTelemetryRequestEventsItem
from .types.metadata_send_telemetry_request_service import MetadataSendTelemetryRequestService
from .types.metadata_send_telemetry_response import MetadataSendTelemetryResponse


OMIT = typing.cast(typing.Any, ...)


class MetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetadataClient
        """
        return self._raw_client

    def retrievecurrentbalances(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetadataRetrieveCurrentBalancesResponse:
        """
        Retrieve the current usage balances for the organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataRetrieveCurrentBalancesResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metadata.retrievecurrentbalances()
        """
        _response = self._raw_client.retrievecurrentbalances(request_options=request_options)
        return _response.data

    def sendfeedback(
        self,
        *,
        message: str,
        feature: typing.Optional[MetadataSendFeedbackRequestFeature] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        settings: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataSendFeedbackResponse:
        """
        Send feedback from users to improve our services.

        Parameters
        ----------
        message : str

        feature : typing.Optional[MetadataSendFeedbackRequestFeature]

        agent_id : typing.Optional[str]

        session_id : typing.Optional[str]

        version : typing.Optional[str]

        platform : typing.Optional[str]

        settings : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataSendFeedbackResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metadata.sendfeedback(
            message="message",
        )
        """
        _response = self._raw_client.sendfeedback(
            message=message,
            feature=feature,
            agent_id=agent_id,
            session_id=session_id,
            version=version,
            platform=platform,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    def sendtelemetry(
        self,
        *,
        service: MetadataSendTelemetryRequestService,
        events: typing.Sequence[MetadataSendTelemetryRequestEventsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataSendTelemetryResponse:
        """
        Send telemetry events for usage tracking and analysis.

        Parameters
        ----------
        service : MetadataSendTelemetryRequestService

        events : typing.Sequence[MetadataSendTelemetryRequestEventsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataSendTelemetryResponse
            200

        Examples
        --------
        from fern.metadata import (
            MetadataSendTelemetryRequestEventsItem_SessionStart,
            MetadataSendTelemetryRequestEventsItemSessionStartData,
            MetadataSendTelemetryRequestService,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metadata.sendtelemetry(
            service=MetadataSendTelemetryRequestService.LETTA_CODE,
            events=[
                MetadataSendTelemetryRequestEventsItem_SessionStart(
                    timestamp="timestamp",
                    data=MetadataSendTelemetryRequestEventsItemSessionStartData(
                        session_id="session_id",
                        startup_command="startup_command",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.sendtelemetry(service=service, events=events, request_options=request_options)
        return _response.data

    def getstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetadataGetStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataGetStatusResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metadata.getstatus()
        """
        _response = self._raw_client.getstatus(request_options=request_options)
        return _response.data

    def getuser(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetadataGetUserResponse:
        """
        Retrieve information about the current authenticated user including email, name, organization, and current project.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataGetUserResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metadata.getuser()
        """
        _response = self._raw_client.getuser(request_options=request_options)
        return _response.data


class AsyncMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetadataClient
        """
        return self._raw_client

    async def retrievecurrentbalances(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetadataRetrieveCurrentBalancesResponse:
        """
        Retrieve the current usage balances for the organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataRetrieveCurrentBalancesResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metadata.retrievecurrentbalances()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrievecurrentbalances(request_options=request_options)
        return _response.data

    async def sendfeedback(
        self,
        *,
        message: str,
        feature: typing.Optional[MetadataSendFeedbackRequestFeature] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        settings: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataSendFeedbackResponse:
        """
        Send feedback from users to improve our services.

        Parameters
        ----------
        message : str

        feature : typing.Optional[MetadataSendFeedbackRequestFeature]

        agent_id : typing.Optional[str]

        session_id : typing.Optional[str]

        version : typing.Optional[str]

        platform : typing.Optional[str]

        settings : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataSendFeedbackResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metadata.sendfeedback(
                message="message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sendfeedback(
            message=message,
            feature=feature,
            agent_id=agent_id,
            session_id=session_id,
            version=version,
            platform=platform,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    async def sendtelemetry(
        self,
        *,
        service: MetadataSendTelemetryRequestService,
        events: typing.Sequence[MetadataSendTelemetryRequestEventsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataSendTelemetryResponse:
        """
        Send telemetry events for usage tracking and analysis.

        Parameters
        ----------
        service : MetadataSendTelemetryRequestService

        events : typing.Sequence[MetadataSendTelemetryRequestEventsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataSendTelemetryResponse
            200

        Examples
        --------
        import asyncio

        from fern.metadata import (
            MetadataSendTelemetryRequestEventsItem_SessionStart,
            MetadataSendTelemetryRequestEventsItemSessionStartData,
            MetadataSendTelemetryRequestService,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metadata.sendtelemetry(
                service=MetadataSendTelemetryRequestService.LETTA_CODE,
                events=[
                    MetadataSendTelemetryRequestEventsItem_SessionStart(
                        timestamp="timestamp",
                        data=MetadataSendTelemetryRequestEventsItemSessionStartData(
                            session_id="session_id",
                            startup_command="startup_command",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sendtelemetry(
            service=service, events=events, request_options=request_options
        )
        return _response.data

    async def getstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetadataGetStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataGetStatusResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metadata.getstatus()


        asyncio.run(main())
        """
        _response = await self._raw_client.getstatus(request_options=request_options)
        return _response.data

    async def getuser(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetadataGetUserResponse:
        """
        Retrieve information about the current authenticated user including email, name, organization, and current project.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataGetUserResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metadata.getuser()


        asyncio.run(main())
        """
        _response = await self._raw_client.getuser(request_options=request_options)
        return _response.data
