

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.dataset_governance import DatasetGovernance
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGovernanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_description(
        self, name: str, *, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DatasetGovernance]:
        """
        Set the dataset's description (an empty string clears it).

        Parameters
        ----------
        name : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/description",
            method="PUT",
            json={
                "description": description,
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
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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

    def get_governance(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DatasetGovernance]:
        """
        The dataset's curated tags + description with last-writer attribution (who/when per field).

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/governance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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

    def add_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DatasetGovernance]:
        """
        Add one governance tag (idempotent — re-adding an existing tag is a no-op re-stamp).

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/tags/{encode_path_param(tag)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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

    def remove_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DatasetGovernance]:
        """
        Remove one governance tag (idempotent — removing an absent tag is a no-op re-stamp).

        Deliberately unvalidated: removal only filters an existing element out of storage, so any string is
        safe — and it lets a curator purge a non-conforming tag (e.g. an old producer label) that the add
        path would refuse.

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/tags/{encode_path_param(tag)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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


class AsyncRawGovernanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_description(
        self, name: str, *, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DatasetGovernance]:
        """
        Set the dataset's description (an empty string clears it).

        Parameters
        ----------
        name : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/description",
            method="PUT",
            json={
                "description": description,
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
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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

    async def get_governance(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DatasetGovernance]:
        """
        The dataset's curated tags + description with last-writer attribution (who/when per field).

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/governance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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

    async def add_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DatasetGovernance]:
        """
        Add one governance tag (idempotent — re-adding an existing tag is a no-op re-stamp).

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/tags/{encode_path_param(tag)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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

    async def remove_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DatasetGovernance]:
        """
        Remove one governance tag (idempotent — removing an absent tag is a no-op re-stamp).

        Deliberately unvalidated: removal only filters an existing element out of storage, so any string is
        safe — and it lets a curator purge a non-conforming tag (e.g. an old producer label) that the add
        path would refuse.

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetGovernance]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/tags/{encode_path_param(tag)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetGovernance,
                    parse_obj_as(
                        type_=DatasetGovernance,
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
