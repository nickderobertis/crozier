

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.response_id import ResponseId
from .raw_client import AsyncRawManagementApiResponsesClient, RawManagementApiResponsesClient
from .types.create_response_request_data_value import CreateResponseRequestDataValue
from .types.create_response_request_meta import CreateResponseRequestMeta
from .types.create_response_request_variables_value import CreateResponseRequestVariablesValue
from .types.create_response_response import CreateResponseResponse
from .types.delete_response_response import DeleteResponseResponse
from .types.get_response_response import GetResponseResponse
from .types.get_responses_request_filter_date_field import GetResponsesRequestFilterDateField
from .types.get_responses_request_order import GetResponsesRequestOrder
from .types.get_responses_request_sort_by import GetResponsesRequestSortBy
from .types.get_responses_response import GetResponsesResponse
from .types.update_response_request_data_value import UpdateResponseRequestDataValue
from .types.update_response_request_variables_value import UpdateResponseRequestVariablesValue
from .types.update_response_response import UpdateResponseResponse


OMIT = typing.cast(typing.Any, ...)


class ManagementApiResponsesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementApiResponsesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementApiResponsesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementApiResponsesClient
        """
        return self._raw_client

    def get_responses(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetResponsesRequestSortBy] = None,
        order: typing.Optional[GetResponsesRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetResponsesRequestFilterDateField] = None,
        survey_id: typing.Optional[str] = None,
        contact_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetResponsesResponse:
        """
        Gets responses from the database.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetResponsesRequestSortBy]
            Sort by field

        order : typing.Optional[GetResponsesRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetResponsesRequestFilterDateField]
            Date field to filter by

        survey_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponsesResponse
            Responses retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_responses.get_responses()
        """
        _response = self._raw_client.get_responses(
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            survey_id=survey_id,
            contact_id=contact_id,
            request_options=request_options,
        )
        return _response.data

    def create_response(
        self,
        *,
        survey_id: str,
        finished: bool,
        data: typing.Dict[str, CreateResponseRequestDataValue],
        created_at: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        single_use_id: typing.Optional[str] = OMIT,
        ending_id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        variables: typing.Optional[typing.Dict[str, CreateResponseRequestVariablesValue]] = OMIT,
        ttc: typing.Optional[typing.Dict[str, float]] = OMIT,
        meta: typing.Optional[CreateResponseRequestMeta] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateResponseResponse:
        """
        Creates a response in the database. This will trigger the response pipeline, including webhooks, integrations, follow-up emails, and other configured actions.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        finished : bool
            Whether the response is finished

        data : typing.Dict[str, CreateResponseRequestDataValue]
            The data of the response

        created_at : typing.Optional[str]
            The date and time the response was created

        updated_at : typing.Optional[str]
            The date and time the response was last updated

        display_id : typing.Optional[str]
            The display ID of the response

        single_use_id : typing.Optional[str]
            The single use ID of the response

        ending_id : typing.Optional[str]
            The ID of the ending

        language : typing.Optional[str]
            The language of the response

        variables : typing.Optional[typing.Dict[str, CreateResponseRequestVariablesValue]]
            The variables of the response

        ttc : typing.Optional[typing.Dict[str, float]]
            The TTC of the response

        meta : typing.Optional[CreateResponseRequestMeta]
            The meta data of the response

        user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateResponseResponse
            Response created successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_responses.create_response(
            survey_id="surveyId",
            finished=True,
            data={"key": "value"},
        )
        """
        _response = self._raw_client.create_response(
            survey_id=survey_id,
            finished=finished,
            data=data,
            created_at=created_at,
            updated_at=updated_at,
            display_id=display_id,
            single_use_id=single_use_id,
            ending_id=ending_id,
            language=language,
            variables=variables,
            ttc=ttc,
            meta=meta,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    def get_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetResponseResponse:
        """
        Gets a response from the database.

        Parameters
        ----------
        id : ResponseId
            The ID of the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponseResponse
            Response retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_responses.get_response(
            id="id",
        )
        """
        _response = self._raw_client.get_response(id, request_options=request_options)
        return _response.data

    def update_response(
        self,
        id: ResponseId,
        *,
        finished: typing.Optional[bool] = OMIT,
        ending_id: typing.Optional[str] = OMIT,
        data: typing.Optional[typing.Dict[str, UpdateResponseRequestDataValue]] = OMIT,
        variables: typing.Optional[typing.Dict[str, UpdateResponseRequestVariablesValue]] = OMIT,
        ttc: typing.Optional[typing.Dict[str, float]] = OMIT,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateResponseResponse:
        """
        Updates a response in the database. This will trigger the response pipeline, including webhooks, integrations, follow-up emails (if the response is marked as finished), and other configured actions.

        Parameters
        ----------
        id : ResponseId
            The ID of the response

        finished : typing.Optional[bool]

        ending_id : typing.Optional[str]

        data : typing.Optional[typing.Dict[str, UpdateResponseRequestDataValue]]

        variables : typing.Optional[typing.Dict[str, UpdateResponseRequestVariablesValue]]

        ttc : typing.Optional[typing.Dict[str, float]]

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateResponseResponse
            Response updated successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_responses.update_response(
            id="id",
        )
        """
        _response = self._raw_client.update_response(
            id,
            finished=finished,
            ending_id=ending_id,
            data=data,
            variables=variables,
            ttc=ttc,
            language=language,
            request_options=request_options,
        )
        return _response.data

    def delete_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteResponseResponse:
        """
        Deletes a response from the database.

        Parameters
        ----------
        id : ResponseId
            The ID of the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteResponseResponse
            Response deleted successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_responses.delete_response(
            id="id",
        )
        """
        _response = self._raw_client.delete_response(id, request_options=request_options)
        return _response.data


class AsyncManagementApiResponsesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementApiResponsesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementApiResponsesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementApiResponsesClient
        """
        return self._raw_client

    async def get_responses(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetResponsesRequestSortBy] = None,
        order: typing.Optional[GetResponsesRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetResponsesRequestFilterDateField] = None,
        survey_id: typing.Optional[str] = None,
        contact_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetResponsesResponse:
        """
        Gets responses from the database.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetResponsesRequestSortBy]
            Sort by field

        order : typing.Optional[GetResponsesRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetResponsesRequestFilterDateField]
            Date field to filter by

        survey_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponsesResponse
            Responses retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_responses.get_responses()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_responses(
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            survey_id=survey_id,
            contact_id=contact_id,
            request_options=request_options,
        )
        return _response.data

    async def create_response(
        self,
        *,
        survey_id: str,
        finished: bool,
        data: typing.Dict[str, CreateResponseRequestDataValue],
        created_at: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        single_use_id: typing.Optional[str] = OMIT,
        ending_id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        variables: typing.Optional[typing.Dict[str, CreateResponseRequestVariablesValue]] = OMIT,
        ttc: typing.Optional[typing.Dict[str, float]] = OMIT,
        meta: typing.Optional[CreateResponseRequestMeta] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateResponseResponse:
        """
        Creates a response in the database. This will trigger the response pipeline, including webhooks, integrations, follow-up emails, and other configured actions.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        finished : bool
            Whether the response is finished

        data : typing.Dict[str, CreateResponseRequestDataValue]
            The data of the response

        created_at : typing.Optional[str]
            The date and time the response was created

        updated_at : typing.Optional[str]
            The date and time the response was last updated

        display_id : typing.Optional[str]
            The display ID of the response

        single_use_id : typing.Optional[str]
            The single use ID of the response

        ending_id : typing.Optional[str]
            The ID of the ending

        language : typing.Optional[str]
            The language of the response

        variables : typing.Optional[typing.Dict[str, CreateResponseRequestVariablesValue]]
            The variables of the response

        ttc : typing.Optional[typing.Dict[str, float]]
            The TTC of the response

        meta : typing.Optional[CreateResponseRequestMeta]
            The meta data of the response

        user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateResponseResponse
            Response created successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_responses.create_response(
                survey_id="surveyId",
                finished=True,
                data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_response(
            survey_id=survey_id,
            finished=finished,
            data=data,
            created_at=created_at,
            updated_at=updated_at,
            display_id=display_id,
            single_use_id=single_use_id,
            ending_id=ending_id,
            language=language,
            variables=variables,
            ttc=ttc,
            meta=meta,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    async def get_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetResponseResponse:
        """
        Gets a response from the database.

        Parameters
        ----------
        id : ResponseId
            The ID of the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponseResponse
            Response retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_responses.get_response(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_response(id, request_options=request_options)
        return _response.data

    async def update_response(
        self,
        id: ResponseId,
        *,
        finished: typing.Optional[bool] = OMIT,
        ending_id: typing.Optional[str] = OMIT,
        data: typing.Optional[typing.Dict[str, UpdateResponseRequestDataValue]] = OMIT,
        variables: typing.Optional[typing.Dict[str, UpdateResponseRequestVariablesValue]] = OMIT,
        ttc: typing.Optional[typing.Dict[str, float]] = OMIT,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateResponseResponse:
        """
        Updates a response in the database. This will trigger the response pipeline, including webhooks, integrations, follow-up emails (if the response is marked as finished), and other configured actions.

        Parameters
        ----------
        id : ResponseId
            The ID of the response

        finished : typing.Optional[bool]

        ending_id : typing.Optional[str]

        data : typing.Optional[typing.Dict[str, UpdateResponseRequestDataValue]]

        variables : typing.Optional[typing.Dict[str, UpdateResponseRequestVariablesValue]]

        ttc : typing.Optional[typing.Dict[str, float]]

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateResponseResponse
            Response updated successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_responses.update_response(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_response(
            id,
            finished=finished,
            ending_id=ending_id,
            data=data,
            variables=variables,
            ttc=ttc,
            language=language,
            request_options=request_options,
        )
        return _response.data

    async def delete_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteResponseResponse:
        """
        Deletes a response from the database.

        Parameters
        ----------
        id : ResponseId
            The ID of the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteResponseResponse
            Response deleted successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_responses.delete_response(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_response(id, request_options=request_options)
        return _response.data
