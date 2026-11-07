

import datetime as dt
import typing

import httpx
from . import core
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.create_profile_request_role import CreateProfileRequestRole
from .types.mutation_nullable_response import MutationNullableResponse
from .types.mutation_pattern_payload_region import MutationPatternPayloadRegion
from .types.mutation_strict_object_payload_profile import MutationStrictObjectPayloadProfile
from .types.ok_response import OkResponse
from .types.prepare_upload_meta_request_content_type import PrepareUploadMetaRequestContentType
from .types.profile_response import ProfileResponse
from .types.ref_parameter_candidate_request_locale import RefParameterCandidateRequestLocale
from .types.search_profiles_response import SearchProfilesResponse
from .types.union_candidate_request import UnionCandidateRequest
from .types.update_preferences_request_theme import UpdatePreferencesRequestTheme
from .types.upload_meta_response import UploadMetaResponse


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
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

    def create_profile(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfileResponse:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_profile(
            display_name="display_name",
            email="email",
            contact_phone="contact_phone",
            tags=["tags"],
            role="user",
        )
        """
        _response = self._raw_client.create_profile(
            display_name=display_name,
            email=email,
            contact_phone=contact_phone,
            tags=tags,
            role=role,
            homepage=homepage,
            callback_url=callback_url,
            birth_date=birth_date,
            last_login_at=last_login_at,
            avatar_base64=avatar_base64,
            tenant_host=tenant_host,
            source_ip=source_ip,
            login_count=login_count,
            request_options=request_options,
        )
        return _response.data

    def update_preferences(
        self,
        *,
        theme: UpdatePreferencesRequestTheme,
        timezone: str,
        daily_digest: typing.Optional[bool] = OMIT,
        weekly_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        theme : UpdatePreferencesRequestTheme

        timezone : str

        daily_digest : typing.Optional[bool]

        weekly_limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_preferences(
            theme="light",
            timezone="",
        )
        """
        _response = self._raw_client.update_preferences(
            theme=theme,
            timezone=timezone,
            daily_digest=daily_digest,
            weekly_limit=weekly_limit,
            request_options=request_options,
        )
        return _response.data

    def prepare_upload_meta(
        self,
        *,
        bucket: str,
        object_key: str,
        content_type: PrepareUploadMetaRequestContentType,
        size_bytes: int,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadMetaResponse:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        content_type : PrepareUploadMetaRequestContentType

        size_bytes : int

        checksum : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadMetaResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prepare_upload_meta(
            bucket="bucket",
            object_key="object_key",
            content_type="image/png",
            size_bytes=1000000,
        )
        """
        _response = self._raw_client.prepare_upload_meta(
            bucket=bucket,
            object_key=object_key,
            content_type=content_type,
            size_bytes=size_bytes,
            checksum=checksum,
            request_options=request_options,
        )
        return _response.data

    def search_profiles(
        self,
        *,
        keyword: str,
        request_id: str,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchProfilesResponse:
        """


        Parameters
        ----------
        keyword : str


        request_id : str


        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        page_size : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchProfilesResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.search_profiles(
            request_id="X-Request-Id",
            keyword="keyword",
        )
        """
        _response = self._raw_client.search_profiles(
            keyword=keyword, request_id=request_id, tags=tags, page_size=page_size, request_options=request_options
        )
        return _response.data

    def validate_raw_json(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> OkResponse:
        """


        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.validate_raw_json(
            request="string",
        )
        """
        _response = self._raw_client.validate_raw_json(request=request, request_options=request_options)
        return _response.data

    def pattern_candidate(
        self,
        *,
        phone: str,
        region: MutationPatternPayloadRegion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        phone : str

        region : MutationPatternPayloadRegion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pattern_candidate(
            phone="phone",
            region="CN",
        )
        """
        _response = self._raw_client.pattern_candidate(phone=phone, region=region, request_options=request_options)
        return _response.data

    def multiple_of_candidate(
        self, *, price: float, quantity: int, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """


        Parameters
        ----------
        price : float

        quantity : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.multiple_of_candidate(
            price=1.1,
            quantity=1,
        )
        """
        _response = self._raw_client.multiple_of_candidate(
            price=price, quantity=quantity, request_options=request_options
        )
        return _response.data

    def strict_object_candidate(
        self, *, profile: MutationStrictObjectPayloadProfile, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """


        Parameters
        ----------
        profile : MutationStrictObjectPayloadProfile

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi, MutationStrictObjectPayloadProfile

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.strict_object_candidate(
            profile=MutationStrictObjectPayloadProfile(
                source="manual",
                region="region",
            ),
        )
        """
        _response = self._raw_client.strict_object_candidate(profile=profile, request_options=request_options)
        return _response.data

    def nullable_any_of_candidate(
        self, *, nickname: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> MutationNullableResponse:
        """


        Parameters
        ----------
        nickname : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MutationNullableResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.nullable_any_of_candidate()
        """
        _response = self._raw_client.nullable_any_of_candidate(nickname=nickname, request_options=request_options)
        return _response.data

    def union_candidate(
        self, *, request: UnionCandidateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """


        Parameters
        ----------
        request : UnionCandidateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi, MutationUnionPayload

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.union_candidate(
            request=MutationUnionPayload(
                contact_kind="email",
                value="value",
            ),
        )
        """
        _response = self._raw_client.union_candidate(request=request, request_options=request_options)
        return _response.data

    def query_object_candidate(
        self,
        *,
        filter_keyword: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        filter_keyword : typing.Optional[str]


        limit : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.query_object_candidate()
        """
        _response = self._raw_client.query_object_candidate(
            filter_keyword=filter_keyword, limit=limit, request_options=request_options
        )
        return _response.data

    def query_array_candidate(
        self,
        *,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.query_array_candidate()
        """
        _response = self._raw_client.query_array_candidate(tags=tags, request_options=request_options)
        return _response.data

    def upload_file_candidate(
        self,
        *,
        bucket: str,
        object_key: str,
        checksum: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        checksum : typing.Optional[str]

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.upload_file_candidate(
            bucket="bucket",
            object_key="object_key",
        )
        """
        _response = self._raw_client.upload_file_candidate(
            bucket=bucket, object_key=object_key, checksum=checksum, file=file, request_options=request_options
        )
        return _response.data

    def ref_request_body_candidate(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ref_request_body_candidate(
            display_name="display_name",
            email="email",
            contact_phone="contact_phone",
            tags=["tags"],
            role="user",
        )
        """
        _response = self._raw_client.ref_request_body_candidate(
            display_name=display_name,
            email=email,
            contact_phone=contact_phone,
            tags=tags,
            role=role,
            homepage=homepage,
            callback_url=callback_url,
            birth_date=birth_date,
            last_login_at=last_login_at,
            avatar_base64=avatar_base64,
            tenant_host=tenant_host,
            source_ip=source_ip,
            login_count=login_count,
            request_options=request_options,
        )
        return _response.data

    def ref_parameter_candidate(
        self,
        item_id: str,
        *,
        locale: typing.Optional[RefParameterCandidateRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        item_id : str


        locale : typing.Optional[RefParameterCandidateRequestLocale]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ref_parameter_candidate(
            item_id="item_id",
        )
        """
        _response = self._raw_client.ref_parameter_candidate(item_id, locale=locale, request_options=request_options)
        return _response.data

    def multi2xx_candidate(self, *, request_options: typing.Optional[RequestOptions] = None) -> OkResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.multi2xx_candidate()
        """
        _response = self._raw_client.multi2xx_candidate(request_options=request_options)
        return _response.data

    def non_json_success_candidate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            ok
        """
        with self._raw_client.non_json_success_candidate(request_options=request_options) as r:
            yield from r.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
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

    async def create_profile(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfileResponse:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_profile(
                display_name="display_name",
                email="email",
                contact_phone="contact_phone",
                tags=["tags"],
                role="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_profile(
            display_name=display_name,
            email=email,
            contact_phone=contact_phone,
            tags=tags,
            role=role,
            homepage=homepage,
            callback_url=callback_url,
            birth_date=birth_date,
            last_login_at=last_login_at,
            avatar_base64=avatar_base64,
            tenant_host=tenant_host,
            source_ip=source_ip,
            login_count=login_count,
            request_options=request_options,
        )
        return _response.data

    async def update_preferences(
        self,
        *,
        theme: UpdatePreferencesRequestTheme,
        timezone: str,
        daily_digest: typing.Optional[bool] = OMIT,
        weekly_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        theme : UpdatePreferencesRequestTheme

        timezone : str

        daily_digest : typing.Optional[bool]

        weekly_limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_preferences(
                theme="light",
                timezone="",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_preferences(
            theme=theme,
            timezone=timezone,
            daily_digest=daily_digest,
            weekly_limit=weekly_limit,
            request_options=request_options,
        )
        return _response.data

    async def prepare_upload_meta(
        self,
        *,
        bucket: str,
        object_key: str,
        content_type: PrepareUploadMetaRequestContentType,
        size_bytes: int,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadMetaResponse:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        content_type : PrepareUploadMetaRequestContentType

        size_bytes : int

        checksum : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadMetaResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prepare_upload_meta(
                bucket="bucket",
                object_key="object_key",
                content_type="image/png",
                size_bytes=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prepare_upload_meta(
            bucket=bucket,
            object_key=object_key,
            content_type=content_type,
            size_bytes=size_bytes,
            checksum=checksum,
            request_options=request_options,
        )
        return _response.data

    async def search_profiles(
        self,
        *,
        keyword: str,
        request_id: str,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchProfilesResponse:
        """


        Parameters
        ----------
        keyword : str


        request_id : str


        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        page_size : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchProfilesResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.search_profiles(
                request_id="X-Request-Id",
                keyword="keyword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_profiles(
            keyword=keyword, request_id=request_id, tags=tags, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def validate_raw_json(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """


        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.validate_raw_json(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_raw_json(request=request, request_options=request_options)
        return _response.data

    async def pattern_candidate(
        self,
        *,
        phone: str,
        region: MutationPatternPayloadRegion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        phone : str

        region : MutationPatternPayloadRegion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pattern_candidate(
                phone="phone",
                region="CN",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pattern_candidate(
            phone=phone, region=region, request_options=request_options
        )
        return _response.data

    async def multiple_of_candidate(
        self, *, price: float, quantity: int, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """


        Parameters
        ----------
        price : float

        quantity : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.multiple_of_candidate(
                price=1.1,
                quantity=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.multiple_of_candidate(
            price=price, quantity=quantity, request_options=request_options
        )
        return _response.data

    async def strict_object_candidate(
        self, *, profile: MutationStrictObjectPayloadProfile, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """


        Parameters
        ----------
        profile : MutationStrictObjectPayloadProfile

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MutationStrictObjectPayloadProfile

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.strict_object_candidate(
                profile=MutationStrictObjectPayloadProfile(
                    source="manual",
                    region="region",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.strict_object_candidate(profile=profile, request_options=request_options)
        return _response.data

    async def nullable_any_of_candidate(
        self, *, nickname: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> MutationNullableResponse:
        """


        Parameters
        ----------
        nickname : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MutationNullableResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nullable_any_of_candidate()


        asyncio.run(main())
        """
        _response = await self._raw_client.nullable_any_of_candidate(nickname=nickname, request_options=request_options)
        return _response.data

    async def union_candidate(
        self, *, request: UnionCandidateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """


        Parameters
        ----------
        request : UnionCandidateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MutationUnionPayload

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.union_candidate(
                request=MutationUnionPayload(
                    contact_kind="email",
                    value="value",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.union_candidate(request=request, request_options=request_options)
        return _response.data

    async def query_object_candidate(
        self,
        *,
        filter_keyword: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        filter_keyword : typing.Optional[str]


        limit : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.query_object_candidate()


        asyncio.run(main())
        """
        _response = await self._raw_client.query_object_candidate(
            filter_keyword=filter_keyword, limit=limit, request_options=request_options
        )
        return _response.data

    async def query_array_candidate(
        self,
        *,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.query_array_candidate()


        asyncio.run(main())
        """
        _response = await self._raw_client.query_array_candidate(tags=tags, request_options=request_options)
        return _response.data

    async def upload_file_candidate(
        self,
        *,
        bucket: str,
        object_key: str,
        checksum: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        checksum : typing.Optional[str]

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.upload_file_candidate(
                bucket="bucket",
                object_key="object_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file_candidate(
            bucket=bucket, object_key=object_key, checksum=checksum, file=file, request_options=request_options
        )
        return _response.data

    async def ref_request_body_candidate(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ref_request_body_candidate(
                display_name="display_name",
                email="email",
                contact_phone="contact_phone",
                tags=["tags"],
                role="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ref_request_body_candidate(
            display_name=display_name,
            email=email,
            contact_phone=contact_phone,
            tags=tags,
            role=role,
            homepage=homepage,
            callback_url=callback_url,
            birth_date=birth_date,
            last_login_at=last_login_at,
            avatar_base64=avatar_base64,
            tenant_host=tenant_host,
            source_ip=source_ip,
            login_count=login_count,
            request_options=request_options,
        )
        return _response.data

    async def ref_parameter_candidate(
        self,
        item_id: str,
        *,
        locale: typing.Optional[RefParameterCandidateRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponse:
        """


        Parameters
        ----------
        item_id : str


        locale : typing.Optional[RefParameterCandidateRequestLocale]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ref_parameter_candidate(
                item_id="item_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ref_parameter_candidate(
            item_id, locale=locale, request_options=request_options
        )
        return _response.data

    async def multi2xx_candidate(self, *, request_options: typing.Optional[RequestOptions] = None) -> OkResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.multi2xx_candidate()


        asyncio.run(main())
        """
        _response = await self._raw_client.multi2xx_candidate(request_options=request_options)
        return _response.data

    async def non_json_success_candidate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            ok
        """
        async with self._raw_client.non_json_success_candidate(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
