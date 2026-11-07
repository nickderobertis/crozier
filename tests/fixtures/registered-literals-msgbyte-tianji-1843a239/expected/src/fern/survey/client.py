

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSurveyClient, RawSurveyClient
from .types.survey_ai_category_list_response_item import SurveyAiCategoryListResponseItem
from .types.survey_all_response_item import SurveyAllResponseItem
from .types.survey_create_request_payload import SurveyCreateRequestPayload
from .types.survey_create_response import SurveyCreateResponse
from .types.survey_delete_response import SurveyDeleteResponse
from .types.survey_duplicate_response import SurveyDuplicateResponse
from .types.survey_get_response import SurveyGetResponse
from .types.survey_get_result_response import SurveyGetResultResponse
from .types.survey_result_list_response import SurveyResultListResponse
from .types.survey_stats_response_item import SurveyStatsResponseItem
from .types.survey_submit_response import SurveySubmitResponse
from .types.survey_update_request_payload import SurveyUpdateRequestPayload
from .types.survey_update_response import SurveyUpdateResponse


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

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SurveyAllResponseItem]:
        """
        Get all surveys

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SurveyAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.all_(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    def get(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[SurveyGetResponse]:
        """
        Get a specific survey by ID

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SurveyGetResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.get(
            workspace_id="workspaceId",
            survey_id="surveyId",
        )
        """
        _response = self._raw_client.get(workspace_id, survey_id, request_options=request_options)
        return _response.data

    def count(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Get the total count of survey results

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.count(
            workspace_id="workspaceId",
            survey_id="surveyId",
        )
        """
        _response = self._raw_client.count(workspace_id, survey_id, request_options=request_options)
        return _response.data

    def allresultcount(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, float]:
        """
        Get result counts for all surveys in the workspace

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, float]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.allresultcount(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.allresultcount(workspace_id, request_options=request_options)
        return _response.data

    def submit(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        payload: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveySubmitResponse:
        """
        Submit survey responses

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        payload : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveySubmitResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.submit(
            workspace_id="workspaceId",
            survey_id="surveyId",
            payload={"key": "value"},
        )
        """
        _response = self._raw_client.submit(workspace_id, survey_id, payload=payload, request_options=request_options)
        return _response.data

    def create(
        self,
        workspace_id: str,
        *,
        name: str,
        payload: SurveyCreateRequestPayload,
        feed_channel_ids: typing.Sequence[str],
        feed_template: str,
        webhook_url: str,
        desc: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveyCreateResponse:
        """
        Create a new survey with payload, feed channels and webhook configuration

        Parameters
        ----------
        workspace_id : str

        name : str

        payload : SurveyCreateRequestPayload

        feed_channel_ids : typing.Sequence[str]

        feed_template : str

        webhook_url : str

        desc : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyCreateResponse
            Successful response

        Examples
        --------
        from fern.survey import (
            SurveyCreateRequestPayload,
            SurveyCreateRequestPayloadItemsItem,
            SurveyCreateRequestPayloadItemsItemType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.create(
            workspace_id="workspaceId",
            name="name",
            payload=SurveyCreateRequestPayload(
                items=[
                    SurveyCreateRequestPayloadItemsItem(
                        label="label",
                        name="name",
                        type=SurveyCreateRequestPayloadItemsItemType.TEXT,
                    )
                ],
            ),
            feed_channel_ids=["feedChannelIds"],
            feed_template="feedTemplate",
            webhook_url="webhookUrl",
        )
        """
        _response = self._raw_client.create(
            workspace_id,
            name=name,
            payload=payload,
            feed_channel_ids=feed_channel_ids,
            feed_template=feed_template,
            webhook_url=webhook_url,
            desc=desc,
            request_options=request_options,
        )
        return _response.data

    def update(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        desc: typing.Optional[str] = OMIT,
        payload: typing.Optional[SurveyUpdateRequestPayload] = OMIT,
        feed_channel_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        feed_template: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveyUpdateResponse:
        """
        Update an existing survey configuration

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        name : typing.Optional[str]

        desc : typing.Optional[str]

        payload : typing.Optional[SurveyUpdateRequestPayload]

        feed_channel_ids : typing.Optional[typing.Sequence[str]]

        feed_template : typing.Optional[str]

        webhook_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyUpdateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.update(
            workspace_id="workspaceId",
            survey_id="surveyId",
        )
        """
        _response = self._raw_client.update(
            workspace_id,
            survey_id,
            name=name,
            desc=desc,
            payload=payload,
            feed_channel_ids=feed_channel_ids,
            feed_template=feed_template,
            webhook_url=webhook_url,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SurveyDeleteResponse:
        """
        Delete a survey permanently

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.delete(
            workspace_id="workspaceId",
            survey_id="surveyId",
        )
        """
        _response = self._raw_client.delete(workspace_id, survey_id, request_options=request_options)
        return _response.data

    def duplicate(
        self, workspace_id: str, survey_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SurveyDuplicateResponse:
        """
        Duplicate an existing survey with a new name

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyDuplicateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.duplicate(
            workspace_id="workspaceId",
            survey_id="surveyId",
            name="name",
        )
        """
        _response = self._raw_client.duplicate(workspace_id, survey_id, name=name, request_options=request_options)
        return _response.data

    def getresult(
        self, workspace_id: str, result_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[SurveyGetResultResponse]:
        """
        Get a specific survey result by result ID

        Parameters
        ----------
        workspace_id : str

        result_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SurveyGetResultResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.getresult(
            workspace_id="workspaceId",
            result_id="resultId",
        )
        """
        _response = self._raw_client.getresult(workspace_id, result_id, request_options=request_options)
        return _response.data

    def resultlist(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        start_at: typing.Optional[float] = None,
        end_at: typing.Optional[float] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveyResultListResponse:
        """
        Get paginated list of survey results with optional date range and filters

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        start_at : typing.Optional[float]

        end_at : typing.Optional[float]

        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyResultListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.resultlist(
            workspace_id="workspaceId",
            survey_id="surveyId",
        )
        """
        _response = self._raw_client.resultlist(
            workspace_id,
            survey_id,
            limit=limit,
            cursor=cursor,
            start_at=start_at,
            end_at=end_at,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    def stats(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        start_at: typing.Optional[float] = None,
        end_at: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SurveyStatsResponseItem]:
        """
        Get survey submission statistics grouped by date

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : typing.Optional[float]

        end_at : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SurveyStatsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.stats(
            workspace_id="workspaceId",
            survey_id="surveyId",
        )
        """
        _response = self._raw_client.stats(
            workspace_id, survey_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    def aicategorylist(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SurveyAiCategoryListResponseItem]:
        """
        Get AI-categorized survey results with counts for each category

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SurveyAiCategoryListResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.survey.aicategorylist(
            workspace_id="workspaceId",
            survey_id="surveyId",
        )
        """
        _response = self._raw_client.aicategorylist(workspace_id, survey_id, request_options=request_options)
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

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SurveyAllResponseItem]:
        """
        Get all surveys

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SurveyAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.all_(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    async def get(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[SurveyGetResponse]:
        """
        Get a specific survey by ID

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SurveyGetResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.get(
                workspace_id="workspaceId",
                survey_id="surveyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(workspace_id, survey_id, request_options=request_options)
        return _response.data

    async def count(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Get the total count of survey results

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.count(
                workspace_id="workspaceId",
                survey_id="surveyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.count(workspace_id, survey_id, request_options=request_options)
        return _response.data

    async def allresultcount(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, float]:
        """
        Get result counts for all surveys in the workspace

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, float]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.allresultcount(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.allresultcount(workspace_id, request_options=request_options)
        return _response.data

    async def submit(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        payload: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveySubmitResponse:
        """
        Submit survey responses

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        payload : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveySubmitResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.submit(
                workspace_id="workspaceId",
                survey_id="surveyId",
                payload={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit(
            workspace_id, survey_id, payload=payload, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        workspace_id: str,
        *,
        name: str,
        payload: SurveyCreateRequestPayload,
        feed_channel_ids: typing.Sequence[str],
        feed_template: str,
        webhook_url: str,
        desc: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveyCreateResponse:
        """
        Create a new survey with payload, feed channels and webhook configuration

        Parameters
        ----------
        workspace_id : str

        name : str

        payload : SurveyCreateRequestPayload

        feed_channel_ids : typing.Sequence[str]

        feed_template : str

        webhook_url : str

        desc : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.survey import (
            SurveyCreateRequestPayload,
            SurveyCreateRequestPayloadItemsItem,
            SurveyCreateRequestPayloadItemsItemType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.create(
                workspace_id="workspaceId",
                name="name",
                payload=SurveyCreateRequestPayload(
                    items=[
                        SurveyCreateRequestPayloadItemsItem(
                            label="label",
                            name="name",
                            type=SurveyCreateRequestPayloadItemsItemType.TEXT,
                        )
                    ],
                ),
                feed_channel_ids=["feedChannelIds"],
                feed_template="feedTemplate",
                webhook_url="webhookUrl",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            workspace_id,
            name=name,
            payload=payload,
            feed_channel_ids=feed_channel_ids,
            feed_template=feed_template,
            webhook_url=webhook_url,
            desc=desc,
            request_options=request_options,
        )
        return _response.data

    async def update(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        desc: typing.Optional[str] = OMIT,
        payload: typing.Optional[SurveyUpdateRequestPayload] = OMIT,
        feed_channel_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        feed_template: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveyUpdateResponse:
        """
        Update an existing survey configuration

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        name : typing.Optional[str]

        desc : typing.Optional[str]

        payload : typing.Optional[SurveyUpdateRequestPayload]

        feed_channel_ids : typing.Optional[typing.Sequence[str]]

        feed_template : typing.Optional[str]

        webhook_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyUpdateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.update(
                workspace_id="workspaceId",
                survey_id="surveyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            workspace_id,
            survey_id,
            name=name,
            desc=desc,
            payload=payload,
            feed_channel_ids=feed_channel_ids,
            feed_template=feed_template,
            webhook_url=webhook_url,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SurveyDeleteResponse:
        """
        Delete a survey permanently

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.delete(
                workspace_id="workspaceId",
                survey_id="surveyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(workspace_id, survey_id, request_options=request_options)
        return _response.data

    async def duplicate(
        self, workspace_id: str, survey_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SurveyDuplicateResponse:
        """
        Duplicate an existing survey with a new name

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyDuplicateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.duplicate(
                workspace_id="workspaceId",
                survey_id="surveyId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.duplicate(
            workspace_id, survey_id, name=name, request_options=request_options
        )
        return _response.data

    async def getresult(
        self, workspace_id: str, result_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[SurveyGetResultResponse]:
        """
        Get a specific survey result by result ID

        Parameters
        ----------
        workspace_id : str

        result_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SurveyGetResultResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.getresult(
                workspace_id="workspaceId",
                result_id="resultId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getresult(workspace_id, result_id, request_options=request_options)
        return _response.data

    async def resultlist(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        start_at: typing.Optional[float] = None,
        end_at: typing.Optional[float] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SurveyResultListResponse:
        """
        Get paginated list of survey results with optional date range and filters

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        start_at : typing.Optional[float]

        end_at : typing.Optional[float]

        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SurveyResultListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.resultlist(
                workspace_id="workspaceId",
                survey_id="surveyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resultlist(
            workspace_id,
            survey_id,
            limit=limit,
            cursor=cursor,
            start_at=start_at,
            end_at=end_at,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    async def stats(
        self,
        workspace_id: str,
        survey_id: str,
        *,
        start_at: typing.Optional[float] = None,
        end_at: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SurveyStatsResponseItem]:
        """
        Get survey submission statistics grouped by date

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : typing.Optional[float]

        end_at : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SurveyStatsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.stats(
                workspace_id="workspaceId",
                survey_id="surveyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stats(
            workspace_id, survey_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    async def aicategorylist(
        self, workspace_id: str, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SurveyAiCategoryListResponseItem]:
        """
        Get AI-categorized survey results with counts for each category

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SurveyAiCategoryListResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.survey.aicategorylist(
                workspace_id="workspaceId",
                survey_id="surveyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aicategorylist(workspace_id, survey_id, request_options=request_options)
        return _response.data
