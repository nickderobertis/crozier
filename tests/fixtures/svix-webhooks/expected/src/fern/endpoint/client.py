

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_headers_out import EndpointHeadersOut
from ..types.endpoint_out import EndpointOut
from ..types.endpoint_secret_out import EndpointSecretOut
from ..types.endpoint_stats import EndpointStats
from ..types.list_response_endpoint_out import ListResponseEndpointOut
from ..types.message_out import MessageOut
from ..types.ordering import Ordering
from ..types.recover_out import RecoverOut
from .raw_client import AsyncRawEndpointClient, RawEndpointClient


OMIT = typing.cast(typing.Any, ...)


class EndpointClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEndpointClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEndpointClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEndpointClient
        """
        return self._raw_client

    def v1endpoint_list(
        self,
        app_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseEndpointOut:
        """
        List the application's endpoints.

        Parameters
        ----------
        app_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseEndpointOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_list(
            app_id="unique-app-identifier",
            iterator="ep_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        )
        """
        _response = self._raw_client.v1endpoint_list(
            app_id, limit=limit, iterator=iterator, order=order, request_options=request_options
        )
        return _response.data

    def v1endpoint_create(
        self,
        app_id: str,
        *,
        url: str,
        idempotency_key: typing.Optional[str] = None,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointOut:
        """
        Create a new endpoint for the application.

        When `secret` is `null` the secret is automatically generated (recommended)

        Parameters
        ----------
        app_id : str

        url : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        secret : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_create(
            app_id="unique-app-identifier",
            url="https://example.com/webhook/",
        )
        """
        _response = self._raw_client.v1endpoint_create(
            app_id,
            url=url,
            idempotency_key=idempotency_key,
            channels=channels,
            description=description,
            disabled=disabled,
            event_types=event_types,
            metadata=metadata,
            secret=secret,
            throttle_rate=throttle_rate,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    def v1endpoint_get(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointOut:
        """
        Get an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_get(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.v1endpoint_get(app_id, endpoint_id, request_options=request_options)
        return _response.data

    def v1endpoint_update(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        url: str,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointOut:
        """
        Update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        url : str

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_update(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
            url="https://example.com/webhook/",
        )
        """
        _response = self._raw_client.v1endpoint_update(
            app_id,
            endpoint_id,
            url=url,
            channels=channels,
            description=description,
            disabled=disabled,
            event_types=event_types,
            metadata=metadata,
            throttle_rate=throttle_rate,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    def v1endpoint_delete(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_delete(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.v1endpoint_delete(app_id, endpoint_id, request_options=request_options)
        return _response.data

    def patch_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointOut:
        """
        Partially update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        channels : typing.Optional[typing.Sequence[str]]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.patch_endpoint(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.patch_endpoint(
            app_id,
            endpoint_id,
            channels=channels,
            description=description,
            disabled=disabled,
            event_types=event_types,
            metadata=metadata,
            throttle_rate=throttle_rate,
            uid=uid,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def v1endpoint_get_headers(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointHeadersOut:
        """
        Get the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointHeadersOut
            The value of the headers is returned in the `headers` field.

            Sensitive headers that have been redacted are returned in the sensitive field.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_get_headers(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.v1endpoint_get_headers(app_id, endpoint_id, request_options=request_options)
        return _response.data

    def v1endpoint_update_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_update_headers(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
            headers={"X-Example": "123", "X-Foobar": "Bar"},
        )
        """
        _response = self._raw_client.v1endpoint_update_headers(
            app_id, endpoint_id, headers=headers, request_options=request_options
        )
        return _response.data

    def v1endpoint_patch_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Partially set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_patch_headers(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
            headers={"X-Example": "123", "X-Foobar": "Bar"},
        )
        """
        _response = self._raw_client.v1endpoint_patch_headers(
            app_id, endpoint_id, headers=headers, request_options=request_options
        )
        return _response.data

    def v1endpoint_recover(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecoverOut:
        """
        Resend all failed messages since a given time.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : dt.datetime

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecoverOut


        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_recover(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
            since=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.v1endpoint_recover(
            app_id,
            endpoint_id,
            since=since,
            idempotency_key=idempotency_key,
            until=until,
            request_options=request_options,
        )
        return _response.data

    def v1endpoint_get_secret(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointSecretOut:
        """
        Get the endpoint's signing secret.

        This is used to verify the authenticity of the webhook.
        For more information please refer to [the consuming webhooks docs](https://docs.svix.com/consuming-webhooks/).

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointSecretOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_get_secret(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.v1endpoint_get_secret(app_id, endpoint_id, request_options=request_options)
        return _response.data

    def v1endpoint_rotate_secret(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Rotates the endpoint's signing secret.  The previous secret will be valid for the next 24 hours.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        grace_period_seconds : typing.Optional[int]
            How long the old secret will be valid for, in seconds.

            Valid values are between 0 (immediate expiry) and 7 days. The default is 24 hours.

        key : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_rotate_secret(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.v1endpoint_rotate_secret(
            app_id,
            endpoint_id,
            idempotency_key=idempotency_key,
            grace_period_seconds=grace_period_seconds,
            key=key,
            request_options=request_options,
        )
        return _response.data

    def v1endpoint_send_example(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        event_type: str,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageOut:
        """
        Send an example message for an event

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        event_type : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_send_example(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
            event_type="user.signup",
        )
        """
        _response = self._raw_client.v1endpoint_send_example(
            app_id, endpoint_id, event_type=event_type, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def v1endpoint_get_stats(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: typing.Optional[dt.datetime] = None,
        until: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointStats:
        """
        Get basic statistics for the endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : typing.Optional[dt.datetime]

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointStats


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoint.v1endpoint_get_stats(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.v1endpoint_get_stats(
            app_id, endpoint_id, since=since, until=until, request_options=request_options
        )
        return _response.data


class AsyncEndpointClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEndpointClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEndpointClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEndpointClient
        """
        return self._raw_client

    async def v1endpoint_list(
        self,
        app_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseEndpointOut:
        """
        List the application's endpoints.

        Parameters
        ----------
        app_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseEndpointOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_list(
                app_id="unique-app-identifier",
                iterator="ep_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_list(
            app_id, limit=limit, iterator=iterator, order=order, request_options=request_options
        )
        return _response.data

    async def v1endpoint_create(
        self,
        app_id: str,
        *,
        url: str,
        idempotency_key: typing.Optional[str] = None,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointOut:
        """
        Create a new endpoint for the application.

        When `secret` is `null` the secret is automatically generated (recommended)

        Parameters
        ----------
        app_id : str

        url : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        secret : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_create(
                app_id="unique-app-identifier",
                url="https://example.com/webhook/",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_create(
            app_id,
            url=url,
            idempotency_key=idempotency_key,
            channels=channels,
            description=description,
            disabled=disabled,
            event_types=event_types,
            metadata=metadata,
            secret=secret,
            throttle_rate=throttle_rate,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    async def v1endpoint_get(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointOut:
        """
        Get an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_get(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_get(app_id, endpoint_id, request_options=request_options)
        return _response.data

    async def v1endpoint_update(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        url: str,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointOut:
        """
        Update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        url : str

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_update(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
                url="https://example.com/webhook/",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_update(
            app_id,
            endpoint_id,
            url=url,
            channels=channels,
            description=description,
            disabled=disabled,
            event_types=event_types,
            metadata=metadata,
            throttle_rate=throttle_rate,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    async def v1endpoint_delete(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_delete(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_delete(app_id, endpoint_id, request_options=request_options)
        return _response.data

    async def patch_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointOut:
        """
        Partially update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        channels : typing.Optional[typing.Sequence[str]]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.patch_endpoint(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_endpoint(
            app_id,
            endpoint_id,
            channels=channels,
            description=description,
            disabled=disabled,
            event_types=event_types,
            metadata=metadata,
            throttle_rate=throttle_rate,
            uid=uid,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def v1endpoint_get_headers(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointHeadersOut:
        """
        Get the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointHeadersOut
            The value of the headers is returned in the `headers` field.

            Sensitive headers that have been redacted are returned in the sensitive field.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_get_headers(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_get_headers(app_id, endpoint_id, request_options=request_options)
        return _response.data

    async def v1endpoint_update_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_update_headers(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
                headers={"X-Example": "123", "X-Foobar": "Bar"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_update_headers(
            app_id, endpoint_id, headers=headers, request_options=request_options
        )
        return _response.data

    async def v1endpoint_patch_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Partially set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_patch_headers(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
                headers={"X-Example": "123", "X-Foobar": "Bar"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_patch_headers(
            app_id, endpoint_id, headers=headers, request_options=request_options
        )
        return _response.data

    async def v1endpoint_recover(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecoverOut:
        """
        Resend all failed messages since a given time.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : dt.datetime

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecoverOut


        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_recover(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
                since=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_recover(
            app_id,
            endpoint_id,
            since=since,
            idempotency_key=idempotency_key,
            until=until,
            request_options=request_options,
        )
        return _response.data

    async def v1endpoint_get_secret(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointSecretOut:
        """
        Get the endpoint's signing secret.

        This is used to verify the authenticity of the webhook.
        For more information please refer to [the consuming webhooks docs](https://docs.svix.com/consuming-webhooks/).

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointSecretOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_get_secret(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_get_secret(app_id, endpoint_id, request_options=request_options)
        return _response.data

    async def v1endpoint_rotate_secret(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Rotates the endpoint's signing secret.  The previous secret will be valid for the next 24 hours.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        grace_period_seconds : typing.Optional[int]
            How long the old secret will be valid for, in seconds.

            Valid values are between 0 (immediate expiry) and 7 days. The default is 24 hours.

        key : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_rotate_secret(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_rotate_secret(
            app_id,
            endpoint_id,
            idempotency_key=idempotency_key,
            grace_period_seconds=grace_period_seconds,
            key=key,
            request_options=request_options,
        )
        return _response.data

    async def v1endpoint_send_example(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        event_type: str,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageOut:
        """
        Send an example message for an event

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        event_type : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_send_example(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
                event_type="user.signup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_send_example(
            app_id, endpoint_id, event_type=event_type, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def v1endpoint_get_stats(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: typing.Optional[dt.datetime] = None,
        until: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointStats:
        """
        Get basic statistics for the endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : typing.Optional[dt.datetime]

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointStats


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoint.v1endpoint_get_stats(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1endpoint_get_stats(
            app_id, endpoint_id, since=since, until=until, request_options=request_options
        )
        return _response.data
