

import contextlib
import datetime as dt
import typing
from json.decoder import JSONDecodeError

from . import core
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.create_profile_request_role import CreateProfileRequestRole
from .types.mutation_nullable_response import MutationNullableResponse
from .types.mutation_pattern_payload_region import MutationPatternPayloadRegion
from .types.mutation_strict_object_payload_profile import MutationStrictObjectPayloadProfile
from .types.ok_response import OkResponse
from .types.prepare_upload_meta_request_content_type import PrepareUploadMetaRequestContentType
from .types.profile_response import ProfileResponse
from .types.ref_parameter_candidate_request_locale import RefParameterCandidateRequestLocale
from .types.search_profiles_response import SearchProfilesResponse
from .types.union_candidate_request import UnionCandidateRequest
from .types.update_preferences_request_theme import UpdatePreferencesRequestTheme
from .types.upload_meta_response import UploadMetaResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_profile(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProfileResponse]:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProfileResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/profiles",
            method="POST",
            json={
                "display_name": display_name,
                "email": email,
                "contact_phone": contact_phone,
                "homepage": homepage,
                "callback_url": callback_url,
                "birth_date": birth_date,
                "last_login_at": last_login_at,
                "avatar_base64": avatar_base64,
                "tenant_host": tenant_host,
                "source_ip": source_ip,
                "login_count": login_count,
                "tags": tags,
                "role": role,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileResponse,
                    parse_obj_as(
                        type_=ProfileResponse,
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

    def update_preferences(
        self,
        *,
        theme: UpdatePreferencesRequestTheme,
        timezone: str,
        daily_digest: typing.Optional[bool] = OMIT,
        weekly_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        theme : UpdatePreferencesRequestTheme

        timezone : str

        daily_digest : typing.Optional[bool]

        weekly_limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/preferences",
            method="POST",
            data={
                "theme": theme,
                "timezone": timezone,
                "daily_digest": daily_digest,
                "weekly_limit": weekly_limit,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def prepare_upload_meta(
        self,
        *,
        bucket: str,
        object_key: str,
        content_type: PrepareUploadMetaRequestContentType,
        size_bytes: int,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadMetaResponse]:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        content_type : PrepareUploadMetaRequestContentType

        size_bytes : int

        checksum : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadMetaResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/uploads/meta",
            method="POST",
            data={
                "bucket": bucket,
                "object_key": object_key,
                "checksum": checksum,
                "content_type": content_type,
                "size_bytes": size_bytes,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadMetaResponse,
                    parse_obj_as(
                        type_=UploadMetaResponse,
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

    def search_profiles(
        self,
        *,
        keyword: str,
        request_id: str,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchProfilesResponse]:
        """


        Parameters
        ----------
        keyword : str


        request_id : str


        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        page_size : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchProfilesResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/search",
            method="GET",
            params={
                "keyword": keyword,
                "tags": tags,
                "page_size": page_size,
            },
            headers={
                "X-Request-Id": str(request_id) if request_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchProfilesResponse,
                    parse_obj_as(
                        type_=SearchProfilesResponse,
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

    def validate_raw_json(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/raw-json",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def pattern_candidate(
        self,
        *,
        phone: str,
        region: MutationPatternPayloadRegion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        phone : str

        region : MutationPatternPayloadRegion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/pattern",
            method="POST",
            json={
                "phone": phone,
                "region": region,
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
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def multiple_of_candidate(
        self, *, price: float, quantity: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        price : float

        quantity : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/multiple-of",
            method="POST",
            json={
                "price": price,
                "quantity": quantity,
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
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def strict_object_candidate(
        self, *, profile: MutationStrictObjectPayloadProfile, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        profile : MutationStrictObjectPayloadProfile

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/strict-object",
            method="POST",
            json={
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=MutationStrictObjectPayloadProfile, direction="write"
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
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def nullable_any_of_candidate(
        self, *, nickname: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MutationNullableResponse]:
        """


        Parameters
        ----------
        nickname : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MutationNullableResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/nullable-anyof",
            method="POST",
            json={
                "nickname": nickname,
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
                    MutationNullableResponse,
                    parse_obj_as(
                        type_=MutationNullableResponse,
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

    def union_candidate(
        self, *, request: UnionCandidateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        request : UnionCandidateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/union-contact",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UnionCandidateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def query_object_candidate(
        self,
        *,
        filter_keyword: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        filter_keyword : typing.Optional[str]


        limit : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/query-object",
            method="GET",
            params={
                "filter_keyword": filter_keyword,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def query_array_candidate(
        self,
        *,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/query-array",
            method="GET",
            params={
                "tags": tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def upload_file_candidate(
        self,
        *,
        bucket: str,
        object_key: str,
        checksum: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        checksum : typing.Optional[str]

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/upload-file",
            method="POST",
            data={
                "bucket": bucket,
                "object_key": object_key,
                "checksum": checksum,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def ref_request_body_candidate(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/ref-request-body",
            method="POST",
            json={
                "display_name": display_name,
                "email": email,
                "contact_phone": contact_phone,
                "homepage": homepage,
                "callback_url": callback_url,
                "birth_date": birth_date,
                "last_login_at": last_login_at,
                "avatar_base64": avatar_base64,
                "tenant_host": tenant_host,
                "source_ip": source_ip,
                "login_count": login_count,
                "tags": tags,
                "role": role,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def ref_parameter_candidate(
        self,
        item_id: str,
        *,
        locale: typing.Optional[RefParameterCandidateRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        item_id : str


        locale : typing.Optional[RefParameterCandidateRequestLocale]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/lab/mutation/ref-parameter/{encode_path_param(item_id)}",
            method="GET",
            params={
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    def multi2xx_candidate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OkResponse]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/multi-2xx",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    @contextlib.contextmanager
    def non_json_success_candidate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            ok
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/lab/mutation/non-json-success",
            method="GET",
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_profile(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProfileResponse]:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProfileResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/profiles",
            method="POST",
            json={
                "display_name": display_name,
                "email": email,
                "contact_phone": contact_phone,
                "homepage": homepage,
                "callback_url": callback_url,
                "birth_date": birth_date,
                "last_login_at": last_login_at,
                "avatar_base64": avatar_base64,
                "tenant_host": tenant_host,
                "source_ip": source_ip,
                "login_count": login_count,
                "tags": tags,
                "role": role,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileResponse,
                    parse_obj_as(
                        type_=ProfileResponse,
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

    async def update_preferences(
        self,
        *,
        theme: UpdatePreferencesRequestTheme,
        timezone: str,
        daily_digest: typing.Optional[bool] = OMIT,
        weekly_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        theme : UpdatePreferencesRequestTheme

        timezone : str

        daily_digest : typing.Optional[bool]

        weekly_limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/preferences",
            method="POST",
            data={
                "theme": theme,
                "timezone": timezone,
                "daily_digest": daily_digest,
                "weekly_limit": weekly_limit,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def prepare_upload_meta(
        self,
        *,
        bucket: str,
        object_key: str,
        content_type: PrepareUploadMetaRequestContentType,
        size_bytes: int,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadMetaResponse]:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        content_type : PrepareUploadMetaRequestContentType

        size_bytes : int

        checksum : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadMetaResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/uploads/meta",
            method="POST",
            data={
                "bucket": bucket,
                "object_key": object_key,
                "checksum": checksum,
                "content_type": content_type,
                "size_bytes": size_bytes,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadMetaResponse,
                    parse_obj_as(
                        type_=UploadMetaResponse,
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

    async def search_profiles(
        self,
        *,
        keyword: str,
        request_id: str,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchProfilesResponse]:
        """


        Parameters
        ----------
        keyword : str


        request_id : str


        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        page_size : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchProfilesResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/search",
            method="GET",
            params={
                "keyword": keyword,
                "tags": tags,
                "page_size": page_size,
            },
            headers={
                "X-Request-Id": str(request_id) if request_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchProfilesResponse,
                    parse_obj_as(
                        type_=SearchProfilesResponse,
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

    async def validate_raw_json(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/raw-json",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def pattern_candidate(
        self,
        *,
        phone: str,
        region: MutationPatternPayloadRegion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        phone : str

        region : MutationPatternPayloadRegion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/pattern",
            method="POST",
            json={
                "phone": phone,
                "region": region,
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
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def multiple_of_candidate(
        self, *, price: float, quantity: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        price : float

        quantity : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/multiple-of",
            method="POST",
            json={
                "price": price,
                "quantity": quantity,
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
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def strict_object_candidate(
        self, *, profile: MutationStrictObjectPayloadProfile, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        profile : MutationStrictObjectPayloadProfile

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/strict-object",
            method="POST",
            json={
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=MutationStrictObjectPayloadProfile, direction="write"
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
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def nullable_any_of_candidate(
        self, *, nickname: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MutationNullableResponse]:
        """


        Parameters
        ----------
        nickname : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MutationNullableResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/nullable-anyof",
            method="POST",
            json={
                "nickname": nickname,
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
                    MutationNullableResponse,
                    parse_obj_as(
                        type_=MutationNullableResponse,
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

    async def union_candidate(
        self, *, request: UnionCandidateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        request : UnionCandidateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/union-contact",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UnionCandidateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def query_object_candidate(
        self,
        *,
        filter_keyword: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        filter_keyword : typing.Optional[str]


        limit : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/query-object",
            method="GET",
            params={
                "filter_keyword": filter_keyword,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def query_array_candidate(
        self,
        *,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/query-array",
            method="GET",
            params={
                "tags": tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def upload_file_candidate(
        self,
        *,
        bucket: str,
        object_key: str,
        checksum: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        bucket : str

        object_key : str

        checksum : typing.Optional[str]

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/upload-file",
            method="POST",
            data={
                "bucket": bucket,
                "object_key": object_key,
                "checksum": checksum,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def ref_request_body_candidate(
        self,
        *,
        display_name: str,
        email: str,
        contact_phone: str,
        tags: typing.Sequence[str],
        role: CreateProfileRequestRole,
        homepage: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        last_login_at: typing.Optional[dt.datetime] = OMIT,
        avatar_base64: typing.Optional[str] = OMIT,
        tenant_host: typing.Optional[str] = OMIT,
        source_ip: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        display_name : str

        email : str

        contact_phone : str

        tags : typing.Sequence[str]

        role : CreateProfileRequestRole

        homepage : typing.Optional[str]

        callback_url : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        last_login_at : typing.Optional[dt.datetime]

        avatar_base64 : typing.Optional[str]

        tenant_host : typing.Optional[str]

        source_ip : typing.Optional[str]

        login_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/ref-request-body",
            method="POST",
            json={
                "display_name": display_name,
                "email": email,
                "contact_phone": contact_phone,
                "homepage": homepage,
                "callback_url": callback_url,
                "birth_date": birth_date,
                "last_login_at": last_login_at,
                "avatar_base64": avatar_base64,
                "tenant_host": tenant_host,
                "source_ip": source_ip,
                "login_count": login_count,
                "tags": tags,
                "role": role,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def ref_parameter_candidate(
        self,
        item_id: str,
        *,
        locale: typing.Optional[RefParameterCandidateRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        item_id : str


        locale : typing.Optional[RefParameterCandidateRequestLocale]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/lab/mutation/ref-parameter/{encode_path_param(item_id)}",
            method="GET",
            params={
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    async def multi2xx_candidate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OkResponse]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/lab/mutation/multi-2xx",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
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

    @contextlib.asynccontextmanager
    async def non_json_success_candidate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            ok
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/lab/mutation/non-json-success",
            method="GET",
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
