

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.create_plan_body_course import CreatePlanBodyCourse
from .types.create_plan_body_diet import CreatePlanBodyDiet
from .types.plan import Plan
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_plan(
        self,
        *,
        course: typing.Optional[CreatePlanBodyCourse] = OMIT,
        diet: typing.Optional[CreatePlanBodyDiet] = OMIT,
        servings: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Plan]:
        """
        Parameters
        ----------
        course : typing.Optional[CreatePlanBodyCourse]
            Which course to plan, if any.

        diet : typing.Optional[CreatePlanBodyDiet]
            Dietary needs the plan must respect.

        servings : typing.Optional[int]
            How many people eat.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Plan]
            The plan
        """
        _response = self._client_wrapper.httpx_client.request(
            "plans",
            method="POST",
            json={
                "course": course,
                "diet": convert_and_respect_annotation_metadata(
                    object_=diet, annotation=typing.Optional[CreatePlanBodyDiet], direction="write"
                ),
                "servings": servings,
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
                    Plan,
                    parse_obj_as(
                        type_=Plan,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_plan(
        self,
        *,
        course: typing.Optional[CreatePlanBodyCourse] = OMIT,
        diet: typing.Optional[CreatePlanBodyDiet] = OMIT,
        servings: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Plan]:
        """
        Parameters
        ----------
        course : typing.Optional[CreatePlanBodyCourse]
            Which course to plan, if any.

        diet : typing.Optional[CreatePlanBodyDiet]
            Dietary needs the plan must respect.

        servings : typing.Optional[int]
            How many people eat.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Plan]
            The plan
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plans",
            method="POST",
            json={
                "course": course,
                "diet": convert_and_respect_annotation_metadata(
                    object_=diet, annotation=typing.Optional[CreatePlanBodyDiet], direction="write"
                ),
                "servings": servings,
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
                    Plan,
                    parse_obj_as(
                        type_=Plan,
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
