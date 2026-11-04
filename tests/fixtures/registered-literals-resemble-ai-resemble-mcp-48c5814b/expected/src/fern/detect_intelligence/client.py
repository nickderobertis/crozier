

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDetectIntelligenceClient, RawDetectIntelligenceClient
from .types.ask_detect_intelligence_question_response import AskDetectIntelligenceQuestionResponse
from .types.get_detect_intelligence_question_response import GetDetectIntelligenceQuestionResponse


OMIT = typing.cast(typing.Any, ...)


class DetectIntelligenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDetectIntelligenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDetectIntelligenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDetectIntelligenceClient
        """
        return self._raw_client

    def ask_detect_intelligence_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AskDetectIntelligenceQuestionResponse:
        """
        Submit a natural-language question about a completed detection report. Returns 202 Accepted while the answer is generated in the background.

        Parameters
        ----------
        uuid_ : str
            UUID of the completed detection report

        query : str
            The natural-language question to ask about the detection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AskDetectIntelligenceQuestionResponse
            Question accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.detect_intelligence.ask_detect_intelligence_question(
            uuid_="uuid",
            query="query",
        )
        """
        _response = self._raw_client.ask_detect_intelligence_question(
            uuid_, query=query, request_options=request_options
        )
        return _response.data

    def get_detect_intelligence_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDetectIntelligenceQuestionResponse:
        """
        Retrieve the status and answer for a previously submitted question. Poll until status is completed or failed.

        Parameters
        ----------
        uuid_ : str
            UUID of the detection report

        question_uuid : str
            UUID of the question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDetectIntelligenceQuestionResponse
            Question status and answer

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.detect_intelligence.get_detect_intelligence_question(
            uuid_="uuid",
            question_uuid="question_uuid",
        )
        """
        _response = self._raw_client.get_detect_intelligence_question(
            uuid_, question_uuid, request_options=request_options
        )
        return _response.data


class AsyncDetectIntelligenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDetectIntelligenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDetectIntelligenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDetectIntelligenceClient
        """
        return self._raw_client

    async def ask_detect_intelligence_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AskDetectIntelligenceQuestionResponse:
        """
        Submit a natural-language question about a completed detection report. Returns 202 Accepted while the answer is generated in the background.

        Parameters
        ----------
        uuid_ : str
            UUID of the completed detection report

        query : str
            The natural-language question to ask about the detection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AskDetectIntelligenceQuestionResponse
            Question accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.detect_intelligence.ask_detect_intelligence_question(
                uuid_="uuid",
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ask_detect_intelligence_question(
            uuid_, query=query, request_options=request_options
        )
        return _response.data

    async def get_detect_intelligence_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDetectIntelligenceQuestionResponse:
        """
        Retrieve the status and answer for a previously submitted question. Poll until status is completed or failed.

        Parameters
        ----------
        uuid_ : str
            UUID of the detection report

        question_uuid : str
            UUID of the question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDetectIntelligenceQuestionResponse
            Question status and answer

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.detect_intelligence.get_detect_intelligence_question(
                uuid_="uuid",
                question_uuid="question_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_detect_intelligence_question(
            uuid_, question_uuid, request_options=request_options
        )
        return _response.data
