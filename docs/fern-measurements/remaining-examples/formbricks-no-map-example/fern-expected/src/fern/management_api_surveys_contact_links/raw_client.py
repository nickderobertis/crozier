

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_contact_links_by_segment_response import GetContactLinksBySegmentResponse
from .types.get_personalized_survey_link_response import GetPersonalizedSurveyLinkResponse
from pydantic import ValidationError


class RawManagementApiSurveysContactLinksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_personalized_survey_link(
        self,
        survey_id: str,
        contact_id: str,
        *,
        expiration_days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPersonalizedSurveyLinkResponse]:
        """
        Retrieves a personalized link for a specific survey.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        contact_id : str
            The ID of the contact

        expiration_days : typing.Optional[int]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPersonalizedSurveyLinkResponse]
            Personalized survey link retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/surveys/{encode_path_param(survey_id)}/contact-links/contacts/{encode_path_param(contact_id)}/",
            method="GET",
            params={
                "expirationDays": expiration_days,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPersonalizedSurveyLinkResponse,
                    parse_obj_as(
                        type_=GetPersonalizedSurveyLinkResponse,
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

    def get_contact_links_by_segment(
        self,
        survey_id: str,
        segment_id: str,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        expiration_days: typing.Optional[float] = None,
        attribute_keys: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetContactLinksBySegmentResponse]:
        """
        Generates personalized survey links for contacts in a segment.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        segment_id : str
            The ID of the segment

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        expiration_days : typing.Optional[float]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        attribute_keys : typing.Optional[str]
            Comma-separated list of contact attribute keys to include in the response. You can have max 20 keys. If not provided, no attributes will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetContactLinksBySegmentResponse]
            Contact links generated successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/surveys/{encode_path_param(survey_id)}/contact-links/segments/{encode_path_param(segment_id)}",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "expirationDays": expiration_days,
                "attributeKeys": attribute_keys,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactLinksBySegmentResponse,
                    parse_obj_as(
                        type_=GetContactLinksBySegmentResponse,
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


class AsyncRawManagementApiSurveysContactLinksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_personalized_survey_link(
        self,
        survey_id: str,
        contact_id: str,
        *,
        expiration_days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPersonalizedSurveyLinkResponse]:
        """
        Retrieves a personalized link for a specific survey.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        contact_id : str
            The ID of the contact

        expiration_days : typing.Optional[int]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPersonalizedSurveyLinkResponse]
            Personalized survey link retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/surveys/{encode_path_param(survey_id)}/contact-links/contacts/{encode_path_param(contact_id)}/",
            method="GET",
            params={
                "expirationDays": expiration_days,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPersonalizedSurveyLinkResponse,
                    parse_obj_as(
                        type_=GetPersonalizedSurveyLinkResponse,
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

    async def get_contact_links_by_segment(
        self,
        survey_id: str,
        segment_id: str,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        expiration_days: typing.Optional[float] = None,
        attribute_keys: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetContactLinksBySegmentResponse]:
        """
        Generates personalized survey links for contacts in a segment.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        segment_id : str
            The ID of the segment

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        expiration_days : typing.Optional[float]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        attribute_keys : typing.Optional[str]
            Comma-separated list of contact attribute keys to include in the response. You can have max 20 keys. If not provided, no attributes will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetContactLinksBySegmentResponse]
            Contact links generated successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/surveys/{encode_path_param(survey_id)}/contact-links/segments/{encode_path_param(segment_id)}",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "expirationDays": expiration_days,
                "attributeKeys": attribute_keys,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactLinksBySegmentResponse,
                    parse_obj_as(
                        type_=GetContactLinksBySegmentResponse,
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
