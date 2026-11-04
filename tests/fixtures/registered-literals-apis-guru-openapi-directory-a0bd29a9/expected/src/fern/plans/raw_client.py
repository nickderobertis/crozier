

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.delegate_identity import DelegateIdentity
from ..types.plan_resource import PlanResource
from ..types.plan_resource_headers import PlanResourceHeaders
from ..types.plan_resource_identity import PlanResourceIdentity
from ..types.plan_resource_properties import PlanResourceProperties
from ..types.rp_subscription_properties import RpSubscriptionProperties
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPlansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.Codespaces/plans/SubscriptionLifeCycleNotification",
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

    def post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.Codespaces/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    def put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.VSOnline/plans/SubscriptionLifeCycleNotification",
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

    def post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.VSOnline/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}",
            method="PUT",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/deleteAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/deleteAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/readAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/readAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/readDelegates",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceCreationCompleted",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceCreationValidate",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceDeletionValidate",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourcePatchCompleted",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourcePatchValidate",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceReadBegin",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/writeCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/writeDelegates",
            method="POST",
            json={
                "environmentIds": environment_ids,
                "expiration": expiration,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=DelegateIdentity, direction="write"
                ),
                "portNumbers": port_numbers,
                "scope": scope,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/writeEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}",
            method="PUT",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/deleteAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/deleteAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/readAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/readAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/readDelegates",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceCreationCompleted",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceCreationValidate",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceDeletionValidate",
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourcePatchCompleted",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourcePatchValidate",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceReadBegin",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/writeCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/writeDelegates",
            method="POST",
            json={
                "environmentIds": environment_ids,
                "expiration": expiration,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=DelegateIdentity, direction="write"
                ),
                "portNumbers": port_numbers,
                "scope": scope,
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

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/writeEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/deleteDelegates",
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

    def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/deleteDelegates",
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


class AsyncRawPlansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.Codespaces/plans/SubscriptionLifeCycleNotification",
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

    async def post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.Codespaces/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    async def put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.VSOnline/plans/SubscriptionLifeCycleNotification",
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

    async def post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.VSOnline/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    async def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}",
            method="PUT",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/deleteAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/deleteAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/readAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/readAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/readDelegates",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceCreationCompleted",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceCreationValidate",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceDeletionValidate",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourcePatchCompleted",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourcePatchValidate",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/resourceReadBegin",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/writeCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/writeDelegates",
            method="POST",
            json={
                "environmentIds": environment_ids,
                "expiration": expiration,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=DelegateIdentity, direction="write"
                ),
                "portNumbers": port_numbers,
                "scope": scope,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/writeEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/resourceReadBegin",
            method="POST",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[typing.Sequence[PlanResource]], direction="write"
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

    async def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}",
            method="PUT",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
                "provisioningState": provisioning_state,
                "tags": tags,
                "type": type,
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/deleteAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/deleteAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/readAllCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/readAllEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/readDelegates",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceCreationCompleted",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceCreationValidate",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceDeletionValidate",
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourcePatchCompleted",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
                ),
            },
            headers={
                "headers": str(headers) if headers is not None else None,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourcePatchValidate",
            method="POST",
            json={
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/resourceReadBegin",
            method="POST",
            json={
                "id": id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=PlanResourceIdentity, direction="write"
                ),
                "location": location,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=PlanResourceProperties, direction="write"
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/writeCodespaces",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/writeDelegates",
            method="POST",
            json={
                "environmentIds": environment_ids,
                "expiration": expiration,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=DelegateIdentity, direction="write"
                ),
                "portNumbers": port_numbers,
                "scope": scope,
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

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/writeEnvironments",
            method="POST",
            params={
                "expiration": serialize_datetime(expiration) if expiration is not None else None,
            },
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

    async def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/{encode_path_param(resource_group)}/providers/Microsoft.Codespaces/plans/{encode_path_param(resource_name)}/deleteDelegates",
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

    async def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/subscriptions/{encode_path_param(subscription_id)}/{encode_path_param(resource_group)}/providers/Microsoft.VSOnline/plans/{encode_path_param(resource_name)}/deleteDelegates",
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
