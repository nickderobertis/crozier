

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.process_version_validation_response_dto import ProcessVersionValidationResponseDto
from .raw_client import AsyncRawVersionControlClient, RawVersionControlClient


OMIT = typing.cast(typing.Any, ...)


class VersionControlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVersionControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVersionControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVersionControlClient
        """
        return self._raw_client

    def post_api_versioncontrol_scenarioname_versionvalidation(
        self, scenario_name: str, *, local_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessVersionValidationResponseDto:
        """
        Parameters
        ----------
        scenario_name : str

        local_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessVersionValidationResponseDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.version_control.post_api_versioncontrol_scenarioname_versionvalidation(
            scenario_name="scenarioName",
            local_version=24,
        )
        """
        _response = self._raw_client.post_api_versioncontrol_scenarioname_versionvalidation(
            scenario_name, local_version=local_version, request_options=request_options
        )
        return _response.data


class AsyncVersionControlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVersionControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVersionControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVersionControlClient
        """
        return self._raw_client

    async def post_api_versioncontrol_scenarioname_versionvalidation(
        self, scenario_name: str, *, local_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessVersionValidationResponseDto:
        """
        Parameters
        ----------
        scenario_name : str

        local_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessVersionValidationResponseDto


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.version_control.post_api_versioncontrol_scenarioname_versionvalidation(
                scenario_name="scenarioName",
                local_version=24,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_versioncontrol_scenarioname_versionvalidation(
            scenario_name, local_version=local_version, request_options=request_options
        )
        return _response.data
