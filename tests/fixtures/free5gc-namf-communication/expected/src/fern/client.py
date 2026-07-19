

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .individual_subscription_document.client import (
        AsyncIndividualSubscriptionDocumentClient,
        IndividualSubscriptionDocumentClient,
    )
    from .individual_ue_context_document.client import (
        AsyncIndividualUeContextDocumentClient,
        IndividualUeContextDocumentClient,
    )
    from .n1n2individual_subscription_document.client import (
        AsyncN1N2IndividualSubscriptionDocumentClient,
        N1N2IndividualSubscriptionDocumentClient,
    )
    from .n1n2message_collection_document.client import (
        AsyncN1N2MessageCollectionDocumentClient,
        N1N2MessageCollectionDocumentClient,
    )
    from .n1n2subscriptions_collection_for_individual_ue_contexts_document.client import (
        AsyncN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient,
        N1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient,
    )
    from .non_ue_n2message_notification_individual_subscription_document.client import (
        AsyncNonUeN2MessageNotificationIndividualSubscriptionDocumentClient,
        NonUeN2MessageNotificationIndividualSubscriptionDocumentClient,
    )
    from .non_ue_n2messages_collection_document.client import (
        AsyncNonUeN2MessagesCollectionDocumentClient,
        NonUeN2MessagesCollectionDocumentClient,
    )
    from .non_ue_n2messages_subscriptions_collection_document.client import (
        AsyncNonUeN2MessagesSubscriptionsCollectionDocumentClient,
        NonUeN2MessagesSubscriptionsCollectionDocumentClient,
    )
    from .subscriptions_collection_document.client import (
        AsyncSubscriptionsCollectionDocumentClient,
        SubscriptionsCollectionDocumentClient,
    )


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



    api_root : typing.Optional[str]
        Server URL variable for 'apiRoot'. Defaults to 'https://example.com'.

    token : typing.Union[str, typing.Callable[[], str]]
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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_root: typing.Optional[str] = None,
        token: typing.Union[str, typing.Callable[[], str]],
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
        if api_root is not None:
            _api_root = api_root if api_root is not None else "https://example.com"
            base_url = "{apiRoot}/namf-comm/v1".format(apiRoot=_api_root)
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
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
        self._individual_ue_context_document: typing.Optional[IndividualUeContextDocumentClient] = None
        self._n1n2message_collection_document: typing.Optional[N1N2MessageCollectionDocumentClient] = None
        self._n1n2subscriptions_collection_for_individual_ue_contexts_document: typing.Optional[
            N1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient
        ] = None
        self._n1n2individual_subscription_document: typing.Optional[N1N2IndividualSubscriptionDocumentClient] = None
        self._non_ue_n2messages_collection_document: typing.Optional[NonUeN2MessagesCollectionDocumentClient] = None
        self._non_ue_n2messages_subscriptions_collection_document: typing.Optional[
            NonUeN2MessagesSubscriptionsCollectionDocumentClient
        ] = None
        self._non_ue_n2message_notification_individual_subscription_document: typing.Optional[
            NonUeN2MessageNotificationIndividualSubscriptionDocumentClient
        ] = None
        self._subscriptions_collection_document: typing.Optional[SubscriptionsCollectionDocumentClient] = None
        self._individual_subscription_document: typing.Optional[IndividualSubscriptionDocumentClient] = None

    @property
    def individual_ue_context_document(self):
        if self._individual_ue_context_document is None:
            from .individual_ue_context_document.client import IndividualUeContextDocumentClient

            self._individual_ue_context_document = IndividualUeContextDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._individual_ue_context_document

    @property
    def n1n2message_collection_document(self):
        if self._n1n2message_collection_document is None:
            from .n1n2message_collection_document.client import N1N2MessageCollectionDocumentClient

            self._n1n2message_collection_document = N1N2MessageCollectionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._n1n2message_collection_document

    @property
    def n1n2subscriptions_collection_for_individual_ue_contexts_document(self):
        if self._n1n2subscriptions_collection_for_individual_ue_contexts_document is None:
            from .n1n2subscriptions_collection_for_individual_ue_contexts_document.client import (
                N1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient,
            )

            self._n1n2subscriptions_collection_for_individual_ue_contexts_document = (
                N1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient(client_wrapper=self._client_wrapper)
            )
        return self._n1n2subscriptions_collection_for_individual_ue_contexts_document

    @property
    def n1n2individual_subscription_document(self):
        if self._n1n2individual_subscription_document is None:
            from .n1n2individual_subscription_document.client import (
                N1N2IndividualSubscriptionDocumentClient,
            )

            self._n1n2individual_subscription_document = N1N2IndividualSubscriptionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._n1n2individual_subscription_document

    @property
    def non_ue_n2messages_collection_document(self):
        if self._non_ue_n2messages_collection_document is None:
            from .non_ue_n2messages_collection_document.client import (
                NonUeN2MessagesCollectionDocumentClient,
            )

            self._non_ue_n2messages_collection_document = NonUeN2MessagesCollectionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._non_ue_n2messages_collection_document

    @property
    def non_ue_n2messages_subscriptions_collection_document(self):
        if self._non_ue_n2messages_subscriptions_collection_document is None:
            from .non_ue_n2messages_subscriptions_collection_document.client import (
                NonUeN2MessagesSubscriptionsCollectionDocumentClient,
            )

            self._non_ue_n2messages_subscriptions_collection_document = (
                NonUeN2MessagesSubscriptionsCollectionDocumentClient(client_wrapper=self._client_wrapper)
            )
        return self._non_ue_n2messages_subscriptions_collection_document

    @property
    def non_ue_n2message_notification_individual_subscription_document(self):
        if self._non_ue_n2message_notification_individual_subscription_document is None:
            from .non_ue_n2message_notification_individual_subscription_document.client import (
                NonUeN2MessageNotificationIndividualSubscriptionDocumentClient,
            )

            self._non_ue_n2message_notification_individual_subscription_document = (
                NonUeN2MessageNotificationIndividualSubscriptionDocumentClient(client_wrapper=self._client_wrapper)
            )
        return self._non_ue_n2message_notification_individual_subscription_document

    @property
    def subscriptions_collection_document(self):
        if self._subscriptions_collection_document is None:
            from .subscriptions_collection_document.client import SubscriptionsCollectionDocumentClient

            self._subscriptions_collection_document = SubscriptionsCollectionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._subscriptions_collection_document

    @property
    def individual_subscription_document(self):
        if self._individual_subscription_document is None:
            from .individual_subscription_document.client import IndividualSubscriptionDocumentClient

            self._individual_subscription_document = IndividualSubscriptionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._individual_subscription_document


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
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_root : typing.Optional[str]
        Server URL variable for 'apiRoot'. Defaults to 'https://example.com'.

    token : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_root: typing.Optional[str] = None,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
        if api_root is not None:
            _api_root = api_root if api_root is not None else "https://example.com"
            base_url = "{apiRoot}/namf-comm/v1".format(apiRoot=_api_root)
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._individual_ue_context_document: typing.Optional[AsyncIndividualUeContextDocumentClient] = None
        self._n1n2message_collection_document: typing.Optional[AsyncN1N2MessageCollectionDocumentClient] = None
        self._n1n2subscriptions_collection_for_individual_ue_contexts_document: typing.Optional[
            AsyncN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient
        ] = None
        self._n1n2individual_subscription_document: typing.Optional[AsyncN1N2IndividualSubscriptionDocumentClient] = (
            None
        )
        self._non_ue_n2messages_collection_document: typing.Optional[AsyncNonUeN2MessagesCollectionDocumentClient] = (
            None
        )
        self._non_ue_n2messages_subscriptions_collection_document: typing.Optional[
            AsyncNonUeN2MessagesSubscriptionsCollectionDocumentClient
        ] = None
        self._non_ue_n2message_notification_individual_subscription_document: typing.Optional[
            AsyncNonUeN2MessageNotificationIndividualSubscriptionDocumentClient
        ] = None
        self._subscriptions_collection_document: typing.Optional[AsyncSubscriptionsCollectionDocumentClient] = None
        self._individual_subscription_document: typing.Optional[AsyncIndividualSubscriptionDocumentClient] = None

    @property
    def individual_ue_context_document(self):
        if self._individual_ue_context_document is None:
            from .individual_ue_context_document.client import AsyncIndividualUeContextDocumentClient

            self._individual_ue_context_document = AsyncIndividualUeContextDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._individual_ue_context_document

    @property
    def n1n2message_collection_document(self):
        if self._n1n2message_collection_document is None:
            from .n1n2message_collection_document.client import AsyncN1N2MessageCollectionDocumentClient

            self._n1n2message_collection_document = AsyncN1N2MessageCollectionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._n1n2message_collection_document

    @property
    def n1n2subscriptions_collection_for_individual_ue_contexts_document(self):
        if self._n1n2subscriptions_collection_for_individual_ue_contexts_document is None:
            from .n1n2subscriptions_collection_for_individual_ue_contexts_document.client import (
                AsyncN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient,
            )

            self._n1n2subscriptions_collection_for_individual_ue_contexts_document = (
                AsyncN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient(
                    client_wrapper=self._client_wrapper
                )
            )
        return self._n1n2subscriptions_collection_for_individual_ue_contexts_document

    @property
    def n1n2individual_subscription_document(self):
        if self._n1n2individual_subscription_document is None:
            from .n1n2individual_subscription_document.client import (
                AsyncN1N2IndividualSubscriptionDocumentClient,
            )

            self._n1n2individual_subscription_document = AsyncN1N2IndividualSubscriptionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._n1n2individual_subscription_document

    @property
    def non_ue_n2messages_collection_document(self):
        if self._non_ue_n2messages_collection_document is None:
            from .non_ue_n2messages_collection_document.client import (
                AsyncNonUeN2MessagesCollectionDocumentClient,
            )

            self._non_ue_n2messages_collection_document = AsyncNonUeN2MessagesCollectionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._non_ue_n2messages_collection_document

    @property
    def non_ue_n2messages_subscriptions_collection_document(self):
        if self._non_ue_n2messages_subscriptions_collection_document is None:
            from .non_ue_n2messages_subscriptions_collection_document.client import (
                AsyncNonUeN2MessagesSubscriptionsCollectionDocumentClient,
            )

            self._non_ue_n2messages_subscriptions_collection_document = (
                AsyncNonUeN2MessagesSubscriptionsCollectionDocumentClient(client_wrapper=self._client_wrapper)
            )
        return self._non_ue_n2messages_subscriptions_collection_document

    @property
    def non_ue_n2message_notification_individual_subscription_document(self):
        if self._non_ue_n2message_notification_individual_subscription_document is None:
            from .non_ue_n2message_notification_individual_subscription_document.client import (
                AsyncNonUeN2MessageNotificationIndividualSubscriptionDocumentClient,
            )

            self._non_ue_n2message_notification_individual_subscription_document = (
                AsyncNonUeN2MessageNotificationIndividualSubscriptionDocumentClient(client_wrapper=self._client_wrapper)
            )
        return self._non_ue_n2message_notification_individual_subscription_document

    @property
    def subscriptions_collection_document(self):
        if self._subscriptions_collection_document is None:
            from .subscriptions_collection_document.client import (
                AsyncSubscriptionsCollectionDocumentClient,
            )

            self._subscriptions_collection_document = AsyncSubscriptionsCollectionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._subscriptions_collection_document

    @property
    def individual_subscription_document(self):
        if self._individual_subscription_document is None:
            from .individual_subscription_document.client import AsyncIndividualSubscriptionDocumentClient

            self._individual_subscription_document = AsyncIndividualSubscriptionDocumentClient(
                client_wrapper=self._client_wrapper
            )
        return self._individual_subscription_document


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
