

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1state import V1State
from ..types.v1state_permission import V1StatePermission
from ..types.v1states_create_state import V1StatesCreateState
from ..types.v1states_update_state import V1StatesUpdateState
from .raw_client import AsyncRawEventStatesClient, RawEventStatesClient
from .types.v1state_permissions_create_state_permission import V1StatePermissionsCreateStatePermission


OMIT = typing.cast(typing.Any, ...)


class EventStatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventStatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventStatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventStatesClient
        """
        return self._raw_client

    def list_hour_states(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1State]:
        """
        List all available time entry states for the account.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1State]
            Time entry states list

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.list_hour_states(
            account_id=1,
        )
        """
        _response = self._raw_client.list_hour_states(account_id, request_options=request_options)
        return _response.data

    def create_hour_state(
        self, account_id: int, *, state: V1StatesCreateState, request_options: typing.Optional[RequestOptions] = None
    ) -> V1State:
        """
        Create a new time entry state. Only admin users can create states.

        Parameters
        ----------
        account_id : int
            Account ID

        state : V1StatesCreateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State created

        Examples
        --------
        from fern import FernApi, V1StatesCreateState

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.create_hour_state(
            account_id=1,
            state=V1StatesCreateState(
                name="Review Required",
                color="ff5722",
            ),
        )
        """
        _response = self._raw_client.create_hour_state(account_id, state=state, request_options=request_options)
        return _response.data

    def update_hour_state(
        self,
        account_id: int,
        id: int,
        *,
        state: V1StatesUpdateState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1State:
        """
        Update an existing time entry state. Only admin users can update states.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        state : V1StatesUpdateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State updated

        Examples
        --------
        from fern import FernApi, V1StatesUpdateState

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.update_hour_state(
            account_id=1,
            id=1,
            state=V1StatesUpdateState(
                name="Updated State Name",
            ),
        )
        """
        _response = self._raw_client.update_hour_state(account_id, id, state=state, request_options=request_options)
        return _response.data

    def delete_hour_state(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a time entry state. Only admin users can delete states and system-managed states cannot be deleted.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            State deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.delete_hour_state(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_hour_state(account_id, id, request_options=request_options)
        return _response.data

    def create_state_permissions(
        self,
        account_id: int,
        state_id: int,
        *,
        state_permission: V1StatePermissionsCreateStatePermission,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1StatePermission]:
        """
        Create or update permissions for a state. Admin access required. System-managed states cannot be modified.

        Parameters
        ----------
        account_id : int
            Account ID

        state_id : int
            State ID

        state_permission : V1StatePermissionsCreateStatePermission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1StatePermission]
            State permissions created successfully

        Examples
        --------
        from fern.event_states import V1StatePermissionsCreateStatePermission

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.create_state_permissions(
            account_id=1,
            state_id=1,
            state_permission=V1StatePermissionsCreateStatePermission(
                role_ids=[1],
                team_lead=False,
                project_lead=False,
            ),
        )
        """
        _response = self._raw_client.create_state_permissions(
            account_id, state_id, state_permission=state_permission, request_options=request_options
        )
        return _response.data

    def delete_state_permissions(
        self, account_id: int, state_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete all permissions for a state. Admin access required. System-managed states cannot be modified.

        Parameters
        ----------
        account_id : int
            Account ID

        state_id : int
            State ID

        id : int
            State permission ID (all permissions for the state are deleted regardless of ID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            State permissions deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.delete_state_permissions(
            account_id=1,
            state_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_state_permissions(account_id, state_id, id, request_options=request_options)
        return _response.data

    def list_states(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1State]:
        """
        Retrieve all states for the specified account, including their permissions.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1State]
            States retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.list_states(
            account_id=1,
        )
        """
        _response = self._raw_client.list_states(account_id, request_options=request_options)
        return _response.data

    def create_state(
        self, account_id: int, *, state: V1StatesCreateState, request_options: typing.Optional[RequestOptions] = None
    ) -> V1State:
        """
        Create a new state for the specified account. Only admin users can create states.

        Parameters
        ----------
        account_id : int
            Account ID

        state : V1StatesCreateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State created successfully

        Examples
        --------
        from fern import FernApi, V1StatesCreateState

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.create_state(
            account_id=1,
            state=V1StatesCreateState(
                name="New State",
                icon="star",
                color="ff0000",
                billed=True,
                locked=False,
            ),
        )
        """
        _response = self._raw_client.create_state(account_id, state=state, request_options=request_options)
        return _response.data

    def update_state(
        self,
        account_id: int,
        id: int,
        *,
        state: V1StatesUpdateState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1State:
        """
        Update an existing state. Only admin users can update states.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        state : V1StatesUpdateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State updated successfully

        Examples
        --------
        from fern import FernApi, V1StatesUpdateState

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.update_state(
            account_id=1,
            id=1,
            state=V1StatesUpdateState(
                name="Updated State",
                icon="circle",
                color="00ff00",
                billed=False,
                locked=True,
            ),
        )
        """
        _response = self._raw_client.update_state(account_id, id, state=state, request_options=request_options)
        return _response.data

    def delete_state(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a state. Only admin users can delete states and system-managed states cannot be deleted.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            State deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_states.delete_state(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_state(account_id, id, request_options=request_options)
        return _response.data


class AsyncEventStatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventStatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventStatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventStatesClient
        """
        return self._raw_client

    async def list_hour_states(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1State]:
        """
        List all available time entry states for the account.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1State]
            Time entry states list

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.list_hour_states(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_hour_states(account_id, request_options=request_options)
        return _response.data

    async def create_hour_state(
        self, account_id: int, *, state: V1StatesCreateState, request_options: typing.Optional[RequestOptions] = None
    ) -> V1State:
        """
        Create a new time entry state. Only admin users can create states.

        Parameters
        ----------
        account_id : int
            Account ID

        state : V1StatesCreateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, V1StatesCreateState

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.create_hour_state(
                account_id=1,
                state=V1StatesCreateState(
                    name="Review Required",
                    color="ff5722",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_hour_state(account_id, state=state, request_options=request_options)
        return _response.data

    async def update_hour_state(
        self,
        account_id: int,
        id: int,
        *,
        state: V1StatesUpdateState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1State:
        """
        Update an existing time entry state. Only admin users can update states.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        state : V1StatesUpdateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, V1StatesUpdateState

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.update_hour_state(
                account_id=1,
                id=1,
                state=V1StatesUpdateState(
                    name="Updated State Name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_hour_state(
            account_id, id, state=state, request_options=request_options
        )
        return _response.data

    async def delete_hour_state(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a time entry state. Only admin users can delete states and system-managed states cannot be deleted.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            State deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.delete_hour_state(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_hour_state(account_id, id, request_options=request_options)
        return _response.data

    async def create_state_permissions(
        self,
        account_id: int,
        state_id: int,
        *,
        state_permission: V1StatePermissionsCreateStatePermission,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1StatePermission]:
        """
        Create or update permissions for a state. Admin access required. System-managed states cannot be modified.

        Parameters
        ----------
        account_id : int
            Account ID

        state_id : int
            State ID

        state_permission : V1StatePermissionsCreateStatePermission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1StatePermission]
            State permissions created successfully

        Examples
        --------
        import asyncio

        from fern.event_states import V1StatePermissionsCreateStatePermission

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.create_state_permissions(
                account_id=1,
                state_id=1,
                state_permission=V1StatePermissionsCreateStatePermission(
                    role_ids=[1],
                    team_lead=False,
                    project_lead=False,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_state_permissions(
            account_id, state_id, state_permission=state_permission, request_options=request_options
        )
        return _response.data

    async def delete_state_permissions(
        self, account_id: int, state_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete all permissions for a state. Admin access required. System-managed states cannot be modified.

        Parameters
        ----------
        account_id : int
            Account ID

        state_id : int
            State ID

        id : int
            State permission ID (all permissions for the state are deleted regardless of ID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            State permissions deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.delete_state_permissions(
                account_id=1,
                state_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_state_permissions(
            account_id, state_id, id, request_options=request_options
        )
        return _response.data

    async def list_states(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1State]:
        """
        Retrieve all states for the specified account, including their permissions.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1State]
            States retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.list_states(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_states(account_id, request_options=request_options)
        return _response.data

    async def create_state(
        self, account_id: int, *, state: V1StatesCreateState, request_options: typing.Optional[RequestOptions] = None
    ) -> V1State:
        """
        Create a new state for the specified account. Only admin users can create states.

        Parameters
        ----------
        account_id : int
            Account ID

        state : V1StatesCreateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, V1StatesCreateState

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.create_state(
                account_id=1,
                state=V1StatesCreateState(
                    name="New State",
                    icon="star",
                    color="ff0000",
                    billed=True,
                    locked=False,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_state(account_id, state=state, request_options=request_options)
        return _response.data

    async def update_state(
        self,
        account_id: int,
        id: int,
        *,
        state: V1StatesUpdateState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1State:
        """
        Update an existing state. Only admin users can update states.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        state : V1StatesUpdateState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1State
            State updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, V1StatesUpdateState

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.update_state(
                account_id=1,
                id=1,
                state=V1StatesUpdateState(
                    name="Updated State",
                    icon="circle",
                    color="00ff00",
                    billed=False,
                    locked=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_state(account_id, id, state=state, request_options=request_options)
        return _response.data

    async def delete_state(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a state. Only admin users can delete states and system-managed states cannot be deleted.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            State ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            State deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_states.delete_state(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_state(account_id, id, request_options=request_options)
        return _response.data
