

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawApplicationClient, RawApplicationClient
from .types.ai_gateway_create_response import AiGatewayCreateResponse
from .types.application_all_response_item import ApplicationAllResponseItem
from .types.application_create_response import ApplicationCreateResponse
from .types.application_delete_response import ApplicationDeleteResponse
from .types.application_event_stats_request_unit import ApplicationEventStatsRequestUnit
from .types.application_event_stats_response import ApplicationEventStatsResponse
from .types.application_info_response import ApplicationInfoResponse
from .types.application_store_app_search_request_store_type import ApplicationStoreAppSearchRequestStoreType
from .types.application_store_app_search_response_item import ApplicationStoreAppSearchResponseItem
from .types.application_store_info_history_request_store_type import ApplicationStoreInfoHistoryRequestStoreType
from .types.application_store_info_history_response_item import ApplicationStoreInfoHistoryResponseItem
from .types.application_update_response import ApplicationUpdateResponse


OMIT = typing.cast(typing.Any, ...)


class ApplicationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplicationClient
        """
        return self._raw_client

    def ai_gateway_create(
        self,
        workspace_id: str,
        *,
        name: str,
        model_api_key: typing.Optional[str] = OMIT,
        custom_model_base_url: typing.Optional[str] = OMIT,
        custom_model_name: typing.Optional[str] = OMIT,
        custom_model_input_price: typing.Optional[float] = OMIT,
        custom_model_output_price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayCreateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        model_api_key : typing.Optional[str]

        custom_model_base_url : typing.Optional[str]

        custom_model_name : typing.Optional[str]

        custom_model_input_price : typing.Optional[float]

        custom_model_output_price : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayCreateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.ai_gateway_create(
            workspace_id="workspaceId",
            name="name",
        )
        """
        _response = self._raw_client.ai_gateway_create(
            workspace_id,
            name=name,
            model_api_key=model_api_key,
            custom_model_base_url=custom_model_base_url,
            custom_model_name=custom_model_name,
            custom_model_input_price=custom_model_input_price,
            custom_model_output_price=custom_model_output_price,
            request_options=request_options,
        )
        return _response.data

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApplicationAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.all_(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    def info(
        self, workspace_id: str, application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ApplicationInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ApplicationInfoResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.info(
            workspace_id="workspaceId",
            application_id="applicationId",
        )
        """
        _response = self._raw_client.info(workspace_id, application_id, request_options=request_options)
        return _response.data

    def create(
        self,
        workspace_id: str,
        *,
        name: str,
        appstore_id: typing.Optional[str] = OMIT,
        playstore_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCreateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        appstore_id : typing.Optional[str]

        playstore_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCreateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.create(
            workspace_id="workspaceId",
            name="name",
        )
        """
        _response = self._raw_client.create(
            workspace_id, name=name, appstore_id=appstore_id, playstore_id=playstore_id, request_options=request_options
        )
        return _response.data

    def update(
        self,
        workspace_id: str,
        application_id: str,
        *,
        name: str,
        appstore_id: typing.Optional[str] = OMIT,
        playstore_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationUpdateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        name : str

        appstore_id : typing.Optional[str]

        playstore_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationUpdateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.update(
            workspace_id="workspaceId",
            application_id="applicationId",
            name="name",
        )
        """
        _response = self._raw_client.update(
            workspace_id,
            application_id,
            name=name,
            appstore_id=appstore_id,
            playstore_id=playstore_id,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, workspace_id: str, application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.delete(
            workspace_id="workspaceId",
            application_id="applicationId",
        )
        """
        _response = self._raw_client.delete(workspace_id, application_id, request_options=request_options)
        return _response.data

    def storeappsearch(
        self,
        *,
        workspace_id: str,
        keyword: str,
        store_type: ApplicationStoreAppSearchRequestStoreType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ApplicationStoreAppSearchResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        keyword : str

        store_type : ApplicationStoreAppSearchRequestStoreType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationStoreAppSearchResponseItem]
            Successful response

        Examples
        --------
        from fern.application import ApplicationStoreAppSearchRequestStoreType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.storeappsearch(
            workspace_id="workspaceId",
            keyword="keyword",
            store_type=ApplicationStoreAppSearchRequestStoreType.APPSTORE,
        )
        """
        _response = self._raw_client.storeappsearch(
            workspace_id=workspace_id, keyword=keyword, store_type=store_type, request_options=request_options
        )
        return _response.data

    def storeinfohistory(
        self,
        workspace_id: str,
        application_id: str,
        *,
        store_type: ApplicationStoreInfoHistoryRequestStoreType,
        start_at: float,
        end_at: float,
        store_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ApplicationStoreInfoHistoryResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        store_type : ApplicationStoreInfoHistoryRequestStoreType

        start_at : float

        end_at : float

        store_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationStoreInfoHistoryResponseItem]
            Successful response

        Examples
        --------
        from fern.application import ApplicationStoreInfoHistoryRequestStoreType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.storeinfohistory(
            workspace_id="workspaceId",
            application_id="applicationId",
            store_type=ApplicationStoreInfoHistoryRequestStoreType.APPSTORE,
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.storeinfohistory(
            workspace_id,
            application_id,
            store_type=store_type,
            start_at=start_at,
            end_at=end_at,
            store_id=store_id,
            request_options=request_options,
        )
        return _response.data

    def eventstats(
        self,
        workspace_id: str,
        application_id: str,
        *,
        start_at: float,
        end_at: float,
        timezone: typing.Optional[str] = None,
        unit: typing.Optional[ApplicationEventStatsRequestUnit] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationEventStatsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        start_at : float

        end_at : float

        timezone : typing.Optional[str]

        unit : typing.Optional[ApplicationEventStatsRequestUnit]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationEventStatsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.application.eventstats(
            workspace_id="workspaceId",
            application_id="applicationId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.eventstats(
            workspace_id,
            application_id,
            start_at=start_at,
            end_at=end_at,
            timezone=timezone,
            unit=unit,
            request_options=request_options,
        )
        return _response.data


class AsyncApplicationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplicationClient
        """
        return self._raw_client

    async def ai_gateway_create(
        self,
        workspace_id: str,
        *,
        name: str,
        model_api_key: typing.Optional[str] = OMIT,
        custom_model_base_url: typing.Optional[str] = OMIT,
        custom_model_name: typing.Optional[str] = OMIT,
        custom_model_input_price: typing.Optional[float] = OMIT,
        custom_model_output_price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayCreateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        model_api_key : typing.Optional[str]

        custom_model_base_url : typing.Optional[str]

        custom_model_name : typing.Optional[str]

        custom_model_input_price : typing.Optional[float]

        custom_model_output_price : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.ai_gateway_create(
                workspace_id="workspaceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_create(
            workspace_id,
            name=name,
            model_api_key=model_api_key,
            custom_model_base_url=custom_model_base_url,
            custom_model_name=custom_model_name,
            custom_model_input_price=custom_model_input_price,
            custom_model_output_price=custom_model_output_price,
            request_options=request_options,
        )
        return _response.data

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApplicationAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.all_(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    async def info(
        self, workspace_id: str, application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ApplicationInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ApplicationInfoResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.info(
                workspace_id="workspaceId",
                application_id="applicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.info(workspace_id, application_id, request_options=request_options)
        return _response.data

    async def create(
        self,
        workspace_id: str,
        *,
        name: str,
        appstore_id: typing.Optional[str] = OMIT,
        playstore_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCreateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        appstore_id : typing.Optional[str]

        playstore_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.create(
                workspace_id="workspaceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            workspace_id, name=name, appstore_id=appstore_id, playstore_id=playstore_id, request_options=request_options
        )
        return _response.data

    async def update(
        self,
        workspace_id: str,
        application_id: str,
        *,
        name: str,
        appstore_id: typing.Optional[str] = OMIT,
        playstore_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationUpdateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        name : str

        appstore_id : typing.Optional[str]

        playstore_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationUpdateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.update(
                workspace_id="workspaceId",
                application_id="applicationId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            workspace_id,
            application_id,
            name=name,
            appstore_id=appstore_id,
            playstore_id=playstore_id,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, workspace_id: str, application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.delete(
                workspace_id="workspaceId",
                application_id="applicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(workspace_id, application_id, request_options=request_options)
        return _response.data

    async def storeappsearch(
        self,
        *,
        workspace_id: str,
        keyword: str,
        store_type: ApplicationStoreAppSearchRequestStoreType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ApplicationStoreAppSearchResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        keyword : str

        store_type : ApplicationStoreAppSearchRequestStoreType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationStoreAppSearchResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern.application import ApplicationStoreAppSearchRequestStoreType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.storeappsearch(
                workspace_id="workspaceId",
                keyword="keyword",
                store_type=ApplicationStoreAppSearchRequestStoreType.APPSTORE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.storeappsearch(
            workspace_id=workspace_id, keyword=keyword, store_type=store_type, request_options=request_options
        )
        return _response.data

    async def storeinfohistory(
        self,
        workspace_id: str,
        application_id: str,
        *,
        store_type: ApplicationStoreInfoHistoryRequestStoreType,
        start_at: float,
        end_at: float,
        store_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ApplicationStoreInfoHistoryResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        store_type : ApplicationStoreInfoHistoryRequestStoreType

        start_at : float

        end_at : float

        store_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationStoreInfoHistoryResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern.application import ApplicationStoreInfoHistoryRequestStoreType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.storeinfohistory(
                workspace_id="workspaceId",
                application_id="applicationId",
                store_type=ApplicationStoreInfoHistoryRequestStoreType.APPSTORE,
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.storeinfohistory(
            workspace_id,
            application_id,
            store_type=store_type,
            start_at=start_at,
            end_at=end_at,
            store_id=store_id,
            request_options=request_options,
        )
        return _response.data

    async def eventstats(
        self,
        workspace_id: str,
        application_id: str,
        *,
        start_at: float,
        end_at: float,
        timezone: typing.Optional[str] = None,
        unit: typing.Optional[ApplicationEventStatsRequestUnit] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationEventStatsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        application_id : str

        start_at : float

        end_at : float

        timezone : typing.Optional[str]

        unit : typing.Optional[ApplicationEventStatsRequestUnit]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationEventStatsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.application.eventstats(
                workspace_id="workspaceId",
                application_id="applicationId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eventstats(
            workspace_id,
            application_id,
            start_at=start_at,
            end_at=end_at,
            timezone=timezone,
            unit=unit,
            request_options=request_options,
        )
        return _response.data
