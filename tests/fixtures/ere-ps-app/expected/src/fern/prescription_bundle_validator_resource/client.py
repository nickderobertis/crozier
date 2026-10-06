

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.json_value import JsonValue
from .raw_client import AsyncRawPrescriptionBundleValidatorResourceClient, RawPrescriptionBundleValidatorResourceClient


OMIT = typing.cast(typing.Any, ...)


class PrescriptionBundleValidatorResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrescriptionBundleValidatorResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrescriptionBundleValidatorResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrescriptionBundleValidatorResourceClient
        """
        return self._raw_client

    def post_validate(
        self, *, request: typing.Dict[str, JsonValue], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, JsonValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, JsonValue

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prescription_bundle_validator_resource.post_validate(
            request={"key": JsonValue()},
        )
        """
        _response = self._raw_client.post_validate(request=request, request_options=request_options)
        return _response.data


class AsyncPrescriptionBundleValidatorResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrescriptionBundleValidatorResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrescriptionBundleValidatorResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrescriptionBundleValidatorResourceClient
        """
        return self._raw_client

    async def post_validate(
        self, *, request: typing.Dict[str, JsonValue], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, JsonValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, JsonValue

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prescription_bundle_validator_resource.post_validate(
                request={"key": JsonValue()},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_validate(request=request, request_options=request_options)
        return _response.data
