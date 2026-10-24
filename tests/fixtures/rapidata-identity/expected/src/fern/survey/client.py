

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSurveyClient, RawSurveyClient


OMIT = typing.cast(typing.Any, ...)


class SurveyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSurveyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSurveyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSurveyClient
        """
        return self._raw_client

    def submits_a_survey_for_the_calling_customer(
        self, *, fields: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        fields : typing.Dict[str, str]

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
        )
        client.survey.submits_a_survey_for_the_calling_customer(
            fields={"key": "value"},
        )
        """
        _response = self._raw_client.submits_a_survey_for_the_calling_customer(
            fields=fields, request_options=request_options
        )
        return _response.data


class AsyncSurveyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSurveyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSurveyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSurveyClient
        """
        return self._raw_client

    async def submits_a_survey_for_the_calling_customer(
        self, *, fields: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        fields : typing.Dict[str, str]

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
        )


        async def main() -> None:
            await client.survey.submits_a_survey_for_the_calling_customer(
                fields={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submits_a_survey_for_the_calling_customer(
            fields=fields, request_options=request_options
        )
        return _response.data
