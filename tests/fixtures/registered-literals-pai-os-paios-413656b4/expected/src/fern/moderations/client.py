

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_moderation_response import CreateModerationResponse
from .raw_client import AsyncRawModerationsClient, RawModerationsClient
from .types.create_moderation_request_input import CreateModerationRequestInput
from .types.create_moderation_request_model import CreateModerationRequestModel


OMIT = typing.cast(typing.Any, ...)


class ModerationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModerationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModerationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModerationsClient
        """
        return self._raw_client

    def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[CreateModerationRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateModerationResponse:
        """
        Parameters
        ----------
        input : CreateModerationRequestInput
            The input text to classify

        model : typing.Optional[CreateModerationRequestModel]
            Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

            The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateModerationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.moderations.create_moderation(
            input="I want to kill them.",
        )
        """
        _response = self._raw_client.create_moderation(input=input, model=model, request_options=request_options)
        return _response.data


class AsyncModerationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModerationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModerationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModerationsClient
        """
        return self._raw_client

    async def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[CreateModerationRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateModerationResponse:
        """
        Parameters
        ----------
        input : CreateModerationRequestInput
            The input text to classify

        model : typing.Optional[CreateModerationRequestModel]
            Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

            The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateModerationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.moderations.create_moderation(
                input="I want to kill them.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_moderation(input=input, model=model, request_options=request_options)
        return _response.data
