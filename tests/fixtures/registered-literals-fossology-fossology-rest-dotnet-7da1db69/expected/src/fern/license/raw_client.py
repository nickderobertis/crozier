

import contextlib
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.admin_license_acknowledgement import AdminLicenseAcknowledgement
from ..types.get_suggested_license import GetSuggestedLicense
from ..types.info import Info
from ..types.license_candidate import LicenseCandidate
from ..types.mutate_admin_acknowledgement import MutateAdminAcknowledgement
from ..types.mutate_std_comment import MutateStdComment
from ..types.standard_comment import StandardComment
from .types.get_license_by_shortname_response import GetLicenseByShortnameResponse
from .types.get_licenses_request_kind import GetLicensesRequestKind
from .types.get_licenses_response_item import GetLicensesResponseItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLicenseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def import_obligation_csv(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Import an obligation csv file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Successfully imported
        """
        _response = self._client_wrapper.httpx_client.request(
            "obligations/import-csv",
            method="POST",
            data={
                "enclosure": enclosure,
                "delimiter": delimiter,
            },
            files={
                "file_input": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.contextmanager
    def export_license_obligations(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Export a csv license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Successfully exported
        """
        with self._client_wrapper.httpx_client.stream(
            "obligations/export-csv",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def import_obligations_from_json(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Import an obligation json file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Successfully imported
        """
        _response = self._client_wrapper.httpx_client.request(
            "obligations/import-json",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.contextmanager
    def export_obligations_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Export a json license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Successfully exported
        """
        with self._client_wrapper.httpx_client.stream(
            "obligations/export-json",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def get_licenses(
        self,
        *,
        kind: typing.Optional[GetLicensesRequestKind] = None,
        group_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetLicensesResponseItem]]:
        """
        Get a list of available licenses (filtered by kind or status)

        Parameters
        ----------
        kind : typing.Optional[GetLicensesRequestKind]
            Which kind of licenses to get.

        group_name : typing.Optional[str]
            The group name to chose

        page : typing.Optional[int]
            Page number to fetch

        limit : typing.Optional[int]
            Limits of responses per request

        active : typing.Optional[bool]
            Get only active licenses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetLicensesResponseItem]]
            All licenses from database
        """
        _response = self._client_wrapper.httpx_client.request(
            "license",
            method="GET",
            params={
                "kind": kind,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
                "active": str(active) if active is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetLicensesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetLicensesResponseItem],
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

    def create_license(
        self,
        *,
        short_name: str,
        group_name: typing.Optional[str] = None,
        merge_request: typing.Optional[bool] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        is_candidate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Add a new license to the database

        Parameters
        ----------
        short_name : str
            Short name

        group_name : typing.Optional[str]
            The group name to chose

        merge_request : typing.Optional[bool]
            Open a merge request for candidate license?

        full_name : typing.Optional[str]
            Full name

        text : typing.Optional[str]
            License text

        url : typing.Optional[str]
            URL of the license text

        risk : typing.Optional[int]
            Risk level

        is_candidate : typing.Optional[bool]
            Is the license a candidate?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            License added successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "license",
            method="POST",
            json={
                "shortName": short_name,
                "mergeRequest": merge_request,
                "fullName": full_name,
                "text": text,
                "url": url,
                "risk": risk,
                "isCandidate": is_candidate,
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def import_license(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Import a csv license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Successfully imported
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/import-csv",
            method="POST",
            data={
                "enclosure": enclosure,
                "delimiter": delimiter,
            },
            files={
                "file_input": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.contextmanager
    def export_license(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Export a csv license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Successfully exported
        """
        with self._client_wrapper.httpx_client.stream(
            "license/export-csv",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def handle_import_license(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Import a json license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Successfully imported
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/import-json",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.contextmanager
    def export_admin_license_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Export a json license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Successfully exported
        """
        with self._client_wrapper.httpx_client.stream(
            "license/export-json",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def get_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLicenseByShortnameResponse]:
        """
        Get information about a specific license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLicenseByShortnameResponse]
            License
        """
        _response = self._client_wrapper.httpx_client.request(
            f"license/{encode_path_param(shortname)}",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLicenseByShortnameResponse,
                    parse_obj_as(
                        type_=GetLicenseByShortnameResponse,
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

    def update_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Update information about a given license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        full_name : typing.Optional[str]
            New fullname

        text : typing.Optional[str]
            New license text

        url : typing.Optional[str]
            New URL for license

        risk : typing.Optional[int]
            New risk value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            License added successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"license/{encode_path_param(shortname)}",
            method="PATCH",
            json={
                "fullName": full_name,
                "text": text,
                "url": url,
                "risk": risk,
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    def get_admin_license_candidates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LicenseCandidate]]:
        """
        Get a list of license candidates from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LicenseCandidate]]
            Request is successful
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/admincandidates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LicenseCandidate],
                    parse_obj_as(
                        type_=typing.List[LicenseCandidate],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_by_license_candidate_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Delete a single admin-license-candidate by the given id.

        Parameters
        ----------
        id : int
            Id of the license-candidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            License candidate will be deleted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"license/admincandidates/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_admin_license_acknowledgements(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AdminLicenseAcknowledgement]]:
        """
        Get a list of the admin license acknowledgements

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AdminLicenseAcknowledgement]]
            Request is successful
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/adminacknowledgements",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AdminLicenseAcknowledgement],
                    parse_obj_as(
                        type_=typing.List[AdminLicenseAcknowledgement],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def mutate_admin_license_acknowledgement(
        self,
        *,
        request: typing.Sequence[MutateAdminAcknowledgement],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Info]]:
        """
        Add, edit and toggle admin-license acknowledgement

        Parameters
        ----------
        request : typing.Sequence[MutateAdminAcknowledgement]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Info]]
            Request is successful
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/adminacknowledgements",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[MutateAdminAcknowledgement], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_all_standard_license_comments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[StandardComment]]:
        """
        Get a list of all standard license comments.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[StandardComment]]
            Request is successful
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/stdcomments",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[StandardComment],
                    parse_obj_as(
                        type_=typing.List[StandardComment],
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

    def mutate_std_comments(
        self, *, request: typing.Sequence[MutateStdComment], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Info]]:
        """
        Add, edit and toggle standard comments

        Parameters
        ----------
        request : typing.Sequence[MutateStdComment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Info]]
            Request is successful
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/stdcomments",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[MutateStdComment], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def verify_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Verify a license as new or variant of another license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be verified

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            License verified successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"license/verify/{encode_path_param(shortname)}",
            method="PUT",
            json={
                "parentShortname": parent_shortname,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def merge_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Merge a license to another existing license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be merged

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            License merged successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"license/merge/{encode_path_param(shortname)}",
            method="PUT",
            json={
                "parentShortname": parent_shortname,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_suggested_license(
        self, *, reference_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSuggestedLicense]:
        """
        Get a single suggested license by the given reference text.

        Parameters
        ----------
        reference_text : typing.Optional[str]
            Reference text to get suggested license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSuggestedLicense]
            Request is successful
        """
        _response = self._client_wrapper.httpx_client.request(
            "license/suggest",
            method="POST",
            json={
                "referenceText": reference_text,
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
                    GetSuggestedLicense,
                    parse_obj_as(
                        type_=GetSuggestedLicense,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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


class AsyncRawLicenseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def import_obligation_csv(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Import an obligation csv file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Successfully imported
        """
        _response = await self._client_wrapper.httpx_client.request(
            "obligations/import-csv",
            method="POST",
            data={
                "enclosure": enclosure,
                "delimiter": delimiter,
            },
            files={
                "file_input": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.asynccontextmanager
    async def export_license_obligations(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Export a csv license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Successfully exported
        """
        async with self._client_wrapper.httpx_client.stream(
            "obligations/export-csv",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def import_obligations_from_json(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Import an obligation json file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Successfully imported
        """
        _response = await self._client_wrapper.httpx_client.request(
            "obligations/import-json",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.asynccontextmanager
    async def export_obligations_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Export a json license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Successfully exported
        """
        async with self._client_wrapper.httpx_client.stream(
            "obligations/export-json",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def get_licenses(
        self,
        *,
        kind: typing.Optional[GetLicensesRequestKind] = None,
        group_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetLicensesResponseItem]]:
        """
        Get a list of available licenses (filtered by kind or status)

        Parameters
        ----------
        kind : typing.Optional[GetLicensesRequestKind]
            Which kind of licenses to get.

        group_name : typing.Optional[str]
            The group name to chose

        page : typing.Optional[int]
            Page number to fetch

        limit : typing.Optional[int]
            Limits of responses per request

        active : typing.Optional[bool]
            Get only active licenses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetLicensesResponseItem]]
            All licenses from database
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license",
            method="GET",
            params={
                "kind": kind,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
                "active": str(active) if active is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetLicensesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetLicensesResponseItem],
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

    async def create_license(
        self,
        *,
        short_name: str,
        group_name: typing.Optional[str] = None,
        merge_request: typing.Optional[bool] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        is_candidate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Add a new license to the database

        Parameters
        ----------
        short_name : str
            Short name

        group_name : typing.Optional[str]
            The group name to chose

        merge_request : typing.Optional[bool]
            Open a merge request for candidate license?

        full_name : typing.Optional[str]
            Full name

        text : typing.Optional[str]
            License text

        url : typing.Optional[str]
            URL of the license text

        risk : typing.Optional[int]
            Risk level

        is_candidate : typing.Optional[bool]
            Is the license a candidate?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            License added successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license",
            method="POST",
            json={
                "shortName": short_name,
                "mergeRequest": merge_request,
                "fullName": full_name,
                "text": text,
                "url": url,
                "risk": risk,
                "isCandidate": is_candidate,
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def import_license(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Import a csv license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Successfully imported
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/import-csv",
            method="POST",
            data={
                "enclosure": enclosure,
                "delimiter": delimiter,
            },
            files={
                "file_input": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.asynccontextmanager
    async def export_license(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Export a csv license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Successfully exported
        """
        async with self._client_wrapper.httpx_client.stream(
            "license/export-csv",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def handle_import_license(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Import a json license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Successfully imported
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/import-json",
            method="POST",
            data={},
            files={
                "fileInput": file_input,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    @contextlib.asynccontextmanager
    async def export_admin_license_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Export a json license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Successfully exported
        """
        async with self._client_wrapper.httpx_client.stream(
            "license/export-json",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Info,
                                parse_obj_as(
                                    type_=Info,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def get_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLicenseByShortnameResponse]:
        """
        Get information about a specific license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLicenseByShortnameResponse]
            License
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"license/{encode_path_param(shortname)}",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLicenseByShortnameResponse,
                    parse_obj_as(
                        type_=GetLicenseByShortnameResponse,
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

    async def update_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Update information about a given license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        full_name : typing.Optional[str]
            New fullname

        text : typing.Optional[str]
            New license text

        url : typing.Optional[str]
            New URL for license

        risk : typing.Optional[int]
            New risk value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            License added successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"license/{encode_path_param(shortname)}",
            method="PATCH",
            json={
                "fullName": full_name,
                "text": text,
                "url": url,
                "risk": risk,
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    async def get_admin_license_candidates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LicenseCandidate]]:
        """
        Get a list of license candidates from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LicenseCandidate]]
            Request is successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/admincandidates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LicenseCandidate],
                    parse_obj_as(
                        type_=typing.List[LicenseCandidate],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_by_license_candidate_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Delete a single admin-license-candidate by the given id.

        Parameters
        ----------
        id : int
            Id of the license-candidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            License candidate will be deleted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"license/admincandidates/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_admin_license_acknowledgements(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AdminLicenseAcknowledgement]]:
        """
        Get a list of the admin license acknowledgements

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AdminLicenseAcknowledgement]]
            Request is successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/adminacknowledgements",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AdminLicenseAcknowledgement],
                    parse_obj_as(
                        type_=typing.List[AdminLicenseAcknowledgement],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def mutate_admin_license_acknowledgement(
        self,
        *,
        request: typing.Sequence[MutateAdminAcknowledgement],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Info]]:
        """
        Add, edit and toggle admin-license acknowledgement

        Parameters
        ----------
        request : typing.Sequence[MutateAdminAcknowledgement]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Info]]
            Request is successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/adminacknowledgements",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[MutateAdminAcknowledgement], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_all_standard_license_comments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[StandardComment]]:
        """
        Get a list of all standard license comments.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[StandardComment]]
            Request is successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/stdcomments",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[StandardComment],
                    parse_obj_as(
                        type_=typing.List[StandardComment],
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

    async def mutate_std_comments(
        self, *, request: typing.Sequence[MutateStdComment], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Info]]:
        """
        Add, edit and toggle standard comments

        Parameters
        ----------
        request : typing.Sequence[MutateStdComment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Info]]
            Request is successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/stdcomments",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[MutateStdComment], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Info],
                    parse_obj_as(
                        type_=typing.List[Info],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def verify_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Verify a license as new or variant of another license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be verified

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            License verified successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"license/verify/{encode_path_param(shortname)}",
            method="PUT",
            json={
                "parentShortname": parent_shortname,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def merge_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Merge a license to another existing license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be merged

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            License merged successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"license/merge/{encode_path_param(shortname)}",
            method="PUT",
            json={
                "parentShortname": parent_shortname,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_suggested_license(
        self, *, reference_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSuggestedLicense]:
        """
        Get a single suggested license by the given reference text.

        Parameters
        ----------
        reference_text : typing.Optional[str]
            Reference text to get suggested license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSuggestedLicense]
            Request is successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            "license/suggest",
            method="POST",
            json={
                "referenceText": reference_text,
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
                    GetSuggestedLicense,
                    parse_obj_as(
                        type_=GetSuggestedLicense,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
