

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChannelAdmissionPolicyClient, RawChannelAdmissionPolicyClient
from .types.channel_admission_policy_list_response import ChannelAdmissionPolicyListResponse
from .types.channel_admission_policy_set_request_policy import ChannelAdmissionPolicySetRequestPolicy
from .types.channel_admission_policy_set_response import ChannelAdmissionPolicySetResponse


OMIT = typing.cast(typing.Any, ...)


class ChannelAdmissionPolicyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelAdmissionPolicyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelAdmissionPolicyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelAdmissionPolicyClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ChannelAdmissionPolicyListResponse:
        """
        Returns one entry per enforced channel (exempt and hidden channels are omitted), seeded with defaults for channels without a stored row.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelAdmissionPolicyListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.channel_admission_policy.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def set(
        self,
        channel_type: str,
        *,
        policy: ChannelAdmissionPolicySetRequestPolicy,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelAdmissionPolicySetResponse:
        """
        Upserts the channel's admission policy. Exempt and hidden channels return 403.

        Parameters
        ----------
        channel_type : str
            The channel type (e.g. slack)

        policy : ChannelAdmissionPolicySetRequestPolicy

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelAdmissionPolicySetResponse
            Successful response

        Examples
        --------
        from fern.channel_admission_policy import ChannelAdmissionPolicySetRequestPolicy

        from fern import FernApi

        client = FernApi()
        client.channel_admission_policy.set(
            channel_type="channel_type",
            policy=ChannelAdmissionPolicySetRequestPolicy.NO_ONE,
        )
        """
        _response = self._raw_client.set(channel_type, policy=policy, note=note, request_options=request_options)
        return _response.data


class AsyncChannelAdmissionPolicyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelAdmissionPolicyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelAdmissionPolicyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelAdmissionPolicyClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChannelAdmissionPolicyListResponse:
        """
        Returns one entry per enforced channel (exempt and hidden channels are omitted), seeded with defaults for channels without a stored row.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelAdmissionPolicyListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_admission_policy.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def set(
        self,
        channel_type: str,
        *,
        policy: ChannelAdmissionPolicySetRequestPolicy,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelAdmissionPolicySetResponse:
        """
        Upserts the channel's admission policy. Exempt and hidden channels return 403.

        Parameters
        ----------
        channel_type : str
            The channel type (e.g. slack)

        policy : ChannelAdmissionPolicySetRequestPolicy

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelAdmissionPolicySetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.channel_admission_policy import ChannelAdmissionPolicySetRequestPolicy

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_admission_policy.set(
                channel_type="channel_type",
                policy=ChannelAdmissionPolicySetRequestPolicy.NO_ONE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set(channel_type, policy=policy, note=note, request_options=request_options)
        return _response.data
