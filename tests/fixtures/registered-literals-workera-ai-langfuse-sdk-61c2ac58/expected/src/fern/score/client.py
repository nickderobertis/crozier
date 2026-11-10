

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_score_response import CreateScoreResponse
from ..types.create_score_value import CreateScoreValue
from ..types.get_scores_response import GetScoresResponse
from ..types.score import Score
from ..types.score_data_type import ScoreDataType
from ..types.score_source import ScoreSource
from .raw_client import AsyncRawScoreClient, RawScoreClient


OMIT = typing.cast(typing.Any, ...)


class ScoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScoreClient
        """
        return self._raw_client

    def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source: typing.Optional[ScoreSource] = None,
        operator: typing.Optional[str] = None,
        value: typing.Optional[float] = None,
        score_ids: typing.Optional[str] = None,
        config_id: typing.Optional[str] = None,
        queue_id: typing.Optional[str] = None,
        data_type: typing.Optional[ScoreDataType] = None,
        trace_tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetScoresResponse:
        """
        Get a list of scores

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]
            Retrieve only scores with this userId associated to the trace.

        name : typing.Optional[str]
            Retrieve only scores with this name.

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created before a certain datetime (ISO 8601)

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for scores where the environment is one of the provided values.

        source : typing.Optional[ScoreSource]
            Retrieve only scores from a specific source.

        operator : typing.Optional[str]
            Retrieve only scores with <operator> value.

        value : typing.Optional[float]
            Retrieve only scores with <operator> value.

        score_ids : typing.Optional[str]
            Comma-separated list of score IDs to limit the results to.

        config_id : typing.Optional[str]
            Retrieve only scores with a specific configId.

        queue_id : typing.Optional[str]
            Retrieve only scores with a specific annotation queueId.

        data_type : typing.Optional[ScoreDataType]
            Retrieve only scores with a specific dataType.

        trace_tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only scores linked to traces that include all of these tags will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetScoresResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.score.get()
        """
        _response = self._raw_client.get(
            page=page,
            limit=limit,
            user_id=user_id,
            name=name,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            environment=environment,
            source=source,
            operator=operator,
            value=value,
            score_ids=score_ids,
            config_id=config_id,
            queue_id=queue_id,
            data_type=data_type,
            trace_tags=trace_tags,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        trace_id: str,
        name: str,
        value: CreateScoreValue,
        id: typing.Optional[str] = OMIT,
        observation_id: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        environment: typing.Optional[str] = OMIT,
        data_type: typing.Optional[ScoreDataType] = OMIT,
        config_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateScoreResponse:
        """
        Create a score

        Parameters
        ----------
        trace_id : str

        name : str

        value : CreateScoreValue
            The value of the score. Must be passed as string for categorical scores, and numeric for boolean and numeric scores. Boolean score values must equal either 1 or 0 (true or false)

        id : typing.Optional[str]

        observation_id : typing.Optional[str]

        comment : typing.Optional[str]

        environment : typing.Optional[str]
            The environment of the score. Can be any lowercase alphanumeric string with hyphens and underscores that does not start with 'langfuse'.

        data_type : typing.Optional[ScoreDataType]
            The data type of the score. When passing a configId this field is inferred. Otherwise, this field must be passed or will default to numeric.

        config_id : typing.Optional[str]
            Reference a score config on a score. The unique langfuse identifier of a score config. When passing this field, the dataType and stringValue fields are automatically populated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateScoreResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.score.create(
            trace_id="cdef-1234-5678-90ab",
            name="novelty",
            value=1.1,
        )
        """
        _response = self._raw_client.create(
            trace_id=trace_id,
            name=name,
            value=value,
            id=id,
            observation_id=observation_id,
            comment=comment,
            environment=environment,
            data_type=data_type,
            config_id=config_id,
            request_options=request_options,
        )
        return _response.data

    def get_by_id(self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Score:
        """
        Get a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Score


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.score.get_by_id(
            score_id="scoreId",
        )
        """
        _response = self._raw_client.get_by_id(score_id, request_options=request_options)
        return _response.data

    def delete(self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.score.delete(
            score_id="scoreId",
        )
        """
        _response = self._raw_client.delete(score_id, request_options=request_options)
        return _response.data


class AsyncScoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScoreClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source: typing.Optional[ScoreSource] = None,
        operator: typing.Optional[str] = None,
        value: typing.Optional[float] = None,
        score_ids: typing.Optional[str] = None,
        config_id: typing.Optional[str] = None,
        queue_id: typing.Optional[str] = None,
        data_type: typing.Optional[ScoreDataType] = None,
        trace_tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetScoresResponse:
        """
        Get a list of scores

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]
            Retrieve only scores with this userId associated to the trace.

        name : typing.Optional[str]
            Retrieve only scores with this name.

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created before a certain datetime (ISO 8601)

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for scores where the environment is one of the provided values.

        source : typing.Optional[ScoreSource]
            Retrieve only scores from a specific source.

        operator : typing.Optional[str]
            Retrieve only scores with <operator> value.

        value : typing.Optional[float]
            Retrieve only scores with <operator> value.

        score_ids : typing.Optional[str]
            Comma-separated list of score IDs to limit the results to.

        config_id : typing.Optional[str]
            Retrieve only scores with a specific configId.

        queue_id : typing.Optional[str]
            Retrieve only scores with a specific annotation queueId.

        data_type : typing.Optional[ScoreDataType]
            Retrieve only scores with a specific dataType.

        trace_tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only scores linked to traces that include all of these tags will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetScoresResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.score.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            page=page,
            limit=limit,
            user_id=user_id,
            name=name,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            environment=environment,
            source=source,
            operator=operator,
            value=value,
            score_ids=score_ids,
            config_id=config_id,
            queue_id=queue_id,
            data_type=data_type,
            trace_tags=trace_tags,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        trace_id: str,
        name: str,
        value: CreateScoreValue,
        id: typing.Optional[str] = OMIT,
        observation_id: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        environment: typing.Optional[str] = OMIT,
        data_type: typing.Optional[ScoreDataType] = OMIT,
        config_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateScoreResponse:
        """
        Create a score

        Parameters
        ----------
        trace_id : str

        name : str

        value : CreateScoreValue
            The value of the score. Must be passed as string for categorical scores, and numeric for boolean and numeric scores. Boolean score values must equal either 1 or 0 (true or false)

        id : typing.Optional[str]

        observation_id : typing.Optional[str]

        comment : typing.Optional[str]

        environment : typing.Optional[str]
            The environment of the score. Can be any lowercase alphanumeric string with hyphens and underscores that does not start with 'langfuse'.

        data_type : typing.Optional[ScoreDataType]
            The data type of the score. When passing a configId this field is inferred. Otherwise, this field must be passed or will default to numeric.

        config_id : typing.Optional[str]
            Reference a score config on a score. The unique langfuse identifier of a score config. When passing this field, the dataType and stringValue fields are automatically populated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateScoreResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.score.create(
                trace_id="cdef-1234-5678-90ab",
                name="novelty",
                value=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            trace_id=trace_id,
            name=name,
            value=value,
            id=id,
            observation_id=observation_id,
            comment=comment,
            environment=environment,
            data_type=data_type,
            config_id=config_id,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id(self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Score:
        """
        Get a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Score


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.score.get_by_id(
                score_id="scoreId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id(score_id, request_options=request_options)
        return _response.data

    async def delete(self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.score.delete(
                score_id="scoreId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(score_id, request_options=request_options)
        return _response.data
