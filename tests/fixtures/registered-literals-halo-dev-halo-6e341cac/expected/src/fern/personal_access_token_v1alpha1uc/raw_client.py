

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
from ..types.metadata import Metadata
from ..types.pat_spec import PatSpec
from ..types.personal_access_token import PersonalAccessToken
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPersonalAccessTokenV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def obtain_pats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PersonalAccessToken]]:
        """
        Obtain PAT list.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PersonalAccessToken]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PersonalAccessToken],
                    parse_obj_as(
                        type_=typing.List[PersonalAccessToken],
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

    def generate_pat(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: typing.Optional[PatSpec] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PersonalAccessToken]:
        """
        Generate a PAT.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : typing.Optional[PatSpec]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PersonalAccessToken]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens",
            method="POST",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=PatSpec, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    def obtain_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PersonalAccessToken]:
        """
        Obtain a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PersonalAccessToken]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    def delete_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PersonalAccessToken]:
        """
        Delete a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PersonalAccessToken]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    def restore_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PersonalAccessToken]:
        """
        Restore a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to restore.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PersonalAccessToken]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}/actions/restoration",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    def revoke_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PersonalAccessToken]:
        """
        Revoke a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PersonalAccessToken]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}/actions/revocation",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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


class AsyncRawPersonalAccessTokenV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def obtain_pats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PersonalAccessToken]]:
        """
        Obtain PAT list.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PersonalAccessToken]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PersonalAccessToken],
                    parse_obj_as(
                        type_=typing.List[PersonalAccessToken],
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

    async def generate_pat(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: typing.Optional[PatSpec] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PersonalAccessToken]:
        """
        Generate a PAT.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : typing.Optional[PatSpec]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PersonalAccessToken]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens",
            method="POST",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=PatSpec, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    async def obtain_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PersonalAccessToken]:
        """
        Obtain a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PersonalAccessToken]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    async def delete_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PersonalAccessToken]:
        """
        Delete a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PersonalAccessToken]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    async def restore_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PersonalAccessToken]:
        """
        Restore a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to restore.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PersonalAccessToken]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}/actions/restoration",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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

    async def revoke_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PersonalAccessToken]:
        """
        Revoke a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PersonalAccessToken]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.security.halo.run/v1alpha1/personalaccesstokens/{encode_path_param(name)}/actions/revocation",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonalAccessToken,
                    parse_obj_as(
                        type_=PersonalAccessToken,
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
