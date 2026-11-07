

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.network_settings_resource import NetworkSettingsResource
from ..types.network_settings_resource_properties import NetworkSettingsResourceProperties
from ..types.rp_subscription_properties import RpSubscriptionProperties
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNetworkSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        properties: typing.Optional[RpSubscriptionProperties] = OMIT,
        registration_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        properties : typing.Optional[RpSubscriptionProperties]

        registration_date : typing.Optional[dt.datetime]

        state : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/GitHub.Network/{encode_path_param(resource_type)}/SubscriptionLifeCycleNotification",
            method="PUT",
            json={
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=RpSubscriptionProperties, direction="write"
                ),
                "registrationDate": registration_date,
                "state": state,
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

    def post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/GitHub.Network/{encode_path_param(resource_type)}/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value,
                    annotation=typing.Optional[typing.Sequence[NetworkSettingsResource]],
                    direction="write",
                ),
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value,
                    annotation=typing.Optional[typing.Sequence[NetworkSettingsResource]],
                    direction="write",
                ),
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

    def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}",
            method="PUT",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    def delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}",
            method="DELETE",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    def patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}",
            method="PATCH",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceCreationCompleted",
            method="POST",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceCreationValidate",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceDeletionCompleted",
            method="POST",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceDeletionValidate",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourcePatchCompleted",
            method="POST",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourcePatchValidate",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceReadBegin",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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


class AsyncRawNetworkSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        properties: typing.Optional[RpSubscriptionProperties] = OMIT,
        registration_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        properties : typing.Optional[RpSubscriptionProperties]

        registration_date : typing.Optional[dt.datetime]

        state : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/GitHub.Network/{encode_path_param(resource_type)}/SubscriptionLifeCycleNotification",
            method="PUT",
            json={
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=RpSubscriptionProperties, direction="write"
                ),
                "registrationDate": registration_date,
                "state": state,
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

    async def post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/GitHub.Network/{encode_path_param(resource_type)}/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value,
                    annotation=typing.Optional[typing.Sequence[NetworkSettingsResource]],
                    direction="write",
                ),
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value,
                    annotation=typing.Optional[typing.Sequence[NetworkSettingsResource]],
                    direction="write",
                ),
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

    async def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}",
            method="PUT",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    async def delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}",
            method="DELETE",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    async def patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}",
            method="PATCH",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceCreationCompleted",
            method="POST",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceCreationValidate",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceDeletionCompleted",
            method="POST",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceDeletionValidate",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourcePatchCompleted",
            method="POST",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourcePatchValidate",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/GitHub.Network/{encode_path_param(resource_type)}/{encode_path_param(resource_name)}/resourceReadBegin",
            method="POST",
            json={
                "id": id,
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=NetworkSettingsResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
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
