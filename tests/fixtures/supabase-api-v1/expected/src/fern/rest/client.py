

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.postgrest_config_with_jwt_secret_response_output import PostgrestConfigWithJwtSecretResponseOutput
from ..types.v1postgrest_config_response_output import V1PostgrestConfigResponseOutput
from .raw_client import AsyncRawRestClient, RawRestClient


OMIT = typing.cast(typing.Any, ...)


class RestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRestClient
        """
        return self._raw_client

    def v1get_postgrest_service_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostgrestConfigWithJwtSecretResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostgrestConfigWithJwtSecretResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rest.v1get_postgrest_service_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_postgrest_service_config(ref, request_options=request_options)
        return _response.data

    def v1update_postgrest_service_config(
        self,
        ref: str,
        *,
        db_extra_search_path: typing.Optional[str] = OMIT,
        db_schema: typing.Optional[str] = OMIT,
        max_rows: typing.Optional[int] = OMIT,
        db_pool: typing.Optional[int] = OMIT,
        db_pool_acquisition_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1PostgrestConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        db_extra_search_path : typing.Optional[str]

        db_schema : typing.Optional[str]

        max_rows : typing.Optional[int]

        db_pool : typing.Optional[int]

        db_pool_acquisition_timeout : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1PostgrestConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rest.v1update_postgrest_service_config(
            ref="abcdefghijklmnopqrst",
            db_schema="public,storage",
            max_rows=1000,
            db_pool=20,
        )
        """
        _response = self._raw_client.v1update_postgrest_service_config(
            ref,
            db_extra_search_path=db_extra_search_path,
            db_schema=db_schema,
            max_rows=max_rows,
            db_pool=db_pool,
            db_pool_acquisition_timeout=db_pool_acquisition_timeout,
            request_options=request_options,
        )
        return _response.data


class AsyncRestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRestClient
        """
        return self._raw_client

    async def v1get_postgrest_service_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostgrestConfigWithJwtSecretResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostgrestConfigWithJwtSecretResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rest.v1get_postgrest_service_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_postgrest_service_config(ref, request_options=request_options)
        return _response.data

    async def v1update_postgrest_service_config(
        self,
        ref: str,
        *,
        db_extra_search_path: typing.Optional[str] = OMIT,
        db_schema: typing.Optional[str] = OMIT,
        max_rows: typing.Optional[int] = OMIT,
        db_pool: typing.Optional[int] = OMIT,
        db_pool_acquisition_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1PostgrestConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        db_extra_search_path : typing.Optional[str]

        db_schema : typing.Optional[str]

        max_rows : typing.Optional[int]

        db_pool : typing.Optional[int]

        db_pool_acquisition_timeout : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1PostgrestConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rest.v1update_postgrest_service_config(
                ref="abcdefghijklmnopqrst",
                db_schema="public,storage",
                max_rows=1000,
                db_pool=20,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_postgrest_service_config(
            ref,
            db_extra_search_path=db_extra_search_path,
            db_schema=db_schema,
            max_rows=max_rows,
            db_pool=db_pool,
            db_pool_acquisition_timeout=db_pool_acquisition_timeout,
            request_options=request_options,
        )
        return _response.data
