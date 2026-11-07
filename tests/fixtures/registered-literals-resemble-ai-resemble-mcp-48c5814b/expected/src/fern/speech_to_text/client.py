

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSpeechToTextClient, RawSpeechToTextClient
from .types.ask_transcript_question_response import AskTranscriptQuestionResponse
from .types.create_transcript_response import CreateTranscriptResponse
from .types.get_transcript_question_response import GetTranscriptQuestionResponse
from .types.get_transcript_response import GetTranscriptResponse
from .types.list_transcript_questions_response import ListTranscriptQuestionsResponse
from .types.list_transcripts_response import ListTranscriptsResponse


OMIT = typing.cast(typing.Any, ...)


class SpeechToTextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSpeechToTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSpeechToTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSpeechToTextClient
        """
        return self._raw_client

    def list_transcripts(
        self,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTranscriptsResponse:
        """
        Retrieve paginated list of transcript jobs

        Parameters
        ----------
        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTranscriptsResponse
            List of transcripts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.speech_to_text.list_transcripts(
            page=1,
        )
        """
        _response = self._raw_client.list_transcripts(page=page, per_page=per_page, request_options=request_options)
        return _response.data

    def create_transcript(
        self,
        *,
        audio_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTranscriptResponse:
        """
        Submit audio or video for transcription

        Parameters
        ----------
        audio_token : typing.Optional[str]
            Signed ActiveStorage token

        url : typing.Optional[str]
            HTTPS URL to audio/video file

        query : typing.Optional[str]
            Optional intelligence question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTranscriptResponse
            Transcript job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.speech_to_text.create_transcript()
        """
        _response = self._raw_client.create_transcript(
            audio_token=audio_token, url=url, query=query, request_options=request_options
        )
        return _response.data

    def get_transcript(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTranscriptResponse:
        """
        Retrieve transcript status, text, and timestamps

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTranscriptResponse
            Transcript details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.speech_to_text.get_transcript(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_transcript(uuid_, request_options=request_options)
        return _response.data

    def ask_transcript_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AskTranscriptQuestionResponse:
        """
        Submit a question about a completed transcript

        Parameters
        ----------
        uuid_ : str

        query : str
            Question to ask about the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AskTranscriptQuestionResponse
            Question submitted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.speech_to_text.ask_transcript_question(
            uuid_="uuid",
            query="What action items were mentioned?",
        )
        """
        _response = self._raw_client.ask_transcript_question(uuid_, query=query, request_options=request_options)
        return _response.data

    def list_transcript_questions(
        self,
        uuid_: str,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTranscriptQuestionsResponse:
        """
        List all questions asked about a transcript

        Parameters
        ----------
        uuid_ : str

        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTranscriptQuestionsResponse
            List of questions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.speech_to_text.list_transcript_questions(
            uuid_="uuid",
            page=1,
        )
        """
        _response = self._raw_client.list_transcript_questions(
            uuid_, page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    def get_transcript_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTranscriptQuestionResponse:
        """
        Check the status of a specific question

        Parameters
        ----------
        uuid_ : str

        question_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTranscriptQuestionResponse
            Question details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.speech_to_text.get_transcript_question(
            uuid_="uuid",
            question_uuid="question_uuid",
        )
        """
        _response = self._raw_client.get_transcript_question(uuid_, question_uuid, request_options=request_options)
        return _response.data


class AsyncSpeechToTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSpeechToTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSpeechToTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSpeechToTextClient
        """
        return self._raw_client

    async def list_transcripts(
        self,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTranscriptsResponse:
        """
        Retrieve paginated list of transcript jobs

        Parameters
        ----------
        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTranscriptsResponse
            List of transcripts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.speech_to_text.list_transcripts(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_transcripts(
            page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    async def create_transcript(
        self,
        *,
        audio_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTranscriptResponse:
        """
        Submit audio or video for transcription

        Parameters
        ----------
        audio_token : typing.Optional[str]
            Signed ActiveStorage token

        url : typing.Optional[str]
            HTTPS URL to audio/video file

        query : typing.Optional[str]
            Optional intelligence question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTranscriptResponse
            Transcript job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.speech_to_text.create_transcript()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transcript(
            audio_token=audio_token, url=url, query=query, request_options=request_options
        )
        return _response.data

    async def get_transcript(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTranscriptResponse:
        """
        Retrieve transcript status, text, and timestamps

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTranscriptResponse
            Transcript details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.speech_to_text.get_transcript(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transcript(uuid_, request_options=request_options)
        return _response.data

    async def ask_transcript_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AskTranscriptQuestionResponse:
        """
        Submit a question about a completed transcript

        Parameters
        ----------
        uuid_ : str

        query : str
            Question to ask about the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AskTranscriptQuestionResponse
            Question submitted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.speech_to_text.ask_transcript_question(
                uuid_="uuid",
                query="What action items were mentioned?",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ask_transcript_question(uuid_, query=query, request_options=request_options)
        return _response.data

    async def list_transcript_questions(
        self,
        uuid_: str,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTranscriptQuestionsResponse:
        """
        List all questions asked about a transcript

        Parameters
        ----------
        uuid_ : str

        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTranscriptQuestionsResponse
            List of questions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.speech_to_text.list_transcript_questions(
                uuid_="uuid",
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_transcript_questions(
            uuid_, page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    async def get_transcript_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTranscriptQuestionResponse:
        """
        Check the status of a specific question

        Parameters
        ----------
        uuid_ : str

        question_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTranscriptQuestionResponse
            Question details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.speech_to_text.get_transcript_question(
                uuid_="uuid",
                question_uuid="question_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transcript_question(
            uuid_, question_uuid, request_options=request_options
        )
        return _response.data
