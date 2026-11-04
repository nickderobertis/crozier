

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.response_item_thesaurus_concept import ResponseItemThesaurusConcept
from ..types.response_item_thesaurus_concept_scheme import ResponseItemThesaurusConceptScheme
from ..types.response_page_thesaurus_concept import ResponsePageThesaurusConcept
from .types.get_api2thesaurus_level_int_request_form import GetApi2ThesaurusLevelIntRequestForm
from .types.get_api2thesaurus_level_int_request_level import GetApi2ThesaurusLevelIntRequestLevel
from pydantic import ValidationError


class RawThesaurusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_skos_concept_scheme_for_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponseItemThesaurusConceptScheme]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemThesaurusConceptScheme]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/thesaurus",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemThesaurusConceptScheme,
                    parse_obj_as(
                        type_=ResponseItemThesaurusConceptScheme,
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

    def retrieve_skos_concept_from_rdamsc_thesaurus(
        self,
        level: GetApi2ThesaurusLevelIntRequestLevel,
        int_: int,
        *,
        form: typing.Optional[GetApi2ThesaurusLevelIntRequestForm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseItemThesaurusConcept]:
        """
        Parameters
        ----------
        level : GetApi2ThesaurusLevelIntRequestLevel
            String portion of the concept ID.

        int_ : int
            Numeric portion of the concept ID.

        form : typing.Optional[GetApi2ThesaurusLevelIntRequestForm]
            Level of detail to include in the entry.
            - `concept` (default) provides the relationships for just this concept.
            - `tree` recursively provides the IDs for narrower concepts of narrower concepts, and broader concepts of broader concepts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemThesaurusConcept]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/thesaurus/{encode_path_param(level)}{encode_path_param(int_)}",
            method="GET",
            params={
                "form": form,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemThesaurusConcept,
                    parse_obj_as(
                        type_=ResponseItemThesaurusConcept,
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

    def retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageThesaurusConcept]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageThesaurusConcept]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/thesaurus/concepts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageThesaurusConcept,
                    parse_obj_as(
                        type_=ResponsePageThesaurusConcept,
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

    def retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageThesaurusConcept]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageThesaurusConcept]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/thesaurus/concepts/used",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageThesaurusConcept,
                    parse_obj_as(
                        type_=ResponsePageThesaurusConcept,
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


class AsyncRawThesaurusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_skos_concept_scheme_for_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponseItemThesaurusConceptScheme]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemThesaurusConceptScheme]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/thesaurus",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemThesaurusConceptScheme,
                    parse_obj_as(
                        type_=ResponseItemThesaurusConceptScheme,
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

    async def retrieve_skos_concept_from_rdamsc_thesaurus(
        self,
        level: GetApi2ThesaurusLevelIntRequestLevel,
        int_: int,
        *,
        form: typing.Optional[GetApi2ThesaurusLevelIntRequestForm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseItemThesaurusConcept]:
        """
        Parameters
        ----------
        level : GetApi2ThesaurusLevelIntRequestLevel
            String portion of the concept ID.

        int_ : int
            Numeric portion of the concept ID.

        form : typing.Optional[GetApi2ThesaurusLevelIntRequestForm]
            Level of detail to include in the entry.
            - `concept` (default) provides the relationships for just this concept.
            - `tree` recursively provides the IDs for narrower concepts of narrower concepts, and broader concepts of broader concepts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemThesaurusConcept]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/thesaurus/{encode_path_param(level)}{encode_path_param(int_)}",
            method="GET",
            params={
                "form": form,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemThesaurusConcept,
                    parse_obj_as(
                        type_=ResponseItemThesaurusConcept,
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

    async def retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageThesaurusConcept]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageThesaurusConcept]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/thesaurus/concepts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageThesaurusConcept,
                    parse_obj_as(
                        type_=ResponsePageThesaurusConcept,
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

    async def retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageThesaurusConcept]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageThesaurusConcept]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/thesaurus/concepts/used",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageThesaurusConcept,
                    parse_obj_as(
                        type_=ResponsePageThesaurusConcept,
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
