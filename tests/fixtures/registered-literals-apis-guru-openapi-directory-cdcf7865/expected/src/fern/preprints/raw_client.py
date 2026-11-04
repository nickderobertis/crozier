

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
from .types.preprints_bibliographic_contributors_list_response_item import (
    PreprintsBibliographicContributorsListResponseItem,
)
from .types.preprints_citation_list_response import PreprintsCitationListResponse
from .types.preprints_citation_read_response import PreprintsCitationReadResponse
from .types.preprints_contributors_create_request_attributes import PreprintsContributorsCreateRequestAttributes
from .types.preprints_contributors_list_response_item import PreprintsContributorsListResponseItem
from .types.preprints_create_request_attributes import PreprintsCreateRequestAttributes
from .types.preprints_create_request_relationships import PreprintsCreateRequestRelationships
from .types.preprints_list_response_item import PreprintsListResponseItem
from .types.preprints_read_response import PreprintsReadResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPreprintsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PreprintsListResponseItem]]:
        """

        A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]=socarxiv.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PreprintsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "preprints/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintsListResponseItem],
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

    def create(
        self,
        *,
        relationships: PreprintsCreateRequestRelationships,
        type: str,
        attributes: typing.Optional[PreprintsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Creates a new preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        relationships : PreprintsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the preprint entity.

        type : str
            The type identifier of the preprint entity (`preprints`).

        attributes : typing.Optional[PreprintsCreateRequestAttributes]
            The properties of the preprint entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "preprints/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=PreprintsCreateRequestAttributes, direction="write"
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships, annotation=PreprintsCreateRequestRelationships, direction="write"
                ),
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreprintsReadResponse]:
        """
        Retrieves the details of a preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreprintsReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintsReadResponse,
                    parse_obj_as(
                        type_=PreprintsReadResponse,
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

    def partial_update(
        self,
        preprint_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bibliographic_contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PreprintsBibliographicContributorsListResponseItem]]:
        """
        A paginated list of the Preprint's Bibliographic Contributors, sorted by their index.
        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PreprintsBibliographicContributorsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/bibliographic_contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintsBibliographicContributorsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintsBibliographicContributorsListResponseItem],
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

    def citation_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreprintsCitationListResponse]:
        """
        The citation details for a preprint, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the preprint citation.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint whose citation you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreprintsCitationListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/citation/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintsCitationListResponse,
                    parse_obj_as(
                        type_=PreprintsCitationListResponse,
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

    def citation_read(
        self, preprint_id: str, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreprintsCitationReadResponse]:
        """
        The citation for a preprint in a specific style.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the preprint citation, in the requested style.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreprintsCitationReadResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/citation/{encode_path_param(style_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintsCitationReadResponse,
                    parse_obj_as(
                        type_=PreprintsCitationReadResponse,
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

    def contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PreprintsContributorsListResponseItem]]:
        """
        A paginated list of the Preprint's Contributors, sorted by their index.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PreprintsContributorsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintsContributorsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintsContributorsListResponseItem],
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

    def contributors_create(
        self,
        preprint_id: str,
        *,
        attributes: typing.Optional[PreprintsContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a Preprint.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.

        All attributes describing the relationship between the Preprint and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        attributes : typing.Optional[PreprintsContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/contributors/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=PreprintsContributorsCreateRequestAttributes, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def contributor_read(
        self, preprint_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Retrieves the details of a contributor on this Preprint.
        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/contributors/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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


class AsyncRawPreprintsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PreprintsListResponseItem]]:
        """

        A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]=socarxiv.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PreprintsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "preprints/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintsListResponseItem],
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

    async def create(
        self,
        *,
        relationships: PreprintsCreateRequestRelationships,
        type: str,
        attributes: typing.Optional[PreprintsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Creates a new preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        relationships : PreprintsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the preprint entity.

        type : str
            The type identifier of the preprint entity (`preprints`).

        attributes : typing.Optional[PreprintsCreateRequestAttributes]
            The properties of the preprint entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "preprints/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=PreprintsCreateRequestAttributes, direction="write"
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships, annotation=PreprintsCreateRequestRelationships, direction="write"
                ),
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreprintsReadResponse]:
        """
        Retrieves the details of a preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreprintsReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintsReadResponse,
                    parse_obj_as(
                        type_=PreprintsReadResponse,
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

    async def partial_update(
        self,
        preprint_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bibliographic_contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PreprintsBibliographicContributorsListResponseItem]]:
        """
        A paginated list of the Preprint's Bibliographic Contributors, sorted by their index.
        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PreprintsBibliographicContributorsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/bibliographic_contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintsBibliographicContributorsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintsBibliographicContributorsListResponseItem],
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

    async def citation_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreprintsCitationListResponse]:
        """
        The citation details for a preprint, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the preprint citation.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint whose citation you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreprintsCitationListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/citation/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintsCitationListResponse,
                    parse_obj_as(
                        type_=PreprintsCitationListResponse,
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

    async def citation_read(
        self, preprint_id: str, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreprintsCitationReadResponse]:
        """
        The citation for a preprint in a specific style.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the preprint citation, in the requested style.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreprintsCitationReadResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/citation/{encode_path_param(style_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintsCitationReadResponse,
                    parse_obj_as(
                        type_=PreprintsCitationReadResponse,
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

    async def contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PreprintsContributorsListResponseItem]]:
        """
        A paginated list of the Preprint's Contributors, sorted by their index.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PreprintsContributorsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintsContributorsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintsContributorsListResponseItem],
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

    async def contributors_create(
        self,
        preprint_id: str,
        *,
        attributes: typing.Optional[PreprintsContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a Preprint.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.

        All attributes describing the relationship between the Preprint and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        attributes : typing.Optional[PreprintsContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/contributors/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=PreprintsContributorsCreateRequestAttributes, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def contributor_read(
        self, preprint_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Retrieves the details of a contributor on this Preprint.
        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprints/{encode_path_param(preprint_id)}/contributors/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
