

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawRemoteClient, RawRemoteClient
from .types.remote_callbacks_status_setter_status import RemoteCallbacksStatusSetterStatus


OMIT = typing.cast(typing.Any, ...)


class RemoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRemoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRemoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRemoteClient
        """
        return self._raw_client

    def get_fleet_remotes(
        self,
        fid: str,
        *,
        types: typing.Optional[typing.Union[RemoteType, typing.Sequence[RemoteType]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoteCallbacks:
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
        RemoteCallbacks
            A list of subsribed remote callback.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.get_fleet_remotes(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet_remotes(
            fid,
            types=types,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CallbackRef:
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
        CallbackRef
            Remote callback creation or update success response

        Examples
        --------
        from fern import FernApi, RemoteType

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.set_fleet_vehicle_remote(
            fid="fid",
            remote_types=[
                RemoteType.THERMAL_PRECONDITIONING,
                RemoteType.THERMAL_PRECONDITIONING,
            ],
        )
        """
        _response = self._raw_client.set_fleet_vehicle_remote(
            fid,
            remote_types=remote_types,
            label=label,
            retry_policy=retry_policy,
            callback=callback,
            batch_notify=batch_notify,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_remoteby_id(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteCallback:
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
        RemoteCallback
            A remote callback.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.get_fleet_remoteby_id(
            fid="fid",
            cbid="cbid",
        )
        """
        _response = self._raw_client.get_fleet_remoteby_id(fid, cbid, request_options=request_options)
        return _response.data

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
    ) -> CallbackRef:
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
        CallbackRef
            Remote callback creation or update success response

        Examples
        --------
        from fern import FernApi, RemoteType

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.set_fleet_vehicle_remote_by_id(
            fid="fid",
            cbid="cbid",
            remote_types=[
                RemoteType.THERMAL_PRECONDITIONING,
                RemoteType.THERMAL_PRECONDITIONING,
            ],
        )
        """
        _response = self._raw_client.set_fleet_vehicle_remote_by_id(
            fid,
            cbid,
            remote_types=remote_types,
            label=label,
            retry_policy=retry_policy,
            callback=callback,
            batch_notify=batch_notify,
            request_options=request_options,
        )
        return _response.data

    def delete_fleet_remote(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.delete_fleet_remote(
            fid="fid",
            cbid="cbid",
        )
        """
        _response = self._raw_client.delete_fleet_remote(fid, cbid, request_options=request_options)
        return _response.data

    def set_flee_remote_callback_status(
        self,
        fid: str,
        cbid: str,
        *,
        status: RemoteCallbacksStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallbackRef:
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
        CallbackRef
            Remote callback creation or update success response

        Examples
        --------
        from fern.remote import RemoteCallbacksStatusSetterStatus

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.set_flee_remote_callback_status(
            fid="fid",
            cbid="cbid",
            status=RemoteCallbacksStatusSetterStatus.RUNNING,
        )
        """
        _response = self._raw_client.set_flee_remote_callback_status(
            fid, cbid, status=status, request_options=request_options
        )
        return _response.data

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
    ) -> RemoteActions:
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
        RemoteActions
            A list of remote actions.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.get_remote_requests_for_vhl(
            fid="fid",
            vid="vid",
            cbid="cbid",
        )
        """
        _response = self._raw_client.get_remote_requests_for_vhl(
            fid,
            vid,
            cbid,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> RemotePostResponse:
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
        RemotePostResponse
            Remote action creation success response (accepted).

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.send_remote_to_vhl(
            fid="fid",
            vid="vid",
            cbid="cbid",
        )
        """
        _response = self._raw_client.send_remote_to_vhl(
            fid,
            vid,
            cbid,
            label=label,
            preconditioning=preconditioning,
            immobilization=immobilization,
            door=door,
            horn=horn,
            charging=charging,
            stolen=stolen,
            lights=lights,
            wake_up=wake_up,
            navigation=navigation,
            request_options=request_options,
        )
        return _response.data

    def get_remote_request_for_vhl_by_id(
        self, fid: str, vid: str, cbid: str, rid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteAction:
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
        RemoteAction
            A remote action response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remote.get_remote_request_for_vhl_by_id(
            fid="fid",
            vid="vid",
            cbid="cbid",
            rid="rid",
        )
        """
        _response = self._raw_client.get_remote_request_for_vhl_by_id(
            fid, vid, cbid, rid, request_options=request_options
        )
        return _response.data


class AsyncRemoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRemoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRemoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRemoteClient
        """
        return self._raw_client

    async def get_fleet_remotes(
        self,
        fid: str,
        *,
        types: typing.Optional[typing.Union[RemoteType, typing.Sequence[RemoteType]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoteCallbacks:
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
        RemoteCallbacks
            A list of subsribed remote callback.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.get_fleet_remotes(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_remotes(
            fid,
            types=types,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CallbackRef:
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
        CallbackRef
            Remote callback creation or update success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RemoteType

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.set_fleet_vehicle_remote(
                fid="fid",
                remote_types=[
                    RemoteType.THERMAL_PRECONDITIONING,
                    RemoteType.THERMAL_PRECONDITIONING,
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_fleet_vehicle_remote(
            fid,
            remote_types=remote_types,
            label=label,
            retry_policy=retry_policy,
            callback=callback,
            batch_notify=batch_notify,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_remoteby_id(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteCallback:
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
        RemoteCallback
            A remote callback.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.get_fleet_remoteby_id(
                fid="fid",
                cbid="cbid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_remoteby_id(fid, cbid, request_options=request_options)
        return _response.data

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
    ) -> CallbackRef:
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
        CallbackRef
            Remote callback creation or update success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RemoteType

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.set_fleet_vehicle_remote_by_id(
                fid="fid",
                cbid="cbid",
                remote_types=[
                    RemoteType.THERMAL_PRECONDITIONING,
                    RemoteType.THERMAL_PRECONDITIONING,
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_fleet_vehicle_remote_by_id(
            fid,
            cbid,
            remote_types=remote_types,
            label=label,
            retry_policy=retry_policy,
            callback=callback,
            batch_notify=batch_notify,
            request_options=request_options,
        )
        return _response.data

    async def delete_fleet_remote(
        self, fid: str, cbid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.delete_fleet_remote(
                fid="fid",
                cbid="cbid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_fleet_remote(fid, cbid, request_options=request_options)
        return _response.data

    async def set_flee_remote_callback_status(
        self,
        fid: str,
        cbid: str,
        *,
        status: RemoteCallbacksStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallbackRef:
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
        CallbackRef
            Remote callback creation or update success response

        Examples
        --------
        import asyncio

        from fern.remote import RemoteCallbacksStatusSetterStatus

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.set_flee_remote_callback_status(
                fid="fid",
                cbid="cbid",
                status=RemoteCallbacksStatusSetterStatus.RUNNING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_flee_remote_callback_status(
            fid, cbid, status=status, request_options=request_options
        )
        return _response.data

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
    ) -> RemoteActions:
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
        RemoteActions
            A list of remote actions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.get_remote_requests_for_vhl(
                fid="fid",
                vid="vid",
                cbid="cbid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_remote_requests_for_vhl(
            fid,
            vid,
            cbid,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> RemotePostResponse:
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
        RemotePostResponse
            Remote action creation success response (accepted).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.send_remote_to_vhl(
                fid="fid",
                vid="vid",
                cbid="cbid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_remote_to_vhl(
            fid,
            vid,
            cbid,
            label=label,
            preconditioning=preconditioning,
            immobilization=immobilization,
            door=door,
            horn=horn,
            charging=charging,
            stolen=stolen,
            lights=lights,
            wake_up=wake_up,
            navigation=navigation,
            request_options=request_options,
        )
        return _response.data

    async def get_remote_request_for_vhl_by_id(
        self, fid: str, vid: str, cbid: str, rid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteAction:
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
        RemoteAction
            A remote action response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remote.get_remote_request_for_vhl_by_id(
                fid="fid",
                vid="vid",
                cbid="cbid",
                rid="rid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_remote_request_for_vhl_by_id(
            fid, vid, cbid, rid, request_options=request_options
        )
        return _response.data
