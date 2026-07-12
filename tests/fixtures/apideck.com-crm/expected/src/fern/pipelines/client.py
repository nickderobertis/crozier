

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_pipeline_response import CreatePipelineResponse
from ..types.currency import Currency
from ..types.delete_pipeline_response import DeletePipelineResponse
from ..types.get_pipeline_response import GetPipelineResponse
from ..types.get_pipelines_response import GetPipelinesResponse
from ..types.pipeline_stages_item import PipelineStagesItem
from ..types.update_pipeline_response import UpdatePipelineResponse
from .raw_client import AsyncRawPipelinesClient, RawPipelinesClient


OMIT = typing.cast(typing.Any, ...)


class PipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPipelinesClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPipelinesResponse:
        """
        List pipelines

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPipelinesResponse
            Pipelines

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.pipelines.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        stages: typing.Optional[typing.Sequence[PipelineStagesItem]] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        win_probability_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePipelineResponse:
        """
        Create pipeline

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        archived : typing.Optional[bool]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        currency : typing.Optional[Currency]

        display_order : typing.Optional[int]

        id : typing.Optional[str]

        stages : typing.Optional[typing.Sequence[PipelineStagesItem]]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        win_probability_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePipelineResponse
            Pipeline created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.pipelines.add(
            name="Sales Pipeline",
        )
        """
        _response = self._raw_client.add(
            name=name,
            raw=raw,
            active=active,
            archived=archived,
            created_at=created_at,
            currency=currency,
            display_order=display_order,
            id=id,
            stages=stages,
            updated_at=updated_at,
            win_probability_enabled=win_probability_enabled,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPipelineResponse:
        """
        Get pipeline

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPipelineResponse
            Pipeline

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.pipelines.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePipelineResponse:
        """
        Delete pipeline

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePipelineResponse
            Pipeline deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.pipelines.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        stages: typing.Optional[typing.Sequence[PipelineStagesItem]] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        win_probability_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePipelineResponse:
        """
        Update pipeline

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        archived : typing.Optional[bool]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        currency : typing.Optional[Currency]

        display_order : typing.Optional[int]

        id : typing.Optional[str]

        stages : typing.Optional[typing.Sequence[PipelineStagesItem]]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        win_probability_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePipelineResponse
            Pipeline updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.pipelines.update(
            id_="id",
            name="Sales Pipeline",
        )
        """
        _response = self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            active=active,
            archived=archived,
            created_at=created_at,
            currency=currency,
            display_order=display_order,
            id=id,
            stages=stages,
            updated_at=updated_at,
            win_probability_enabled=win_probability_enabled,
            request_options=request_options,
        )
        return _response.data


class AsyncPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPipelinesClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPipelinesResponse:
        """
        List pipelines

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPipelinesResponse
            Pipelines

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipelines.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        stages: typing.Optional[typing.Sequence[PipelineStagesItem]] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        win_probability_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePipelineResponse:
        """
        Create pipeline

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        archived : typing.Optional[bool]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        currency : typing.Optional[Currency]

        display_order : typing.Optional[int]

        id : typing.Optional[str]

        stages : typing.Optional[typing.Sequence[PipelineStagesItem]]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        win_probability_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePipelineResponse
            Pipeline created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipelines.add(
                name="Sales Pipeline",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            name=name,
            raw=raw,
            active=active,
            archived=archived,
            created_at=created_at,
            currency=currency,
            display_order=display_order,
            id=id,
            stages=stages,
            updated_at=updated_at,
            win_probability_enabled=win_probability_enabled,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPipelineResponse:
        """
        Get pipeline

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPipelineResponse
            Pipeline

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipelines.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePipelineResponse:
        """
        Delete pipeline

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePipelineResponse
            Pipeline deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipelines.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_order: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        stages: typing.Optional[typing.Sequence[PipelineStagesItem]] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        win_probability_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePipelineResponse:
        """
        Update pipeline

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        archived : typing.Optional[bool]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        currency : typing.Optional[Currency]

        display_order : typing.Optional[int]

        id : typing.Optional[str]

        stages : typing.Optional[typing.Sequence[PipelineStagesItem]]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        win_probability_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePipelineResponse
            Pipeline updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipelines.update(
                id_="id",
                name="Sales Pipeline",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            active=active,
            archived=archived,
            created_at=created_at,
            currency=currency,
            display_order=display_order,
            id=id,
            stages=stages,
            updated_at=updated_at,
            win_probability_enabled=win_probability_enabled,
            request_options=request_options,
        )
        return _response.data
