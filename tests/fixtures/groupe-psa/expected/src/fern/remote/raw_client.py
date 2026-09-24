

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.callback_ref import CallbackRef
from ..types.callback_subscribe_batch_notify import CallbackSubscribeBatchNotify
from ..types.index_range import IndexRange
from ..types.remote_action import RemoteAction
from ..types.remote_actions import RemoteActions
from ..types.remote_callback import RemoteCallback
from ..types.remote_callback_subscribe_callback import RemoteCallbackSubscribeCallback
from ..types.remote_callback_subscribe_retry_policy import RemoteCallbackSubscribeRetryPolicy
from ..types.remote_callbacks import RemoteCallbacks
from ..types.remote_charging import RemoteCharging
from ..types.remote_doors_state import RemoteDoorsState
from ..types.remote_horn import RemoteHorn
from ..types.remote_lights import RemoteLights
from ..types.remote_navigation import RemoteNavigation
from ..types.remote_post_response import RemotePostResponse
from ..types.remote_preconditioning import RemotePreconditioning
from ..types.remote_set_immobilization import RemoteSetImmobilization
from ..types.remote_stolen import RemoteStolen
from ..types.remote_type import RemoteType
from ..types.remote_types import RemoteTypes
from ..types.remote_wake_up import RemoteWakeUp
from .types.remote_callbacks_status_setter_status import RemoteCallbacksStatusSetterStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRemoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_fleet_remotes(
        self,
        fid: str,
        *,
        types: typing.Optional[typing.Union[RemoteType, typing.Sequence[RemoteType]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RemoteCallbacks]:
        """
        Returns the list of subscribed remote callback of the fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        types : typing.Optional[typing.Union[RemoteType, typing.Sequence[RemoteType]]]
            Results will contain only the Remote-Callbacks of these types. _If not specified then the whole callbacks are retrieved_.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoteCallbacks]
            A list of subsribed remote callback.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks",
            method="GET",
            params={
                "types": types,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteCallbacks,
                    parse_obj_as(
                        type_=RemoteCallbacks,
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

    def set_fleet_vehicle_remote(
        self,
        fid: str,
        *,
        remote_types: RemoteTypes,
        label: typing.Optional[str] = OMIT,
        retry_policy: typing.Optional[RemoteCallbackSubscribeRetryPolicy] = OMIT,
        callback: typing.Optional[RemoteCallbackSubscribeCallback] = OMIT,
        batch_notify: typing.Optional[CallbackSubscribeBatchNotify] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CallbackRef]:
        """
        Create a new reusable callback.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        remote_types : RemoteTypes

        label : typing.Optional[str]

        retry_policy : typing.Optional[RemoteCallbackSubscribeRetryPolicy]
            The retry policy to apply when notification failed.

        callback : typing.Optional[RemoteCallbackSubscribeCallback]

        batch_notify : typing.Optional[CallbackSubscribeBatchNotify]

            Notification batch of events defined by a time window and batch size. If this field is not set, the callback will post only one event by call.

              * **At least, the ```size``` parameter should be provided.**
              * **If the time window is not set then the default value will be applied.**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CallbackRef]
            Remote callback creation or update success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks",
            method="POST",
            json={
                "label": label,
                "retryPolicy": convert_and_respect_annotation_metadata(
                    object_=retry_policy, annotation=RemoteCallbackSubscribeRetryPolicy, direction="write"
                ),
                "callback": convert_and_respect_annotation_metadata(
                    object_=callback, annotation=RemoteCallbackSubscribeCallback, direction="write"
                ),
                "remoteTypes": remote_types,
                "batchNotify": convert_and_respect_annotation_metadata(
                    object_=batch_notify, annotation=CallbackSubscribeBatchNotify, direction="write"
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
                    CallbackRef,
                    parse_obj_as(
                        type_=CallbackRef,
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

    def get_fleet_remoteby_id(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RemoteCallback]:
        """
        Returns a subscribed remote callback of the fleet by subscribe ID.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoteCallback]
            A remote callback.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteCallback,
                    parse_obj_as(
                        type_=RemoteCallback,
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

    def set_fleet_vehicle_remote_by_id(
        self,
        fid: str,
        cbid: str,
        *,
        remote_types: RemoteTypes,
        label: typing.Optional[str] = OMIT,
        retry_policy: typing.Optional[RemoteCallbackSubscribeRetryPolicy] = OMIT,
        callback: typing.Optional[RemoteCallbackSubscribeCallback] = OMIT,
        batch_notify: typing.Optional[CallbackSubscribeBatchNotify] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CallbackRef]:
        """

        Update an existing ```Callback``` that has been posted (and accepted previously) for this fleet. The callback object (body) provided should be complete (aggregation is not supported for the update). This object can be retrieved  using the ```GET /fleets/{fid}/remote/callbacks/{cbid}``` API then modify it and finally publish it (via this ```PUT API```)

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        remote_types : RemoteTypes

        label : typing.Optional[str]

        retry_policy : typing.Optional[RemoteCallbackSubscribeRetryPolicy]
            The retry policy to apply when notification failed.

        callback : typing.Optional[RemoteCallbackSubscribeCallback]

        batch_notify : typing.Optional[CallbackSubscribeBatchNotify]

            Notification batch of events defined by a time window and batch size. If this field is not set, the callback will post only one event by call.

              * **At least, the ```size``` parameter should be provided.**
              * **If the time window is not set then the default value will be applied.**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CallbackRef]
            Remote callback creation or update success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}",
            method="PUT",
            json={
                "label": label,
                "retryPolicy": convert_and_respect_annotation_metadata(
                    object_=retry_policy, annotation=RemoteCallbackSubscribeRetryPolicy, direction="write"
                ),
                "callback": convert_and_respect_annotation_metadata(
                    object_=callback, annotation=RemoteCallbackSubscribeCallback, direction="write"
                ),
                "remoteTypes": remote_types,
                "batchNotify": convert_and_respect_annotation_metadata(
                    object_=batch_notify, annotation=CallbackSubscribeBatchNotify, direction="write"
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
                    CallbackRef,
                    parse_obj_as(
                        type_=CallbackRef,
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

    def delete_fleet_remote(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Remove an existing callback if and only if there is no pending remote attached to it.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_flee_remote_callback_status(
        self,
        fid: str,
        cbid: str,
        *,
        status: RemoteCallbacksStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CallbackRef]:
        """
        Set the remote callback status.```Paused``` means that the callback will not post any event.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        status : RemoteCallbacksStatusSetterStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CallbackRef]
            Remote callback creation or update success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}/status",
            method="PUT",
            json={
                "status": status,
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
                    CallbackRef,
                    parse_obj_as(
                        type_=CallbackRef,
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

    def get_remote_requests_for_vhl(
        self,
        fid: str,
        vid: str,
        cbid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RemoteActions]:
        """
        Returns the list of action remote requested for vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cbid : str
            The remote callback ID.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoteActions]
            A list of remote actions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/vehicles/{encode_path_param(vid)}/callbacks/{encode_path_param(cbid)}/remotes",
            method="GET",
            params={
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteActions,
                    parse_obj_as(
                        type_=RemoteActions,
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

    def send_remote_to_vhl(
        self,
        fid: str,
        vid: str,
        cbid: str,
        *,
        label: typing.Optional[str] = OMIT,
        preconditioning: typing.Optional[RemotePreconditioning] = OMIT,
        immobilization: typing.Optional[RemoteSetImmobilization] = OMIT,
        door: typing.Optional[RemoteDoorsState] = OMIT,
        horn: typing.Optional[RemoteHorn] = OMIT,
        charging: typing.Optional[RemoteCharging] = OMIT,
        stolen: typing.Optional[RemoteStolen] = OMIT,
        lights: typing.Optional[RemoteLights] = OMIT,
        wake_up: typing.Optional[RemoteWakeUp] = OMIT,
        navigation: typing.Optional[RemoteNavigation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RemotePostResponse]:
        """
        Create a new asynchrone vehicle remote action and request it.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cbid : str
            The remote callback ID.

        label : typing.Optional[str]

        preconditioning : typing.Optional[RemotePreconditioning]

        immobilization : typing.Optional[RemoteSetImmobilization]

        door : typing.Optional[RemoteDoorsState]

        horn : typing.Optional[RemoteHorn]

        charging : typing.Optional[RemoteCharging]

        stolen : typing.Optional[RemoteStolen]

        lights : typing.Optional[RemoteLights]

        wake_up : typing.Optional[RemoteWakeUp]

        navigation : typing.Optional[RemoteNavigation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemotePostResponse]
            Remote action creation success response (accepted).
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/vehicles/{encode_path_param(vid)}/callbacks/{encode_path_param(cbid)}/remotes",
            method="POST",
            json={
                "label": label,
                "preconditioning": convert_and_respect_annotation_metadata(
                    object_=preconditioning, annotation=RemotePreconditioning, direction="write"
                ),
                "immobilization": convert_and_respect_annotation_metadata(
                    object_=immobilization, annotation=RemoteSetImmobilization, direction="write"
                ),
                "door": convert_and_respect_annotation_metadata(
                    object_=door, annotation=RemoteDoorsState, direction="write"
                ),
                "horn": convert_and_respect_annotation_metadata(object_=horn, annotation=RemoteHorn, direction="write"),
                "charging": convert_and_respect_annotation_metadata(
                    object_=charging, annotation=RemoteCharging, direction="write"
                ),
                "stolen": convert_and_respect_annotation_metadata(
                    object_=stolen, annotation=RemoteStolen, direction="write"
                ),
                "lights": convert_and_respect_annotation_metadata(
                    object_=lights, annotation=RemoteLights, direction="write"
                ),
                "wakeUp": convert_and_respect_annotation_metadata(
                    object_=wake_up, annotation=RemoteWakeUp, direction="write"
                ),
                "navigation": convert_and_respect_annotation_metadata(
                    object_=navigation, annotation=RemoteNavigation, direction="write"
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
                    RemotePostResponse,
                    parse_obj_as(
                        type_=RemotePostResponse,
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

    def get_remote_request_for_vhl_by_id(
        self, fid: str, vid: str, cbid: str, rid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RemoteAction]:
        """
        Returns the remote action requested for vehicle by ID.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cbid : str
            The remote callback ID.

        rid : str
            The remote action ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoteAction]
            A remote action response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/vehicles/{encode_path_param(vid)}/callbacks/{encode_path_param(cbid)}/remotes/{encode_path_param(rid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteAction,
                    parse_obj_as(
                        type_=RemoteAction,
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


class AsyncRawRemoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_fleet_remotes(
        self,
        fid: str,
        *,
        types: typing.Optional[typing.Union[RemoteType, typing.Sequence[RemoteType]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RemoteCallbacks]:
        """
        Returns the list of subscribed remote callback of the fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        types : typing.Optional[typing.Union[RemoteType, typing.Sequence[RemoteType]]]
            Results will contain only the Remote-Callbacks of these types. _If not specified then the whole callbacks are retrieved_.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoteCallbacks]
            A list of subsribed remote callback.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks",
            method="GET",
            params={
                "types": types,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteCallbacks,
                    parse_obj_as(
                        type_=RemoteCallbacks,
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

    async def set_fleet_vehicle_remote(
        self,
        fid: str,
        *,
        remote_types: RemoteTypes,
        label: typing.Optional[str] = OMIT,
        retry_policy: typing.Optional[RemoteCallbackSubscribeRetryPolicy] = OMIT,
        callback: typing.Optional[RemoteCallbackSubscribeCallback] = OMIT,
        batch_notify: typing.Optional[CallbackSubscribeBatchNotify] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CallbackRef]:
        """
        Create a new reusable callback.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        remote_types : RemoteTypes

        label : typing.Optional[str]

        retry_policy : typing.Optional[RemoteCallbackSubscribeRetryPolicy]
            The retry policy to apply when notification failed.

        callback : typing.Optional[RemoteCallbackSubscribeCallback]

        batch_notify : typing.Optional[CallbackSubscribeBatchNotify]

            Notification batch of events defined by a time window and batch size. If this field is not set, the callback will post only one event by call.

              * **At least, the ```size``` parameter should be provided.**
              * **If the time window is not set then the default value will be applied.**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CallbackRef]
            Remote callback creation or update success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks",
            method="POST",
            json={
                "label": label,
                "retryPolicy": convert_and_respect_annotation_metadata(
                    object_=retry_policy, annotation=RemoteCallbackSubscribeRetryPolicy, direction="write"
                ),
                "callback": convert_and_respect_annotation_metadata(
                    object_=callback, annotation=RemoteCallbackSubscribeCallback, direction="write"
                ),
                "remoteTypes": remote_types,
                "batchNotify": convert_and_respect_annotation_metadata(
                    object_=batch_notify, annotation=CallbackSubscribeBatchNotify, direction="write"
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
                    CallbackRef,
                    parse_obj_as(
                        type_=CallbackRef,
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

    async def get_fleet_remoteby_id(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RemoteCallback]:
        """
        Returns a subscribed remote callback of the fleet by subscribe ID.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoteCallback]
            A remote callback.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteCallback,
                    parse_obj_as(
                        type_=RemoteCallback,
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

    async def set_fleet_vehicle_remote_by_id(
        self,
        fid: str,
        cbid: str,
        *,
        remote_types: RemoteTypes,
        label: typing.Optional[str] = OMIT,
        retry_policy: typing.Optional[RemoteCallbackSubscribeRetryPolicy] = OMIT,
        callback: typing.Optional[RemoteCallbackSubscribeCallback] = OMIT,
        batch_notify: typing.Optional[CallbackSubscribeBatchNotify] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CallbackRef]:
        """

        Update an existing ```Callback``` that has been posted (and accepted previously) for this fleet. The callback object (body) provided should be complete (aggregation is not supported for the update). This object can be retrieved  using the ```GET /fleets/{fid}/remote/callbacks/{cbid}``` API then modify it and finally publish it (via this ```PUT API```)

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        remote_types : RemoteTypes

        label : typing.Optional[str]

        retry_policy : typing.Optional[RemoteCallbackSubscribeRetryPolicy]
            The retry policy to apply when notification failed.

        callback : typing.Optional[RemoteCallbackSubscribeCallback]

        batch_notify : typing.Optional[CallbackSubscribeBatchNotify]

            Notification batch of events defined by a time window and batch size. If this field is not set, the callback will post only one event by call.

              * **At least, the ```size``` parameter should be provided.**
              * **If the time window is not set then the default value will be applied.**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CallbackRef]
            Remote callback creation or update success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}",
            method="PUT",
            json={
                "label": label,
                "retryPolicy": convert_and_respect_annotation_metadata(
                    object_=retry_policy, annotation=RemoteCallbackSubscribeRetryPolicy, direction="write"
                ),
                "callback": convert_and_respect_annotation_metadata(
                    object_=callback, annotation=RemoteCallbackSubscribeCallback, direction="write"
                ),
                "remoteTypes": remote_types,
                "batchNotify": convert_and_respect_annotation_metadata(
                    object_=batch_notify, annotation=CallbackSubscribeBatchNotify, direction="write"
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
                    CallbackRef,
                    parse_obj_as(
                        type_=CallbackRef,
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

    async def delete_fleet_remote(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Remove an existing callback if and only if there is no pending remote attached to it.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_flee_remote_callback_status(
        self,
        fid: str,
        cbid: str,
        *,
        status: RemoteCallbacksStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CallbackRef]:
        """
        Set the remote callback status.```Paused``` means that the callback will not post any event.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        cbid : str
            The remote callback ID.

        status : RemoteCallbacksStatusSetterStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CallbackRef]
            Remote callback creation or update success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/remote/callbacks/{encode_path_param(cbid)}/status",
            method="PUT",
            json={
                "status": status,
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
                    CallbackRef,
                    parse_obj_as(
                        type_=CallbackRef,
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

    async def get_remote_requests_for_vhl(
        self,
        fid: str,
        vid: str,
        cbid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RemoteActions]:
        """
        Returns the list of action remote requested for vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cbid : str
            The remote callback ID.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoteActions]
            A list of remote actions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/vehicles/{encode_path_param(vid)}/callbacks/{encode_path_param(cbid)}/remotes",
            method="GET",
            params={
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteActions,
                    parse_obj_as(
                        type_=RemoteActions,
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

    async def send_remote_to_vhl(
        self,
        fid: str,
        vid: str,
        cbid: str,
        *,
        label: typing.Optional[str] = OMIT,
        preconditioning: typing.Optional[RemotePreconditioning] = OMIT,
        immobilization: typing.Optional[RemoteSetImmobilization] = OMIT,
        door: typing.Optional[RemoteDoorsState] = OMIT,
        horn: typing.Optional[RemoteHorn] = OMIT,
        charging: typing.Optional[RemoteCharging] = OMIT,
        stolen: typing.Optional[RemoteStolen] = OMIT,
        lights: typing.Optional[RemoteLights] = OMIT,
        wake_up: typing.Optional[RemoteWakeUp] = OMIT,
        navigation: typing.Optional[RemoteNavigation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RemotePostResponse]:
        """
        Create a new asynchrone vehicle remote action and request it.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cbid : str
            The remote callback ID.

        label : typing.Optional[str]

        preconditioning : typing.Optional[RemotePreconditioning]

        immobilization : typing.Optional[RemoteSetImmobilization]

        door : typing.Optional[RemoteDoorsState]

        horn : typing.Optional[RemoteHorn]

        charging : typing.Optional[RemoteCharging]

        stolen : typing.Optional[RemoteStolen]

        lights : typing.Optional[RemoteLights]

        wake_up : typing.Optional[RemoteWakeUp]

        navigation : typing.Optional[RemoteNavigation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemotePostResponse]
            Remote action creation success response (accepted).
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/vehicles/{encode_path_param(vid)}/callbacks/{encode_path_param(cbid)}/remotes",
            method="POST",
            json={
                "label": label,
                "preconditioning": convert_and_respect_annotation_metadata(
                    object_=preconditioning, annotation=RemotePreconditioning, direction="write"
                ),
                "immobilization": convert_and_respect_annotation_metadata(
                    object_=immobilization, annotation=RemoteSetImmobilization, direction="write"
                ),
                "door": convert_and_respect_annotation_metadata(
                    object_=door, annotation=RemoteDoorsState, direction="write"
                ),
                "horn": convert_and_respect_annotation_metadata(object_=horn, annotation=RemoteHorn, direction="write"),
                "charging": convert_and_respect_annotation_metadata(
                    object_=charging, annotation=RemoteCharging, direction="write"
                ),
                "stolen": convert_and_respect_annotation_metadata(
                    object_=stolen, annotation=RemoteStolen, direction="write"
                ),
                "lights": convert_and_respect_annotation_metadata(
                    object_=lights, annotation=RemoteLights, direction="write"
                ),
                "wakeUp": convert_and_respect_annotation_metadata(
                    object_=wake_up, annotation=RemoteWakeUp, direction="write"
                ),
                "navigation": convert_and_respect_annotation_metadata(
                    object_=navigation, annotation=RemoteNavigation, direction="write"
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
                    RemotePostResponse,
                    parse_obj_as(
                        type_=RemotePostResponse,
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

    async def get_remote_request_for_vhl_by_id(
        self, fid: str, vid: str, cbid: str, rid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RemoteAction]:
        """
        Returns the remote action requested for vehicle by ID.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cbid : str
            The remote callback ID.

        rid : str
            The remote action ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoteAction]
            A remote action response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/vehicles/{encode_path_param(vid)}/callbacks/{encode_path_param(cbid)}/remotes/{encode_path_param(rid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RemoteAction,
                    parse_obj_as(
                        type_=RemoteAction,
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
