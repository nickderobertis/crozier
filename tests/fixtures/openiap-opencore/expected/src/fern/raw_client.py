

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.collection import Collection
from .types.create_collection_options_timeseries import CreateCollectionOptionsTimeseries
from .types.i_record_of_any import IRecordOfAny
from .types.i_string_to_string_dictionary import IStringToStringDictionary
from .types.query_params_sort import QueryParamsSort
from .types.user import User
from .types.workflow import Workflow
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.List[User]]:
        """
        Returns the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[User]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    def get_users(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[User]]:
        """
        Return a list of users ( max 100 by default)
        each users properties are limited to name, username, email, lastseen, Ude GetUser with _id to get all properties

        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[User]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/users",
            method="GET",
            params={
                "limit": limit,
                "projection": projection,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    def create_user(
        self,
        *,
        name: str,
        email: str,
        username: str,
        newpassword: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """
        Parameters
        ----------
        name : str

        email : str

        username : str

        newpassword : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/users",
            method="POST",
            json={
                "name": name,
                "email": email,
                "username": username,
                "newpassword": newpassword,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    def get_user(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[User]:
        """
        Return a user by _id

        Parameters
        ----------
        id : str
            _id of user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            User
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    def delete_user(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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

    def get_openrpaworkflows(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Workflow]]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Workflow]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/openrpaworkflows",
            method="GET",
            params={
                "limit": limit,
                "projection": projection,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Workflow],
                    parse_obj_as(
                        type_=typing.List[Workflow],
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

    def create_open_rpa_workflow(
        self,
        *,
        name: str,
        background: bool,
        serializable: bool,
        filename: str,
        projectandname: str,
        xaml: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Workflow]:
        """
        Parameters
        ----------
        name : str

        background : bool

        serializable : bool

        filename : str

        projectandname : str

        xaml : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Workflow]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/openrpaworkflows",
            method="POST",
            json={
                "name": name,
                "background": background,
                "Serializable": serializable,
                "Filename": filename,
                "projectandname": projectandname,
                "Xaml": xaml,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
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

    def get_open_rpa_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Workflow]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Workflow]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/openrpaworkflows/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
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

    def delete_open_rpa_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/openrpaworkflows/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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

    def get_collections(
        self, *, includesystem: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Collection]]:
        """
        Parameters
        ----------
        includesystem : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Collection]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/collections",
            method="GET",
            params={
                "includesystem": includesystem,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Collection],
                    parse_obj_as(
                        type_=typing.List[Collection],
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

    def create_collection(
        self,
        *,
        name: str,
        timeseries: typing.Optional[CreateCollectionOptionsTimeseries] = OMIT,
        expire_after_seconds: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Collection]:
        """
        Parameters
        ----------
        name : str

        timeseries : typing.Optional[CreateCollectionOptionsTimeseries]

        expire_after_seconds : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/collections",
            method="POST",
            json={
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=CreateCollectionOptionsTimeseries, direction="write"
                ),
                "expireAfterSeconds": expire_after_seconds,
                "name": name,
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
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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

    def get_collection(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Collection]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/collections/{encode_path_param(collectionname)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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

    def drop_collection(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/collections/{encode_path_param(collectionname)}",
            method="DELETE",
            request_options=request_options,
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

    def get_indexes(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/indexes/{encode_path_param(collectionname)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    def create_index(
        self,
        collectionname: str,
        *,
        keypath: IRecordOfAny,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        collectionname : str

        keypath : IRecordOfAny

        name : typing.Optional[str]

        options : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/indexes/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "name": name,
                "options": options,
                "keypath": keypath,
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
                    str,
                    parse_obj_as(
                        type_=str,
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

    def drop_index(
        self, collectionname: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        collectionname : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/indexes/{encode_path_param(collectionname)}/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
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

    def query(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        sort: typing.Optional[QueryParamsSort] = OMIT,
        skip: typing.Optional[float] = OMIT,
        top: typing.Optional[float] = OMIT,
        projection: typing.Optional[IStringToStringDictionary] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        sort : typing.Optional[QueryParamsSort]

        skip : typing.Optional[float]

        top : typing.Optional[float]

        projection : typing.Optional[IStringToStringDictionary]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/query/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "explain": explain,
                "queryas": queryas,
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=QueryParamsSort, direction="write"
                ),
                "skip": skip,
                "top": top,
                "projection": projection,
                "query": query,
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
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    def count(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[float]:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[float]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/count/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "queryas": queryas,
                "query": query,
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
                    float,
                    parse_obj_as(
                        type_=float,
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

    def distinct(
        self,
        collectionname: str,
        *,
        field: str,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        collectionname : str

        field : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/distinct/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "queryas": queryas,
                "field": field,
                "query": query,
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
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def aggregate(
        self,
        collectionname: str,
        *,
        pipeline: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        collectionname : str

        pipeline : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/aggregate/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "explain": explain,
                "queryas": queryas,
                "pipeline": pipeline,
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
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    def run_open_rpa_workflow(
        self,
        robotname: str,
        *,
        rpc: bool,
        workflowid: str,
        parameters: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IRecordOfAny]:
        """
        Parameters
        ----------
        robotname : str

        rpc : bool

        workflowid : str

        parameters : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IRecordOfAny]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/runopenrpaworkflow/{encode_path_param(robotname)}",
            method="POST",
            json={
                "rpc": rpc,
                "Parameters": parameters,
                "workflowid": workflowid,
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
                    IRecordOfAny,
                    parse_obj_as(
                        type_=IRecordOfAny,
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

    def queue_message(
        self, queuename: str, *, rpc: bool, payload: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IRecordOfAny]:
        """
        Parameters
        ----------
        queuename : str

        rpc : bool

        payload : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IRecordOfAny]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/queuemessage/{encode_path_param(queuename)}",
            method="POST",
            json={
                "rpc": rpc,
                "Payload": payload,
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
                    IRecordOfAny,
                    parse_obj_as(
                        type_=IRecordOfAny,
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

    async def me(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[User]]:
        """
        Returns the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[User]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    async def get_users(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[User]]:
        """
        Return a list of users ( max 100 by default)
        each users properties are limited to name, username, email, lastseen, Ude GetUser with _id to get all properties

        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[User]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/users",
            method="GET",
            params={
                "limit": limit,
                "projection": projection,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    async def create_user(
        self,
        *,
        name: str,
        email: str,
        username: str,
        newpassword: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """
        Parameters
        ----------
        name : str

        email : str

        username : str

        newpassword : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/users",
            method="POST",
            json={
                "name": name,
                "email": email,
                "username": username,
                "newpassword": newpassword,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    async def get_user(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Return a user by _id

        Parameters
        ----------
        id : str
            _id of user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            User
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    async def delete_user(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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

    async def get_openrpaworkflows(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Workflow]]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Workflow]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/openrpaworkflows",
            method="GET",
            params={
                "limit": limit,
                "projection": projection,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Workflow],
                    parse_obj_as(
                        type_=typing.List[Workflow],
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

    async def create_open_rpa_workflow(
        self,
        *,
        name: str,
        background: bool,
        serializable: bool,
        filename: str,
        projectandname: str,
        xaml: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Workflow]:
        """
        Parameters
        ----------
        name : str

        background : bool

        serializable : bool

        filename : str

        projectandname : str

        xaml : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Workflow]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/openrpaworkflows",
            method="POST",
            json={
                "name": name,
                "background": background,
                "Serializable": serializable,
                "Filename": filename,
                "projectandname": projectandname,
                "Xaml": xaml,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
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

    async def get_open_rpa_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Workflow]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Workflow]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/openrpaworkflows/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
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

    async def delete_open_rpa_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/openrpaworkflows/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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

    async def get_collections(
        self, *, includesystem: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Collection]]:
        """
        Parameters
        ----------
        includesystem : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Collection]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/collections",
            method="GET",
            params={
                "includesystem": includesystem,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Collection],
                    parse_obj_as(
                        type_=typing.List[Collection],
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

    async def create_collection(
        self,
        *,
        name: str,
        timeseries: typing.Optional[CreateCollectionOptionsTimeseries] = OMIT,
        expire_after_seconds: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Collection]:
        """
        Parameters
        ----------
        name : str

        timeseries : typing.Optional[CreateCollectionOptionsTimeseries]

        expire_after_seconds : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/collections",
            method="POST",
            json={
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=CreateCollectionOptionsTimeseries, direction="write"
                ),
                "expireAfterSeconds": expire_after_seconds,
                "name": name,
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
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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

    async def get_collection(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Collection]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/collections/{encode_path_param(collectionname)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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

    async def drop_collection(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/collections/{encode_path_param(collectionname)}",
            method="DELETE",
            request_options=request_options,
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

    async def get_indexes(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/indexes/{encode_path_param(collectionname)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    async def create_index(
        self,
        collectionname: str,
        *,
        keypath: IRecordOfAny,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        collectionname : str

        keypath : IRecordOfAny

        name : typing.Optional[str]

        options : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/indexes/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "name": name,
                "options": options,
                "keypath": keypath,
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
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def drop_index(
        self, collectionname: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        collectionname : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/indexes/{encode_path_param(collectionname)}/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
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

    async def query(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        sort: typing.Optional[QueryParamsSort] = OMIT,
        skip: typing.Optional[float] = OMIT,
        top: typing.Optional[float] = OMIT,
        projection: typing.Optional[IStringToStringDictionary] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        sort : typing.Optional[QueryParamsSort]

        skip : typing.Optional[float]

        top : typing.Optional[float]

        projection : typing.Optional[IStringToStringDictionary]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/query/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "explain": explain,
                "queryas": queryas,
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=QueryParamsSort, direction="write"
                ),
                "skip": skip,
                "top": top,
                "projection": projection,
                "query": query,
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
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    async def count(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[float]:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[float]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/count/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "queryas": queryas,
                "query": query,
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
                    float,
                    parse_obj_as(
                        type_=float,
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

    async def distinct(
        self,
        collectionname: str,
        *,
        field: str,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        collectionname : str

        field : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/distinct/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "queryas": queryas,
                "field": field,
                "query": query,
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
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def aggregate(
        self,
        collectionname: str,
        *,
        pipeline: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        collectionname : str

        pipeline : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/aggregate/{encode_path_param(collectionname)}",
            method="POST",
            json={
                "explain": explain,
                "queryas": queryas,
                "pipeline": pipeline,
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
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    async def run_open_rpa_workflow(
        self,
        robotname: str,
        *,
        rpc: bool,
        workflowid: str,
        parameters: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IRecordOfAny]:
        """
        Parameters
        ----------
        robotname : str

        rpc : bool

        workflowid : str

        parameters : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IRecordOfAny]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/runopenrpaworkflow/{encode_path_param(robotname)}",
            method="POST",
            json={
                "rpc": rpc,
                "Parameters": parameters,
                "workflowid": workflowid,
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
                    IRecordOfAny,
                    parse_obj_as(
                        type_=IRecordOfAny,
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

    async def queue_message(
        self, queuename: str, *, rpc: bool, payload: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IRecordOfAny]:
        """
        Parameters
        ----------
        queuename : str

        rpc : bool

        payload : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IRecordOfAny]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/queuemessage/{encode_path_param(queuename)}",
            method="POST",
            json={
                "rpc": rpc,
                "Payload": payload,
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
                    IRecordOfAny,
                    parse_obj_as(
                        type_=IRecordOfAny,
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
