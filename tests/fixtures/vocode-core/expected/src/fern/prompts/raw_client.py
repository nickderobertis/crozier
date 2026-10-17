

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.collect_field import CollectField
from ..types.http_validation_error import HttpValidationError
from ..types.prompt import Prompt
from ..types.prompt_page import PromptPage
from ..types.prompt_params_prompt_template import PromptParamsPromptTemplate
from ..types.prompt_update_params_collect_fields import PromptUpdateParamsCollectFields
from ..types.prompt_update_params_content import PromptUpdateParamsContent
from ..types.prompt_update_params_context_endpoint import PromptUpdateParamsContextEndpoint
from ..types.prompt_update_params_prompt_template import PromptUpdateParamsPromptTemplate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_prompt(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Prompt]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompts",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_prompts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PromptPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PromptPage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompts/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PromptPage,
                    parse_obj_as(
                        type_=PromptPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_prompt(
        self,
        *,
        content: typing.Optional[str] = OMIT,
        collect_fields: typing.Optional[typing.Sequence[CollectField]] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[PromptParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Prompt]:
        """
        Parameters
        ----------
        content : typing.Optional[str]

        collect_fields : typing.Optional[typing.Sequence[CollectField]]

        context_endpoint : typing.Optional[str]

        prompt_template : typing.Optional[PromptParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompts/create",
            method="POST",
            json={
                "content": content,
                "collect_fields": convert_and_respect_annotation_metadata(
                    object_=collect_fields, annotation=typing.Optional[typing.Sequence[CollectField]], direction="write"
                ),
                "context_endpoint": context_endpoint,
                "prompt_template": convert_and_respect_annotation_metadata(
                    object_=prompt_template, annotation=typing.Optional[PromptParamsPromptTemplate], direction="write"
                ),
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_prompt(
        self,
        *,
        id: str,
        content: typing.Optional[PromptUpdateParamsContent] = OMIT,
        collect_fields: typing.Optional[PromptUpdateParamsCollectFields] = OMIT,
        context_endpoint: typing.Optional[PromptUpdateParamsContextEndpoint] = OMIT,
        prompt_template: typing.Optional[PromptUpdateParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Prompt]:
        """
        Parameters
        ----------
        id : str

        content : typing.Optional[PromptUpdateParamsContent]

        collect_fields : typing.Optional[PromptUpdateParamsCollectFields]

        context_endpoint : typing.Optional[PromptUpdateParamsContextEndpoint]

        prompt_template : typing.Optional[PromptUpdateParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompts/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=PromptUpdateParamsContent, direction="write"
                ),
                "collect_fields": convert_and_respect_annotation_metadata(
                    object_=collect_fields,
                    annotation=typing.Optional[PromptUpdateParamsCollectFields],
                    direction="write",
                ),
                "context_endpoint": convert_and_respect_annotation_metadata(
                    object_=context_endpoint,
                    annotation=typing.Optional[PromptUpdateParamsContextEndpoint],
                    direction="write",
                ),
                "prompt_template": convert_and_respect_annotation_metadata(
                    object_=prompt_template,
                    annotation=typing.Optional[PromptUpdateParamsPromptTemplate],
                    direction="write",
                ),
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPromptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_prompt(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Prompt]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompts",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_prompts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PromptPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PromptPage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompts/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PromptPage,
                    parse_obj_as(
                        type_=PromptPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_prompt(
        self,
        *,
        content: typing.Optional[str] = OMIT,
        collect_fields: typing.Optional[typing.Sequence[CollectField]] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[PromptParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Prompt]:
        """
        Parameters
        ----------
        content : typing.Optional[str]

        collect_fields : typing.Optional[typing.Sequence[CollectField]]

        context_endpoint : typing.Optional[str]

        prompt_template : typing.Optional[PromptParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompts/create",
            method="POST",
            json={
                "content": content,
                "collect_fields": convert_and_respect_annotation_metadata(
                    object_=collect_fields, annotation=typing.Optional[typing.Sequence[CollectField]], direction="write"
                ),
                "context_endpoint": context_endpoint,
                "prompt_template": convert_and_respect_annotation_metadata(
                    object_=prompt_template, annotation=typing.Optional[PromptParamsPromptTemplate], direction="write"
                ),
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_prompt(
        self,
        *,
        id: str,
        content: typing.Optional[PromptUpdateParamsContent] = OMIT,
        collect_fields: typing.Optional[PromptUpdateParamsCollectFields] = OMIT,
        context_endpoint: typing.Optional[PromptUpdateParamsContextEndpoint] = OMIT,
        prompt_template: typing.Optional[PromptUpdateParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Prompt]:
        """
        Parameters
        ----------
        id : str

        content : typing.Optional[PromptUpdateParamsContent]

        collect_fields : typing.Optional[PromptUpdateParamsCollectFields]

        context_endpoint : typing.Optional[PromptUpdateParamsContextEndpoint]

        prompt_template : typing.Optional[PromptUpdateParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompts/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=PromptUpdateParamsContent, direction="write"
                ),
                "collect_fields": convert_and_respect_annotation_metadata(
                    object_=collect_fields,
                    annotation=typing.Optional[PromptUpdateParamsCollectFields],
                    direction="write",
                ),
                "context_endpoint": convert_and_respect_annotation_metadata(
                    object_=context_endpoint,
                    annotation=typing.Optional[PromptUpdateParamsContextEndpoint],
                    direction="write",
                ),
                "prompt_template": convert_and_respect_annotation_metadata(
                    object_=prompt_template,
                    annotation=typing.Optional[PromptUpdateParamsPromptTemplate],
                    direction="write",
                ),
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
