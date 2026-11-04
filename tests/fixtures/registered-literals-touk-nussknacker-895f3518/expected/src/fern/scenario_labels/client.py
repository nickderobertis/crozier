

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.scenario_labels import ScenarioLabels
from ..types.scenario_labels_validation_response_dto import ScenarioLabelsValidationResponseDto
from .raw_client import AsyncRawScenarioLabelsClient, RawScenarioLabelsClient


OMIT = typing.cast(typing.Any, ...)


class ScenarioLabelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScenarioLabelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScenarioLabelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScenarioLabelsClient
        """
        return self._raw_client

    def get_api_scenariolabels(self, *, request_options: typing.Optional[RequestOptions] = None) -> ScenarioLabels:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioLabels


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.scenario_labels.get_api_scenariolabels()
        """
        _response = self._raw_client.get_api_scenariolabels(request_options=request_options)
        return _response.data

    def post_api_scenariolabels_validation(
        self,
        *,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScenarioLabelsValidationResponseDto:
        """
        Parameters
        ----------
        labels : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioLabelsValidationResponseDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.scenario_labels.post_api_scenariolabels_validation(
            labels=["Label_1", "Label_2"],
        )
        """
        _response = self._raw_client.post_api_scenariolabels_validation(labels=labels, request_options=request_options)
        return _response.data


class AsyncScenarioLabelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScenarioLabelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScenarioLabelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScenarioLabelsClient
        """
        return self._raw_client

    async def get_api_scenariolabels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioLabels:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioLabels


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
            await client.scenario_labels.get_api_scenariolabels()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_scenariolabels(request_options=request_options)
        return _response.data

    async def post_api_scenariolabels_validation(
        self,
        *,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScenarioLabelsValidationResponseDto:
        """
        Parameters
        ----------
        labels : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioLabelsValidationResponseDto


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
            await client.scenario_labels.post_api_scenariolabels_validation(
                labels=["Label_1", "Label_2"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariolabels_validation(
            labels=labels, request_options=request_options
        )
        return _response.data
