

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_next_models_ng_route import OtoroshiNextModelsNgRoute
from ..types.otoroshi_next_models_ng_route_backend_ref import OtoroshiNextModelsNgRouteBackendRef
from .raw_client import AsyncRawRoutesClient, RawRoutesClient


OMIT = typing.cast(typing.Any, ...)


class RoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoutesClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key_quotas(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key_quotas(
            route_id="routeId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key_quotas(
            route_id, client_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_reset_api_key_quotas(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_reset_api_key_quotas(
            route_id="routeId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_reset_api_key_quotas(
            route_id, client_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key(
            route_id="routeId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key(
            route_id, client_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_update_api_key(
        self,
        route_id: str,
        client_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_update_api_key(
            route_id="routeId",
            client_id="clientId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_update_api_key(
            route_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_delete_api_key(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_delete_api_key(
            route_id="routeId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_delete_api_key(
            route_id, client_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_patch_api_key(
        self,
        route_id: str,
        client_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_patch_api_key(
            route_id="routeId",
            client_id="clientId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_patch_api_key(
            route_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_api_keys(
        self, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_keys(
            route_id="routeId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_keys(
            route_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_from_route_controller_create_api_key(
        self,
        route_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_create_api_key(
            route_id="routeId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_create_api_key(
            route_id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_form(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_form()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_form(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_initiate_route(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_initiate_route()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_initiate_route(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRoute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRoute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiNextModelsNgRoute

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_create_action(
            request=[OtoroshiNextModelsNgRoute()],
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRoute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRoute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiNextModelsNgRoute

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_update_action(
            request=[OtoroshiNextModelsNgRoute()],
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_update_entity_action(
        self,
        id_: str,
        *,
        debug_flow: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        frontend: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        capture: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        backend_ref: typing.Optional[OtoroshiNextModelsNgRouteBackendRef] = OMIT,
        description: typing.Optional[str] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        debug_flow : typing.Optional[bool]
            Enable report debugging

        enabled : typing.Optional[bool]
            Is the route enabled

        name : typing.Optional[str]
            The name of the route

        id : typing.Optional[str]
            The ud of the route

        export_reporting : typing.Optional[bool]
            Export the execution reporting through standard data exporter

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the route

        frontend : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the route

        capture : typing.Optional[bool]
            Capture http traffic

        groups : typing.Optional[typing.Sequence[str]]
            The groups of the route

        backend_ref : typing.Optional[OtoroshiNextModelsNgRouteBackendRef]
            The backend id of the route (if one)

        description : typing.Optional[str]
            The description of the route

        backend : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_update_entity_action(
            id_,
            debug_flow=debug_flow,
            enabled=enabled,
            name=name,
            id=id,
            export_reporting=export_reporting,
            metadata=metadata,
            frontend=frontend,
            loc=loc,
            tags=tags,
            capture=capture,
            groups=groups,
            backend_ref=backend_ref,
            description=description,
            backend=backend,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_patch_entity_action(
        self,
        id_: str,
        *,
        debug_flow: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        frontend: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        capture: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        backend_ref: typing.Optional[OtoroshiNextModelsNgRouteBackendRef] = OMIT,
        description: typing.Optional[str] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        debug_flow : typing.Optional[bool]
            Enable report debugging

        enabled : typing.Optional[bool]
            Is the route enabled

        name : typing.Optional[str]
            The name of the route

        id : typing.Optional[str]
            The ud of the route

        export_reporting : typing.Optional[bool]
            Export the execution reporting through standard data exporter

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the route

        frontend : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the route

        capture : typing.Optional[bool]
            Capture http traffic

        groups : typing.Optional[typing.Sequence[str]]
            The groups of the route

        backend_ref : typing.Optional[OtoroshiNextModelsNgRouteBackendRef]
            The backend id of the route (if one)

        description : typing.Optional[str]
            The description of the route

        backend : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_patch_entity_action(
            id_,
            debug_flow=debug_flow,
            enabled=enabled,
            name=name,
            id=id,
            export_reporting=export_reporting,
            metadata=metadata,
            frontend=frontend,
            loc=loc,
            tags=tags,
            capture=capture,
            groups=groups,
            backend_ref=backend_ref,
            description=description,
            backend=backend,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiNextModelsNgRoute]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiNextModelsNgRoute]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_routes_controller_create_action(
        self,
        *,
        debug_flow: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        frontend: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        capture: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        backend_ref: typing.Optional[OtoroshiNextModelsNgRouteBackendRef] = OMIT,
        description: typing.Optional[str] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        debug_flow : typing.Optional[bool]
            Enable report debugging

        enabled : typing.Optional[bool]
            Is the route enabled

        name : typing.Optional[str]
            The name of the route

        id : typing.Optional[str]
            The ud of the route

        export_reporting : typing.Optional[bool]
            Export the execution reporting through standard data exporter

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the route

        frontend : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the route

        capture : typing.Optional[bool]
            Capture http traffic

        groups : typing.Optional[typing.Sequence[str]]
            The groups of the route

        backend_ref : typing.Optional[OtoroshiNextModelsNgRouteBackendRef]
            The backend id of the route (if one)

        description : typing.Optional[str]
            The description of the route

        backend : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_create_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_create_action(
            debug_flow=debug_flow,
            enabled=enabled,
            name=name,
            id=id,
            export_reporting=export_reporting,
            metadata=metadata,
            frontend=frontend,
            loc=loc,
            tags=tags,
            capture=capture,
            groups=groups,
            backend_ref=backend_ref,
            description=description,
            backend=backend,
            request_options=request_options,
        )
        return _response.data


class AsyncRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoutesClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key_quotas(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key_quotas(
                route_id="routeId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key_quotas(
            route_id, client_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_reset_api_key_quotas(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_reset_api_key_quotas(
                route_id="routeId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_reset_api_key_quotas(
                route_id, client_id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key(
                route_id="routeId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_key(
            route_id, client_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_update_api_key(
        self,
        route_id: str,
        client_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_update_api_key(
                route_id="routeId",
                client_id="clientId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_update_api_key(
            route_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_delete_api_key(
        self, route_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_delete_api_key(
                route_id="routeId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_delete_api_key(
            route_id, client_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_patch_api_key(
        self,
        route_id: str,
        client_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        client_id : str
            the clientId parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_patch_api_key(
                route_id="routeId",
                client_id="clientId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_patch_api_key(
            route_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_api_keys(
        self, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_keys(
                route_id="routeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_api_keys(
            route_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_from_route_controller_create_api_key(
        self,
        route_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        route_id : str
            the routeId parameter

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_controllers_adminapi_api_keys_from_route_controller_create_api_key(
                route_id="routeId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_from_route_controller_create_api_key(
            route_id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_form(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_form(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_initiate_route(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_initiate_route()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_initiate_route(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRoute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRoute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiNextModelsNgRoute

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_create_action(
                request=[OtoroshiNextModelsNgRoute()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRoute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRoute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiNextModelsNgRoute

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_update_action(
                request=[OtoroshiNextModelsNgRoute()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_update_entity_action(
        self,
        id_: str,
        *,
        debug_flow: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        frontend: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        capture: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        backend_ref: typing.Optional[OtoroshiNextModelsNgRouteBackendRef] = OMIT,
        description: typing.Optional[str] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        debug_flow : typing.Optional[bool]
            Enable report debugging

        enabled : typing.Optional[bool]
            Is the route enabled

        name : typing.Optional[str]
            The name of the route

        id : typing.Optional[str]
            The ud of the route

        export_reporting : typing.Optional[bool]
            Export the execution reporting through standard data exporter

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the route

        frontend : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the route

        capture : typing.Optional[bool]
            Capture http traffic

        groups : typing.Optional[typing.Sequence[str]]
            The groups of the route

        backend_ref : typing.Optional[OtoroshiNextModelsNgRouteBackendRef]
            The backend id of the route (if one)

        description : typing.Optional[str]
            The description of the route

        backend : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_update_entity_action(
            id_,
            debug_flow=debug_flow,
            enabled=enabled,
            name=name,
            id=id,
            export_reporting=export_reporting,
            metadata=metadata,
            frontend=frontend,
            loc=loc,
            tags=tags,
            capture=capture,
            groups=groups,
            backend_ref=backend_ref,
            description=description,
            backend=backend,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_patch_entity_action(
        self,
        id_: str,
        *,
        debug_flow: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        frontend: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        capture: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        backend_ref: typing.Optional[OtoroshiNextModelsNgRouteBackendRef] = OMIT,
        description: typing.Optional[str] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        debug_flow : typing.Optional[bool]
            Enable report debugging

        enabled : typing.Optional[bool]
            Is the route enabled

        name : typing.Optional[str]
            The name of the route

        id : typing.Optional[str]
            The ud of the route

        export_reporting : typing.Optional[bool]
            Export the execution reporting through standard data exporter

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the route

        frontend : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the route

        capture : typing.Optional[bool]
            Capture http traffic

        groups : typing.Optional[typing.Sequence[str]]
            The groups of the route

        backend_ref : typing.Optional[OtoroshiNextModelsNgRouteBackendRef]
            The backend id of the route (if one)

        description : typing.Optional[str]
            The description of the route

        backend : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_patch_entity_action(
            id_,
            debug_flow=debug_flow,
            enabled=enabled,
            name=name,
            id=id,
            export_reporting=export_reporting,
            metadata=metadata,
            frontend=frontend,
            loc=loc,
            tags=tags,
            capture=capture,
            groups=groups,
            backend_ref=backend_ref,
            description=description,
            backend=backend,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiNextModelsNgRoute]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiNextModelsNgRoute]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_routes_controller_create_action(
        self,
        *,
        debug_flow: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        frontend: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        capture: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        backend_ref: typing.Optional[OtoroshiNextModelsNgRouteBackendRef] = OMIT,
        description: typing.Optional[str] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRoute:
        """
        Parameters
        ----------
        debug_flow : typing.Optional[bool]
            Enable report debugging

        enabled : typing.Optional[bool]
            Is the route enabled

        name : typing.Optional[str]
            The name of the route

        id : typing.Optional[str]
            The ud of the route

        export_reporting : typing.Optional[bool]
            Export the execution reporting through standard data exporter

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the route

        frontend : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the route

        capture : typing.Optional[bool]
            Capture http traffic

        groups : typing.Optional[typing.Sequence[str]]
            The groups of the route

        backend_ref : typing.Optional[OtoroshiNextModelsNgRouteBackendRef]
            The backend id of the route (if one)

        description : typing.Optional[str]
            The description of the route

        backend : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRoute
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.routes.otoroshi_next_controllers_adminapi_ng_routes_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_routes_controller_create_action(
            debug_flow=debug_flow,
            enabled=enabled,
            name=name,
            id=id,
            export_reporting=export_reporting,
            metadata=metadata,
            frontend=frontend,
            loc=loc,
            tags=tags,
            capture=capture,
            groups=groups,
            backend_ref=backend_ref,
            description=description,
            backend=backend,
            request_options=request_options,
        )
        return _response.data
