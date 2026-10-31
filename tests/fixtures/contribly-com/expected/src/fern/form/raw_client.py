

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
from ..errors.not_found_error import NotFoundError
from ..types.form import Form
from ..types.form_field import FormField
from ..types.form_response import FormResponse
from ..types.tag import Tag
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFormClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_form_responses(
        self,
        *,
        user: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        contribution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FormResponse]]:
        """
        Parameters
        ----------
        user : typing.Optional[str]
            Restrict results to responses submitted by this user.

        form : typing.Optional[str]
            Restrict results to responses submitted to this form.

        contribution : typing.Optional[str]
            Restrict results to responses relating to this contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FormResponse]]
            A list of form responses
        """
        _response = self._client_wrapper.httpx_client.request(
            "form-responses",
            method="GET",
            params={
                "user": user,
                "form": form,
                "contribution": contribution,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FormResponse],
                    parse_obj_as(
                        type_=typing.List[FormResponse],
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

    def submit_a_response_to_a_form(
        self,
        *,
        contribution: typing.Optional[str] = OMIT,
        form: typing.Optional[str] = OMIT,
        responses: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FormResponse]:
        """
        Parameters
        ----------
        contribution : typing.Optional[str]

        form : typing.Optional[str]

        responses : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FormResponse]
            Form response saved
        """
        _response = self._client_wrapper.httpx_client.request(
            "form-responses",
            method="POST",
            json={
                "contribution": contribution,
                "form": form,
                "responses": responses,
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
                    FormResponse,
                    parse_obj_as(
                        type_=FormResponse,
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

    def get_a_single_form_response_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FormResponse]:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FormResponse]
            Form response found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"form-responses/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FormResponse,
                    parse_obj_as(
                        type_=FormResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def list_forms(
        self, *, owned_by: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Form]]:
        """
        Parameters
        ----------
        owned_by : str
            Restrict results to forms owned by this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Form]]
            A list of forms
        """
        _response = self._client_wrapper.httpx_client.request(
            "forms",
            method="GET",
            params={
                "ownedBy": owned_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Form],
                    parse_obj_as(
                        type_=typing.List[Form],
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

    def create_a_form(
        self,
        *,
        call_to_action: typing.Optional[str] = OMIT,
        css_url: typing.Optional[str] = OMIT,
        fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        heading: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        no_css: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Form]:
        """
        Parameters
        ----------
        call_to_action : typing.Optional[str]

        css_url : typing.Optional[str]

        fields : typing.Optional[typing.Sequence[FormField]]

        heading : typing.Optional[str]

        name : typing.Optional[str]

        no_css : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[Tag]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Form]
            Form created
        """
        _response = self._client_wrapper.httpx_client.request(
            "forms",
            method="POST",
            json={
                "callToAction": call_to_action,
                "cssUrl": css_url,
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "heading": heading,
                "name": name,
                "noCss": no_css,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[Tag], direction="write"
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
                    Form,
                    parse_obj_as(
                        type_=Form,
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

    def get_a_single_form_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Form]:
        """
        Parameters
        ----------
        id : str
            Id of the form to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Form]
            Form found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"forms/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Form,
                    parse_obj_as(
                        type_=Form,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def delete_this_form_and_all_of_its_responses(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Id of the form to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"forms/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawFormClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_form_responses(
        self,
        *,
        user: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        contribution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FormResponse]]:
        """
        Parameters
        ----------
        user : typing.Optional[str]
            Restrict results to responses submitted by this user.

        form : typing.Optional[str]
            Restrict results to responses submitted to this form.

        contribution : typing.Optional[str]
            Restrict results to responses relating to this contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FormResponse]]
            A list of form responses
        """
        _response = await self._client_wrapper.httpx_client.request(
            "form-responses",
            method="GET",
            params={
                "user": user,
                "form": form,
                "contribution": contribution,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FormResponse],
                    parse_obj_as(
                        type_=typing.List[FormResponse],
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

    async def submit_a_response_to_a_form(
        self,
        *,
        contribution: typing.Optional[str] = OMIT,
        form: typing.Optional[str] = OMIT,
        responses: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FormResponse]:
        """
        Parameters
        ----------
        contribution : typing.Optional[str]

        form : typing.Optional[str]

        responses : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FormResponse]
            Form response saved
        """
        _response = await self._client_wrapper.httpx_client.request(
            "form-responses",
            method="POST",
            json={
                "contribution": contribution,
                "form": form,
                "responses": responses,
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
                    FormResponse,
                    parse_obj_as(
                        type_=FormResponse,
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

    async def get_a_single_form_response_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FormResponse]:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FormResponse]
            Form response found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"form-responses/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FormResponse,
                    parse_obj_as(
                        type_=FormResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def list_forms(
        self, *, owned_by: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Form]]:
        """
        Parameters
        ----------
        owned_by : str
            Restrict results to forms owned by this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Form]]
            A list of forms
        """
        _response = await self._client_wrapper.httpx_client.request(
            "forms",
            method="GET",
            params={
                "ownedBy": owned_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Form],
                    parse_obj_as(
                        type_=typing.List[Form],
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

    async def create_a_form(
        self,
        *,
        call_to_action: typing.Optional[str] = OMIT,
        css_url: typing.Optional[str] = OMIT,
        fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        heading: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        no_css: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Form]:
        """
        Parameters
        ----------
        call_to_action : typing.Optional[str]

        css_url : typing.Optional[str]

        fields : typing.Optional[typing.Sequence[FormField]]

        heading : typing.Optional[str]

        name : typing.Optional[str]

        no_css : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[Tag]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Form]
            Form created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "forms",
            method="POST",
            json={
                "callToAction": call_to_action,
                "cssUrl": css_url,
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "heading": heading,
                "name": name,
                "noCss": no_css,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[Tag], direction="write"
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
                    Form,
                    parse_obj_as(
                        type_=Form,
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

    async def get_a_single_form_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Form]:
        """
        Parameters
        ----------
        id : str
            Id of the form to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Form]
            Form found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"forms/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Form,
                    parse_obj_as(
                        type_=Form,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def delete_this_form_and_all_of_its_responses(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Id of the form to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"forms/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
