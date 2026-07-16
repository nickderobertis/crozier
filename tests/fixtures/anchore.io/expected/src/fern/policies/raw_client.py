

import datetime as dt
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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.image_selection_rule import ImageSelectionRule
from ..types.mapping_rule import MappingRule
from ..types.policy import Policy
from ..types.policy_bundle import PolicyBundle
from ..types.policy_bundle_list import PolicyBundleList
from ..types.policy_bundle_record import PolicyBundleRecord
from ..types.whitelist import Whitelist
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPoliciesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_policies(
        self,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PolicyBundleList]:
        """
        List all saved policy bundles

        Parameters
        ----------
        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PolicyBundleList]
            Policy listing
        """
        _response = self._client_wrapper.httpx_client.request(
            "policies",
            method="GET",
            params={
                "detail": detail,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleList,
                    parse_obj_as(
                        type_=PolicyBundleList,
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

    def add_policy(
        self,
        *,
        id: str,
        mappings: typing.Sequence[MappingRule],
        policies: typing.Sequence[Policy],
        version: str,
        anchore_account: typing.Optional[str] = None,
        blacklisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        whitelisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        whitelists: typing.Optional[typing.Sequence[Whitelist]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PolicyBundleRecord]:
        """
        Adds a new policy bundle to the system

        Parameters
        ----------
        id : str
            Id of the bundle

        mappings : typing.Sequence[MappingRule]
            Mapping rules for defining which policy and whitelist(s) to apply to an image based on a match of the image tag or id. Evaluated in order.

        policies : typing.Sequence[Policy]
            Policies which define the go/stop/warn status of an image using rule matches on image properties

        version : str
            Version id for this bundle format

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        blacklisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always result in a STOP/FAIL policy result regardless of policy content or presence in whitelisted_images

        comment : typing.Optional[str]
            Description of the bundle, human readable

        name : typing.Optional[str]
            Human readable name for the bundle

        whitelisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always be passed (unless also on the blacklist), regardless of policy result.

        whitelists : typing.Optional[typing.Sequence[Whitelist]]
            Whitelists which define which policy matches to disregard explicitly in the final policy decision

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PolicyBundleRecord]
            Saved bundle
        """
        _response = self._client_wrapper.httpx_client.request(
            "policies",
            method="POST",
            json={
                "blacklisted_images": convert_and_respect_annotation_metadata(
                    object_=blacklisted_images, annotation=typing.Sequence[ImageSelectionRule], direction="write"
                ),
                "comment": comment,
                "id": id,
                "mappings": convert_and_respect_annotation_metadata(
                    object_=mappings, annotation=typing.Sequence[MappingRule], direction="write"
                ),
                "name": name,
                "policies": convert_and_respect_annotation_metadata(
                    object_=policies, annotation=typing.Sequence[Policy], direction="write"
                ),
                "version": version,
                "whitelisted_images": convert_and_respect_annotation_metadata(
                    object_=whitelisted_images, annotation=typing.Sequence[ImageSelectionRule], direction="write"
                ),
                "whitelists": convert_and_respect_annotation_metadata(
                    object_=whitelists, annotation=typing.Sequence[Whitelist], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleRecord,
                    parse_obj_as(
                        type_=PolicyBundleRecord,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_policy(
        self,
        policy_id: str,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PolicyBundleList]:
        """
        Get the policy bundle content

        Parameters
        ----------
        policy_id : str

        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PolicyBundleList]
            A list with a single fetched policy bundle record
        """
        _response = self._client_wrapper.httpx_client.request(
            f"policies/{encode_path_param(policy_id)}",
            method="GET",
            params={
                "detail": detail,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleList,
                    parse_obj_as(
                        type_=PolicyBundleList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def update_policy(
        self,
        policy_id_: str,
        *,
        active: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        policy_bundle_record_active: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        policy_source: typing.Optional[str] = OMIT,
        policybundle: typing.Optional[PolicyBundle] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PolicyBundleList]:
        """
        Update/replace and existing policy

        Parameters
        ----------
        policy_id_ : str

        active : typing.Optional[bool]
            Mark policy as active

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        policy_bundle_record_active : typing.Optional[bool]
            True if the bundle is currently defined to be used automatically

        created_at : typing.Optional[dt.datetime]

        last_updated : typing.Optional[dt.datetime]

        policy_id : typing.Optional[str]
            The bundle's identifier

        policy_source : typing.Optional[str]
            Source location of where the policy bundle originated

        policybundle : typing.Optional[PolicyBundle]

        user_id : typing.Optional[str]
            UserId of the user that owns the bundle

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PolicyBundleList]
            A list with a single updated policy bundle record
        """
        _response = self._client_wrapper.httpx_client.request(
            f"policies/{encode_path_param(policy_id_)}",
            method="PUT",
            params={
                "active": active,
            },
            json={
                "active": active,
                "created_at": created_at,
                "last_updated": last_updated,
                "policyId": policy_id,
                "policy_source": policy_source,
                "policybundle": convert_and_respect_annotation_metadata(
                    object_=policybundle, annotation=PolicyBundle, direction="write"
                ),
                "userId": user_id,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleList,
                    parse_obj_as(
                        type_=PolicyBundleList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_policy(
        self,
        policy_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete the specified policy

        Parameters
        ----------
        policy_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"policies/{encode_path_param(policy_id)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
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
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawPoliciesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_policies(
        self,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PolicyBundleList]:
        """
        List all saved policy bundles

        Parameters
        ----------
        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PolicyBundleList]
            Policy listing
        """
        _response = await self._client_wrapper.httpx_client.request(
            "policies",
            method="GET",
            params={
                "detail": detail,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleList,
                    parse_obj_as(
                        type_=PolicyBundleList,
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

    async def add_policy(
        self,
        *,
        id: str,
        mappings: typing.Sequence[MappingRule],
        policies: typing.Sequence[Policy],
        version: str,
        anchore_account: typing.Optional[str] = None,
        blacklisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        whitelisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        whitelists: typing.Optional[typing.Sequence[Whitelist]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PolicyBundleRecord]:
        """
        Adds a new policy bundle to the system

        Parameters
        ----------
        id : str
            Id of the bundle

        mappings : typing.Sequence[MappingRule]
            Mapping rules for defining which policy and whitelist(s) to apply to an image based on a match of the image tag or id. Evaluated in order.

        policies : typing.Sequence[Policy]
            Policies which define the go/stop/warn status of an image using rule matches on image properties

        version : str
            Version id for this bundle format

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        blacklisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always result in a STOP/FAIL policy result regardless of policy content or presence in whitelisted_images

        comment : typing.Optional[str]
            Description of the bundle, human readable

        name : typing.Optional[str]
            Human readable name for the bundle

        whitelisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always be passed (unless also on the blacklist), regardless of policy result.

        whitelists : typing.Optional[typing.Sequence[Whitelist]]
            Whitelists which define which policy matches to disregard explicitly in the final policy decision

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PolicyBundleRecord]
            Saved bundle
        """
        _response = await self._client_wrapper.httpx_client.request(
            "policies",
            method="POST",
            json={
                "blacklisted_images": convert_and_respect_annotation_metadata(
                    object_=blacklisted_images, annotation=typing.Sequence[ImageSelectionRule], direction="write"
                ),
                "comment": comment,
                "id": id,
                "mappings": convert_and_respect_annotation_metadata(
                    object_=mappings, annotation=typing.Sequence[MappingRule], direction="write"
                ),
                "name": name,
                "policies": convert_and_respect_annotation_metadata(
                    object_=policies, annotation=typing.Sequence[Policy], direction="write"
                ),
                "version": version,
                "whitelisted_images": convert_and_respect_annotation_metadata(
                    object_=whitelisted_images, annotation=typing.Sequence[ImageSelectionRule], direction="write"
                ),
                "whitelists": convert_and_respect_annotation_metadata(
                    object_=whitelists, annotation=typing.Sequence[Whitelist], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleRecord,
                    parse_obj_as(
                        type_=PolicyBundleRecord,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_policy(
        self,
        policy_id: str,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PolicyBundleList]:
        """
        Get the policy bundle content

        Parameters
        ----------
        policy_id : str

        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PolicyBundleList]
            A list with a single fetched policy bundle record
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"policies/{encode_path_param(policy_id)}",
            method="GET",
            params={
                "detail": detail,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleList,
                    parse_obj_as(
                        type_=PolicyBundleList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def update_policy(
        self,
        policy_id_: str,
        *,
        active: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        policy_bundle_record_active: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        policy_source: typing.Optional[str] = OMIT,
        policybundle: typing.Optional[PolicyBundle] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PolicyBundleList]:
        """
        Update/replace and existing policy

        Parameters
        ----------
        policy_id_ : str

        active : typing.Optional[bool]
            Mark policy as active

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        policy_bundle_record_active : typing.Optional[bool]
            True if the bundle is currently defined to be used automatically

        created_at : typing.Optional[dt.datetime]

        last_updated : typing.Optional[dt.datetime]

        policy_id : typing.Optional[str]
            The bundle's identifier

        policy_source : typing.Optional[str]
            Source location of where the policy bundle originated

        policybundle : typing.Optional[PolicyBundle]

        user_id : typing.Optional[str]
            UserId of the user that owns the bundle

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PolicyBundleList]
            A list with a single updated policy bundle record
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"policies/{encode_path_param(policy_id_)}",
            method="PUT",
            params={
                "active": active,
            },
            json={
                "active": active,
                "created_at": created_at,
                "last_updated": last_updated,
                "policyId": policy_id,
                "policy_source": policy_source,
                "policybundle": convert_and_respect_annotation_metadata(
                    object_=policybundle, annotation=PolicyBundle, direction="write"
                ),
                "userId": user_id,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyBundleList,
                    parse_obj_as(
                        type_=PolicyBundleList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_policy(
        self,
        policy_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete the specified policy

        Parameters
        ----------
        policy_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"policies/{encode_path_param(policy_id)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
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
            if _response.status_code == 500:
                raise InternalServerError(
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
