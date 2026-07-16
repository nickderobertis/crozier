

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.group import Group
from ..types.ip_network import IpNetwork
from ..types.object_permission import ObjectPermission
from ..types.token import Token
from ..types.user import User
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.users_groups_list_response import UsersGroupsListResponse
from .types.users_permissions_list_response import UsersPermissionsListResponse
from .types.users_tokens_list_response import UsersTokensListResponse
from .types.users_users_list_response import UsersUsersListResponse


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def config_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Return the UserConfig for the currently authenticated User.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.config_list()
        """
        _response = self._raw_client.config_list(request_options=request_options)
        return _response.data

    def groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersGroupsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGroupsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_list()
        """
        _response = self._raw_client.groups_list(
            id=id,
            name=name,
            q=q,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def groups_create(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_create(
            name="name",
        )
        """
        _response = self._raw_client.groups_create(
            name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    def groups_bulk_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_bulk_update(
            name="name",
        )
        """
        _response = self._raw_client.groups_bulk_update(
            name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    def groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_bulk_delete()
        """
        _response = self._raw_client.groups_bulk_delete(request_options=request_options)
        return _response.data

    def groups_bulk_partial_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_bulk_partial_update(
            name="name",
        )
        """
        _response = self._raw_client.groups_bulk_partial_update(
            name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    def groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_read(
            id=1,
        )
        """
        _response = self._raw_client.groups_read(id, request_options=request_options)
        return _response.data

    def groups_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.groups_update(
            id_, name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    def groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_delete(
            id=1,
        )
        """
        _response = self._raw_client.groups_delete(id, request_options=request_options)
        return _response.data

    def groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.groups_partial_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.groups_partial_update(
            id_, name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    def permissions_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        object_types: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        object_types_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersPermissionsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        object_types : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        object_types_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersPermissionsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_list()
        """
        _response = self._raw_client.permissions_list(
            id=id,
            name=name,
            enabled=enabled,
            object_types=object_types,
            description=description,
            q=q,
            user_id=user_id,
            user=user,
            group_id=group_id,
            group=group,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            object_types_n=object_types_n,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            user_id_n=user_id_n,
            user_n=user_n,
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def permissions_create(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_create(
            actions=["actions"],
            name="name",
            object_types=["object_types"],
        )
        """
        _response = self._raw_client.permissions_create(
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    def permissions_bulk_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_bulk_update(
            actions=["actions"],
            name="name",
            object_types=["object_types"],
        )
        """
        _response = self._raw_client.permissions_bulk_update(
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    def permissions_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_bulk_delete()
        """
        _response = self._raw_client.permissions_bulk_delete(request_options=request_options)
        return _response.data

    def permissions_bulk_partial_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_bulk_partial_update(
            actions=["actions"],
            name="name",
            object_types=["object_types"],
        )
        """
        _response = self._raw_client.permissions_bulk_partial_update(
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    def permissions_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ObjectPermission:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_read(
            id=1,
        )
        """
        _response = self._raw_client.permissions_read(id, request_options=request_options)
        return _response.data

    def permissions_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_update(
            id_=1,
            actions=["actions"],
            name="name",
            object_types=["object_types"],
        )
        """
        _response = self._raw_client.permissions_update(
            id_,
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    def permissions_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_delete(
            id=1,
        )
        """
        _response = self._raw_client.permissions_delete(id, request_options=request_options)
        return _response.data

    def permissions_partial_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.permissions_partial_update(
            id_=1,
            actions=["actions"],
            name="name",
            object_types=["object_types"],
        )
        """
        _response = self._raw_client.permissions_partial_update(
            id_,
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    def tokens_list(
        self,
        *,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        write_enabled: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        expires_gte: typing.Optional[str] = None,
        expires_lte: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        key_n: typing.Optional[str] = None,
        key_ic: typing.Optional[str] = None,
        key_nic: typing.Optional[str] = None,
        key_iew: typing.Optional[str] = None,
        key_niew: typing.Optional[str] = None,
        key_isw: typing.Optional[str] = None,
        key_nisw: typing.Optional[str] = None,
        key_ie: typing.Optional[str] = None,
        key_nie: typing.Optional[str] = None,
        key_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersTokensListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        key : typing.Optional[str]


        write_enabled : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        created : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_lte : typing.Optional[str]


        expires : typing.Optional[str]


        expires_gte : typing.Optional[str]


        expires_lte : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        key_n : typing.Optional[str]


        key_ic : typing.Optional[str]


        key_nic : typing.Optional[str]


        key_iew : typing.Optional[str]


        key_niew : typing.Optional[str]


        key_isw : typing.Optional[str]


        key_nisw : typing.Optional[str]


        key_ie : typing.Optional[str]


        key_nie : typing.Optional[str]


        key_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersTokensListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_list()
        """
        _response = self._raw_client.tokens_list(
            id=id,
            key=key,
            write_enabled=write_enabled,
            description=description,
            q=q,
            user_id=user_id,
            user=user,
            created=created,
            created_gte=created_gte,
            created_lte=created_lte,
            expires=expires,
            expires_gte=expires_gte,
            expires_lte=expires_lte,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            key_n=key_n,
            key_ic=key_ic,
            key_nic=key_nic,
            key_iew=key_iew,
            key_niew=key_niew,
            key_isw=key_isw,
            key_nisw=key_nisw,
            key_ie=key_ie,
            key_nie=key_nie,
            key_empty=key_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            user_id_n=user_id_n,
            user_n=user_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def tokens_create(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_create(
            user=1,
        )
        """
        _response = self._raw_client.tokens_create(
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    def tokens_bulk_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_bulk_update(
            user=1,
        )
        """
        _response = self._raw_client.tokens_bulk_update(
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    def tokens_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_bulk_delete()
        """
        _response = self._raw_client.tokens_bulk_delete(request_options=request_options)
        return _response.data

    def tokens_bulk_partial_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_bulk_partial_update(
            user=1,
        )
        """
        _response = self._raw_client.tokens_bulk_partial_update(
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    def tokens_provision_create(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Non-authenticated REST API endpoint via which a user may create a Token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_provision_create()
        """
        _response = self._raw_client.tokens_provision_create(request_options=request_options)
        return _response.data

    def tokens_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Token:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_read(
            id=1,
        )
        """
        _response = self._raw_client.tokens_read(id, request_options=request_options)
        return _response.data

    def tokens_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_update(
            id_=1,
            user=1,
        )
        """
        _response = self._raw_client.tokens_update(
            id_,
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    def tokens_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_delete(
            id=1,
        )
        """
        _response = self._raw_client.tokens_delete(id, request_options=request_options)
        return _response.data

    def tokens_partial_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.tokens_partial_update(
            id_=1,
            user=1,
        )
        """
        _response = self._raw_client.tokens_partial_update(
            id_,
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    def users_list(
        self,
        *,
        id: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        is_staff: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        username_n: typing.Optional[str] = None,
        username_ic: typing.Optional[str] = None,
        username_nic: typing.Optional[str] = None,
        username_iew: typing.Optional[str] = None,
        username_niew: typing.Optional[str] = None,
        username_isw: typing.Optional[str] = None,
        username_nisw: typing.Optional[str] = None,
        username_ie: typing.Optional[str] = None,
        username_nie: typing.Optional[str] = None,
        username_empty: typing.Optional[str] = None,
        first_name_n: typing.Optional[str] = None,
        first_name_ic: typing.Optional[str] = None,
        first_name_nic: typing.Optional[str] = None,
        first_name_iew: typing.Optional[str] = None,
        first_name_niew: typing.Optional[str] = None,
        first_name_isw: typing.Optional[str] = None,
        first_name_nisw: typing.Optional[str] = None,
        first_name_ie: typing.Optional[str] = None,
        first_name_nie: typing.Optional[str] = None,
        first_name_empty: typing.Optional[str] = None,
        last_name_n: typing.Optional[str] = None,
        last_name_ic: typing.Optional[str] = None,
        last_name_nic: typing.Optional[str] = None,
        last_name_iew: typing.Optional[str] = None,
        last_name_niew: typing.Optional[str] = None,
        last_name_isw: typing.Optional[str] = None,
        last_name_nisw: typing.Optional[str] = None,
        last_name_ie: typing.Optional[str] = None,
        last_name_nie: typing.Optional[str] = None,
        last_name_empty: typing.Optional[str] = None,
        email_n: typing.Optional[str] = None,
        email_ic: typing.Optional[str] = None,
        email_nic: typing.Optional[str] = None,
        email_iew: typing.Optional[str] = None,
        email_niew: typing.Optional[str] = None,
        email_isw: typing.Optional[str] = None,
        email_nisw: typing.Optional[str] = None,
        email_ie: typing.Optional[str] = None,
        email_nie: typing.Optional[str] = None,
        email_empty: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUsersListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        username : typing.Optional[str]


        first_name : typing.Optional[str]


        last_name : typing.Optional[str]


        email : typing.Optional[str]


        is_staff : typing.Optional[str]


        is_active : typing.Optional[str]


        q : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        username_n : typing.Optional[str]


        username_ic : typing.Optional[str]


        username_nic : typing.Optional[str]


        username_iew : typing.Optional[str]


        username_niew : typing.Optional[str]


        username_isw : typing.Optional[str]


        username_nisw : typing.Optional[str]


        username_ie : typing.Optional[str]


        username_nie : typing.Optional[str]


        username_empty : typing.Optional[str]


        first_name_n : typing.Optional[str]


        first_name_ic : typing.Optional[str]


        first_name_nic : typing.Optional[str]


        first_name_iew : typing.Optional[str]


        first_name_niew : typing.Optional[str]


        first_name_isw : typing.Optional[str]


        first_name_nisw : typing.Optional[str]


        first_name_ie : typing.Optional[str]


        first_name_nie : typing.Optional[str]


        first_name_empty : typing.Optional[str]


        last_name_n : typing.Optional[str]


        last_name_ic : typing.Optional[str]


        last_name_nic : typing.Optional[str]


        last_name_iew : typing.Optional[str]


        last_name_niew : typing.Optional[str]


        last_name_isw : typing.Optional[str]


        last_name_nisw : typing.Optional[str]


        last_name_ie : typing.Optional[str]


        last_name_nie : typing.Optional[str]


        last_name_empty : typing.Optional[str]


        email_n : typing.Optional[str]


        email_ic : typing.Optional[str]


        email_nic : typing.Optional[str]


        email_iew : typing.Optional[str]


        email_niew : typing.Optional[str]


        email_isw : typing.Optional[str]


        email_nisw : typing.Optional[str]


        email_ie : typing.Optional[str]


        email_nie : typing.Optional[str]


        email_empty : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUsersListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_list()
        """
        _response = self._raw_client.users_list(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            q=q,
            group_id=group_id,
            group=group,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            username_n=username_n,
            username_ic=username_ic,
            username_nic=username_nic,
            username_iew=username_iew,
            username_niew=username_niew,
            username_isw=username_isw,
            username_nisw=username_nisw,
            username_ie=username_ie,
            username_nie=username_nie,
            username_empty=username_empty,
            first_name_n=first_name_n,
            first_name_ic=first_name_ic,
            first_name_nic=first_name_nic,
            first_name_iew=first_name_iew,
            first_name_niew=first_name_niew,
            first_name_isw=first_name_isw,
            first_name_nisw=first_name_nisw,
            first_name_ie=first_name_ie,
            first_name_nie=first_name_nie,
            first_name_empty=first_name_empty,
            last_name_n=last_name_n,
            last_name_ic=last_name_ic,
            last_name_nic=last_name_nic,
            last_name_iew=last_name_iew,
            last_name_niew=last_name_niew,
            last_name_isw=last_name_isw,
            last_name_nisw=last_name_nisw,
            last_name_ie=last_name_ie,
            last_name_nie=last_name_nie,
            last_name_empty=last_name_empty,
            email_n=email_n,
            email_ic=email_ic,
            email_nic=email_nic,
            email_iew=email_iew,
            email_niew=email_niew,
            email_isw=email_isw,
            email_nisw=email_nisw,
            email_ie=email_ie,
            email_nie=email_nie,
            email_empty=email_empty,
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def users_create(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_create(
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.users_create(
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def users_bulk_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_bulk_update(
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.users_bulk_update(
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def users_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_bulk_delete()
        """
        _response = self._raw_client.users_bulk_delete(request_options=request_options)
        return _response.data

    def users_bulk_partial_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_bulk_partial_update(
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.users_bulk_partial_update(
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def users_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_read(
            id=1,
        )
        """
        _response = self._raw_client.users_read(id, request_options=request_options)
        return _response.data

    def users_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_update(
            id_=1,
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.users_update(
            id_,
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def users_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_delete(
            id=1,
        )
        """
        _response = self._raw_client.users_delete(id, request_options=request_options)
        return _response.data

    def users_partial_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.users_partial_update(
            id_=1,
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.users_partial_update(
            id_,
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def config_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Return the UserConfig for the currently authenticated User.

        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.config_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.config_list(request_options=request_options)
        return _response.data

    async def groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersGroupsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGroupsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_list(
            id=id,
            name=name,
            q=q,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def groups_create(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_create(
            name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    async def groups_bulk_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_bulk_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_bulk_update(
            name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    async def groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_bulk_delete(request_options=request_options)
        return _response.data

    async def groups_bulk_partial_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_bulk_partial_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_bulk_partial_update(
            name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    async def groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_read(id, request_options=request_options)
        return _response.data

    async def groups_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_update(
            id_, name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    async def groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_delete(id, request_options=request_options)
        return _response.data

    async def groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.groups_partial_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.groups_partial_update(
            id_, name=name, display=display, id=id, url=url, user_count=user_count, request_options=request_options
        )
        return _response.data

    async def permissions_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        object_types: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        object_types_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersPermissionsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        object_types : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        object_types_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersPermissionsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_list(
            id=id,
            name=name,
            enabled=enabled,
            object_types=object_types,
            description=description,
            q=q,
            user_id=user_id,
            user=user,
            group_id=group_id,
            group=group,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            object_types_n=object_types_n,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            user_id_n=user_id_n,
            user_n=user_n,
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def permissions_create(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_create(
                actions=["actions"],
                name="name",
                object_types=["object_types"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_create(
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    async def permissions_bulk_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_bulk_update(
                actions=["actions"],
                name="name",
                object_types=["object_types"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_bulk_update(
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    async def permissions_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_bulk_delete(request_options=request_options)
        return _response.data

    async def permissions_bulk_partial_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_bulk_partial_update(
                actions=["actions"],
                name="name",
                object_types=["object_types"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_bulk_partial_update(
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    async def permissions_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_read(id, request_options=request_options)
        return _response.data

    async def permissions_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_update(
                id_=1,
                actions=["actions"],
                name="name",
                object_types=["object_types"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_update(
            id_,
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    async def permissions_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_delete(id, request_options=request_options)
        return _response.data

    async def permissions_partial_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjectPermission:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Any]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectPermission


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.permissions_partial_update(
                id_=1,
                actions=["actions"],
                name="name",
                object_types=["object_types"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permissions_partial_update(
            id_,
            actions=actions,
            name=name,
            object_types=object_types,
            constraints=constraints,
            description=description,
            display=display,
            enabled=enabled,
            groups=groups,
            id=id,
            url=url,
            users=users,
            request_options=request_options,
        )
        return _response.data

    async def tokens_list(
        self,
        *,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        write_enabled: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        expires_gte: typing.Optional[str] = None,
        expires_lte: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        key_n: typing.Optional[str] = None,
        key_ic: typing.Optional[str] = None,
        key_nic: typing.Optional[str] = None,
        key_iew: typing.Optional[str] = None,
        key_niew: typing.Optional[str] = None,
        key_isw: typing.Optional[str] = None,
        key_nisw: typing.Optional[str] = None,
        key_ie: typing.Optional[str] = None,
        key_nie: typing.Optional[str] = None,
        key_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersTokensListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        key : typing.Optional[str]


        write_enabled : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        created : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_lte : typing.Optional[str]


        expires : typing.Optional[str]


        expires_gte : typing.Optional[str]


        expires_lte : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        key_n : typing.Optional[str]


        key_ic : typing.Optional[str]


        key_nic : typing.Optional[str]


        key_iew : typing.Optional[str]


        key_niew : typing.Optional[str]


        key_isw : typing.Optional[str]


        key_nisw : typing.Optional[str]


        key_ie : typing.Optional[str]


        key_nie : typing.Optional[str]


        key_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersTokensListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_list(
            id=id,
            key=key,
            write_enabled=write_enabled,
            description=description,
            q=q,
            user_id=user_id,
            user=user,
            created=created,
            created_gte=created_gte,
            created_lte=created_lte,
            expires=expires,
            expires_gte=expires_gte,
            expires_lte=expires_lte,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            key_n=key_n,
            key_ic=key_ic,
            key_nic=key_nic,
            key_iew=key_iew,
            key_niew=key_niew,
            key_isw=key_isw,
            key_nisw=key_nisw,
            key_ie=key_ie,
            key_nie=key_nie,
            key_empty=key_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            user_id_n=user_id_n,
            user_n=user_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def tokens_create(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_create(
                user=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_create(
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    async def tokens_bulk_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_bulk_update(
                user=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_bulk_update(
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    async def tokens_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_bulk_delete(request_options=request_options)
        return _response.data

    async def tokens_bulk_partial_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_bulk_partial_update(
                user=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_bulk_partial_update(
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    async def tokens_provision_create(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Non-authenticated REST API endpoint via which a user may create a Token.

        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_provision_create()


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_provision_create(request_options=request_options)
        return _response.data

    async def tokens_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Token:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_read(id, request_options=request_options)
        return _response.data

    async def tokens_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_update(
                id_=1,
                user=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_update(
            id_,
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    async def tokens_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_delete(id, request_options=request_options)
        return _response.data

    async def tokens_partial_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.tokens_partial_update(
                id_=1,
                user=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_partial_update(
            id_,
            user=user,
            allowed_ips=allowed_ips,
            created=created,
            description=description,
            display=display,
            expires=expires,
            id=id,
            key=key,
            last_used=last_used,
            url=url,
            write_enabled=write_enabled,
            request_options=request_options,
        )
        return _response.data

    async def users_list(
        self,
        *,
        id: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        is_staff: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        username_n: typing.Optional[str] = None,
        username_ic: typing.Optional[str] = None,
        username_nic: typing.Optional[str] = None,
        username_iew: typing.Optional[str] = None,
        username_niew: typing.Optional[str] = None,
        username_isw: typing.Optional[str] = None,
        username_nisw: typing.Optional[str] = None,
        username_ie: typing.Optional[str] = None,
        username_nie: typing.Optional[str] = None,
        username_empty: typing.Optional[str] = None,
        first_name_n: typing.Optional[str] = None,
        first_name_ic: typing.Optional[str] = None,
        first_name_nic: typing.Optional[str] = None,
        first_name_iew: typing.Optional[str] = None,
        first_name_niew: typing.Optional[str] = None,
        first_name_isw: typing.Optional[str] = None,
        first_name_nisw: typing.Optional[str] = None,
        first_name_ie: typing.Optional[str] = None,
        first_name_nie: typing.Optional[str] = None,
        first_name_empty: typing.Optional[str] = None,
        last_name_n: typing.Optional[str] = None,
        last_name_ic: typing.Optional[str] = None,
        last_name_nic: typing.Optional[str] = None,
        last_name_iew: typing.Optional[str] = None,
        last_name_niew: typing.Optional[str] = None,
        last_name_isw: typing.Optional[str] = None,
        last_name_nisw: typing.Optional[str] = None,
        last_name_ie: typing.Optional[str] = None,
        last_name_nie: typing.Optional[str] = None,
        last_name_empty: typing.Optional[str] = None,
        email_n: typing.Optional[str] = None,
        email_ic: typing.Optional[str] = None,
        email_nic: typing.Optional[str] = None,
        email_iew: typing.Optional[str] = None,
        email_niew: typing.Optional[str] = None,
        email_isw: typing.Optional[str] = None,
        email_nisw: typing.Optional[str] = None,
        email_ie: typing.Optional[str] = None,
        email_nie: typing.Optional[str] = None,
        email_empty: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersUsersListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        username : typing.Optional[str]


        first_name : typing.Optional[str]


        last_name : typing.Optional[str]


        email : typing.Optional[str]


        is_staff : typing.Optional[str]


        is_active : typing.Optional[str]


        q : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        username_n : typing.Optional[str]


        username_ic : typing.Optional[str]


        username_nic : typing.Optional[str]


        username_iew : typing.Optional[str]


        username_niew : typing.Optional[str]


        username_isw : typing.Optional[str]


        username_nisw : typing.Optional[str]


        username_ie : typing.Optional[str]


        username_nie : typing.Optional[str]


        username_empty : typing.Optional[str]


        first_name_n : typing.Optional[str]


        first_name_ic : typing.Optional[str]


        first_name_nic : typing.Optional[str]


        first_name_iew : typing.Optional[str]


        first_name_niew : typing.Optional[str]


        first_name_isw : typing.Optional[str]


        first_name_nisw : typing.Optional[str]


        first_name_ie : typing.Optional[str]


        first_name_nie : typing.Optional[str]


        first_name_empty : typing.Optional[str]


        last_name_n : typing.Optional[str]


        last_name_ic : typing.Optional[str]


        last_name_nic : typing.Optional[str]


        last_name_iew : typing.Optional[str]


        last_name_niew : typing.Optional[str]


        last_name_isw : typing.Optional[str]


        last_name_nisw : typing.Optional[str]


        last_name_ie : typing.Optional[str]


        last_name_nie : typing.Optional[str]


        last_name_empty : typing.Optional[str]


        email_n : typing.Optional[str]


        email_ic : typing.Optional[str]


        email_nic : typing.Optional[str]


        email_iew : typing.Optional[str]


        email_niew : typing.Optional[str]


        email_isw : typing.Optional[str]


        email_nisw : typing.Optional[str]


        email_ie : typing.Optional[str]


        email_nie : typing.Optional[str]


        email_empty : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersUsersListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.users_list(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            q=q,
            group_id=group_id,
            group=group,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            username_n=username_n,
            username_ic=username_ic,
            username_nic=username_nic,
            username_iew=username_iew,
            username_niew=username_niew,
            username_isw=username_isw,
            username_nisw=username_nisw,
            username_ie=username_ie,
            username_nie=username_nie,
            username_empty=username_empty,
            first_name_n=first_name_n,
            first_name_ic=first_name_ic,
            first_name_nic=first_name_nic,
            first_name_iew=first_name_iew,
            first_name_niew=first_name_niew,
            first_name_isw=first_name_isw,
            first_name_nisw=first_name_nisw,
            first_name_ie=first_name_ie,
            first_name_nie=first_name_nie,
            first_name_empty=first_name_empty,
            last_name_n=last_name_n,
            last_name_ic=last_name_ic,
            last_name_nic=last_name_nic,
            last_name_iew=last_name_iew,
            last_name_niew=last_name_niew,
            last_name_isw=last_name_isw,
            last_name_nisw=last_name_nisw,
            last_name_ie=last_name_ie,
            last_name_nie=last_name_nie,
            last_name_empty=last_name_empty,
            email_n=email_n,
            email_ic=email_ic,
            email_nic=email_nic,
            email_iew=email_iew,
            email_niew=email_niew,
            email_isw=email_isw,
            email_nisw=email_nisw,
            email_ie=email_ie,
            email_nie=email_nie,
            email_empty=email_empty,
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def users_create(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_create(
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_create(
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def users_bulk_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_bulk_update(
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_bulk_update(
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def users_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.users_bulk_delete(request_options=request_options)
        return _response.data

    async def users_bulk_partial_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_bulk_partial_update(
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_bulk_partial_update(
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def users_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_read(id, request_options=request_options)
        return _response.data

    async def users_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_update(
                id_=1,
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_update(
            id_,
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def users_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_delete(id, request_options=request_options)
        return _response.data

    async def users_partial_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.users_partial_update(
                id_=1,
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_partial_update(
            id_,
            password=password,
            username=username,
            date_joined=date_joined,
            display=display,
            email=email,
            first_name=first_name,
            groups=groups,
            id=id,
            is_active=is_active,
            is_staff=is_staff,
            last_name=last_name,
            url=url,
            request_options=request_options,
        )
        return _response.data
