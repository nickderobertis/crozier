

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.response_id import ResponseId
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManagementApiResponsesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[GetResponsesResponse]:
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
        HttpResponse[GetResponsesResponse]
            Responses retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/responses",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "surveyId": survey_id,
                "contactId": contact_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetResponsesResponse,
                    parse_obj_as(
                        type_=GetResponsesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CreateResponseResponse]:
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
        HttpResponse[CreateResponseResponse]
            Response created successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/responses",
            method="POST",
            json={
                "createdAt": created_at,
                "updatedAt": updated_at,
                "surveyId": survey_id,
                "displayId": display_id,
                "singleUseId": single_use_id,
                "finished": finished,
                "endingId": ending_id,
                "language": language,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Dict[str, CreateResponseRequestDataValue], direction="write"
                ),
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables,
                    annotation=typing.Dict[str, CreateResponseRequestVariablesValue],
                    direction="write",
                ),
                "ttc": ttc,
                "meta": convert_and_respect_annotation_metadata(
                    object_=meta, annotation=CreateResponseRequestMeta, direction="write"
                ),
                "userId": user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateResponseResponse,
                    parse_obj_as(
                        type_=CreateResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetResponseResponse]:
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
        HttpResponse[GetResponseResponse]
            Response retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/responses/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetResponseResponse,
                    parse_obj_as(
                        type_=GetResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[UpdateResponseResponse]:
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
        HttpResponse[UpdateResponseResponse]
            Response updated successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/responses/{encode_path_param(id)}",
            method="PUT",
            json={
                "finished": finished,
                "endingId": ending_id,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Dict[str, UpdateResponseRequestDataValue], direction="write"
                ),
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables,
                    annotation=typing.Dict[str, UpdateResponseRequestVariablesValue],
                    direction="write",
                ),
                "ttc": ttc,
                "language": language,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateResponseResponse,
                    parse_obj_as(
                        type_=UpdateResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteResponseResponse]:
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
        HttpResponse[DeleteResponseResponse]
            Response deleted successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/responses/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteResponseResponse,
                    parse_obj_as(
                        type_=DeleteResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawManagementApiResponsesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[GetResponsesResponse]:
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
        AsyncHttpResponse[GetResponsesResponse]
            Responses retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/responses",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "surveyId": survey_id,
                "contactId": contact_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetResponsesResponse,
                    parse_obj_as(
                        type_=GetResponsesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CreateResponseResponse]:
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
        AsyncHttpResponse[CreateResponseResponse]
            Response created successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/responses",
            method="POST",
            json={
                "createdAt": created_at,
                "updatedAt": updated_at,
                "surveyId": survey_id,
                "displayId": display_id,
                "singleUseId": single_use_id,
                "finished": finished,
                "endingId": ending_id,
                "language": language,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Dict[str, CreateResponseRequestDataValue], direction="write"
                ),
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables,
                    annotation=typing.Dict[str, CreateResponseRequestVariablesValue],
                    direction="write",
                ),
                "ttc": ttc,
                "meta": convert_and_respect_annotation_metadata(
                    object_=meta, annotation=CreateResponseRequestMeta, direction="write"
                ),
                "userId": user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateResponseResponse,
                    parse_obj_as(
                        type_=CreateResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetResponseResponse]:
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
        AsyncHttpResponse[GetResponseResponse]
            Response retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/responses/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetResponseResponse,
                    parse_obj_as(
                        type_=GetResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[UpdateResponseResponse]:
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
        AsyncHttpResponse[UpdateResponseResponse]
            Response updated successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/responses/{encode_path_param(id)}",
            method="PUT",
            json={
                "finished": finished,
                "endingId": ending_id,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Dict[str, UpdateResponseRequestDataValue], direction="write"
                ),
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables,
                    annotation=typing.Dict[str, UpdateResponseRequestVariablesValue],
                    direction="write",
                ),
                "ttc": ttc,
                "language": language,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateResponseResponse,
                    parse_obj_as(
                        type_=UpdateResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_response(
        self, id: ResponseId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteResponseResponse]:
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
        AsyncHttpResponse[DeleteResponseResponse]
            Response deleted successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/responses/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteResponseResponse,
                    parse_obj_as(
                        type_=DeleteResponseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
