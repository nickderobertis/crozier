

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.bulk_mapping_job import BulkMappingJob
from .types.bulk_mapping_job_result import BulkMappingJobResult
from .types.get_mapping_values_key_request_key import GetMappingValuesKeyRequestKey
from .types.get_mapping_values_key_response import GetMappingValuesKeyResponse


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def post_mapping(
        self, *, request: BulkMappingJob, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkMappingJobResult:
        """
        Allows mapping from third-party identifiers to FIGIs.

        Parameters
        ----------
        request : BulkMappingJob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkMappingJobResult
            A list of FIGIs and their metadata.

        Examples
        --------
        from fern import FernApi, MappingJob, MappingJobIdType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_mapping(
            request=[
                MappingJob(
                    id_type=MappingJobIdType.ID_ISIN,
                    id_value="idValue",
                )
            ],
        )
        """
        _response = self._raw_client.post_mapping(request=request, request_options=request_options)
        return _response.data

    def get_mapping_values_key(
        self, key: GetMappingValuesKeyRequestKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMappingValuesKeyResponse:
        """
        Get values for enum-like fields.

        Parameters
        ----------
        key : GetMappingValuesKeyRequestKey
            Key of MappingJob for which to get possible values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMappingValuesKeyResponse
            The list of values.

        Examples
        --------
        from fern import FernApi, GetMappingValuesKeyRequestKey

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_mapping_values_key(
            key=GetMappingValuesKeyRequestKey.ID_TYPE,
        )
        """
        _response = self._raw_client.get_mapping_values_key(key, request_options=request_options)
        return _response.data


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def post_mapping(
        self, *, request: BulkMappingJob, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkMappingJobResult:
        """
        Allows mapping from third-party identifiers to FIGIs.

        Parameters
        ----------
        request : BulkMappingJob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkMappingJobResult
            A list of FIGIs and their metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MappingJob, MappingJobIdType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_mapping(
                request=[
                    MappingJob(
                        id_type=MappingJobIdType.ID_ISIN,
                        id_value="idValue",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_mapping(request=request, request_options=request_options)
        return _response.data

    async def get_mapping_values_key(
        self, key: GetMappingValuesKeyRequestKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMappingValuesKeyResponse:
        """
        Get values for enum-like fields.

        Parameters
        ----------
        key : GetMappingValuesKeyRequestKey
            Key of MappingJob for which to get possible values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMappingValuesKeyResponse
            The list of values.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GetMappingValuesKeyRequestKey

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_mapping_values_key(
                key=GetMappingValuesKeyRequestKey.ID_TYPE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mapping_values_key(key, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
