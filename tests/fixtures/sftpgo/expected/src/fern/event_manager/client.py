

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.base_event_action import BaseEventAction
from ..types.base_event_action_options import BaseEventActionOptions
from ..types.event_action_minimal import EventActionMinimal
from ..types.event_action_types import EventActionTypes
from ..types.event_conditions import EventConditions
from ..types.event_rule import EventRule
from ..types.event_trigger_types import EventTriggerTypes
from .raw_client import AsyncRawEventManagerClient, RawEventManagerClient
from .types.get_event_actons_request_order import GetEventActonsRequestOrder
from .types.get_event_rules_request_order import GetEventRulesRequestOrder


OMIT = typing.cast(typing.Any, ...)


class EventManagerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventManagerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventManagerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventManagerClient
        """
        return self._raw_client

    def get_event_actons(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetEventActonsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BaseEventAction]:
        """
        Returns an array with one or more event actions

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetEventActonsRequestOrder]
            Ordering actions by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BaseEventAction]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.get_event_actons()
        """
        _response = self._raw_client.get_event_actons(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_event_action(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[EventActionTypes] = OMIT,
        options: typing.Optional[BaseEventActionOptions] = OMIT,
        rules: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseEventAction:
        """
        Adds a new event actions

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        description : typing.Optional[str]
            optional description

        type : typing.Optional[EventActionTypes]

        options : typing.Optional[BaseEventActionOptions]

        rules : typing.Optional[typing.Sequence[str]]
            list of event rules names associated with this action

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseEventAction
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.add_event_action()
        """
        _response = self._raw_client.add_event_action(
            confidential_data=confidential_data,
            id=id,
            name=name,
            description=description,
            type=type,
            options=options,
            rules=rules,
            request_options=request_options,
        )
        return _response.data

    def get_event_action_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseEventAction:
        """
        Returns the event action with the given name if it exists.

        Parameters
        ----------
        name : str
            action name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseEventAction
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.get_event_action_by_name(
            name="name",
        )
        """
        _response = self._raw_client.get_event_action_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    def update_event_action(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[EventActionTypes] = OMIT,
        options: typing.Optional[BaseEventActionOptions] = OMIT,
        rules: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing event action

        Parameters
        ----------
        name_ : str
            action name

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        description : typing.Optional[str]
            optional description

        type : typing.Optional[EventActionTypes]

        options : typing.Optional[BaseEventActionOptions]

        rules : typing.Optional[typing.Sequence[str]]
            list of event rules names associated with this action

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.update_event_action(
            name_="name",
        )
        """
        _response = self._raw_client.update_event_action(
            name_,
            id=id,
            name=name,
            description=description,
            type=type,
            options=options,
            rules=rules,
            request_options=request_options,
        )
        return _response.data

    def delete_event_action(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing event action

        Parameters
        ----------
        name : str
            action name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.delete_event_action(
            name="name",
        )
        """
        _response = self._raw_client.delete_event_action(name, request_options=request_options)
        return _response.data

    def get_event_rules(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetEventRulesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EventRule]:
        """
        Returns an array with one or more event rules

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetEventRulesRequestOrder]
            Ordering rules by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventRule]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.get_event_rules()
        """
        _response = self._raw_client.get_event_rules(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_event_rule(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        actions: typing.Optional[typing.Sequence[EventActionMinimal]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        trigger: typing.Optional[EventTriggerTypes] = OMIT,
        conditions: typing.Optional[EventConditions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventRule:
        """
        Adds a new event rule

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        actions : typing.Optional[typing.Sequence[EventActionMinimal]]

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        status : typing.Optional[int]
            status:
              * `0` disabled
              * `1` enabled

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

        trigger : typing.Optional[EventTriggerTypes]

        conditions : typing.Optional[EventConditions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRule
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.add_event_rule()
        """
        _response = self._raw_client.add_event_rule(
            confidential_data=confidential_data,
            actions=actions,
            id=id,
            name=name,
            status=status,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            trigger=trigger,
            conditions=conditions,
            request_options=request_options,
        )
        return _response.data

    def get_event_rile_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventRule:
        """
        Returns the event rule with the given name if it exists.

        Parameters
        ----------
        name : str
            rule name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRule
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.get_event_rile_by_name(
            name="name",
        )
        """
        _response = self._raw_client.get_event_rile_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    def update_event_rule(
        self,
        name_: str,
        *,
        actions: typing.Optional[typing.Sequence[EventActionMinimal]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        trigger: typing.Optional[EventTriggerTypes] = OMIT,
        conditions: typing.Optional[EventConditions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing event rule

        Parameters
        ----------
        name_ : str
            rule name

        actions : typing.Optional[typing.Sequence[EventActionMinimal]]

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        status : typing.Optional[int]
            status:
              * `0` disabled
              * `1` enabled

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

        trigger : typing.Optional[EventTriggerTypes]

        conditions : typing.Optional[EventConditions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.update_event_rule(
            name_="name",
        )
        """
        _response = self._raw_client.update_event_rule(
            name_,
            actions=actions,
            id=id,
            name=name,
            status=status,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            trigger=trigger,
            conditions=conditions,
            request_options=request_options,
        )
        return _response.data

    def delete_event_rule(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing event rule

        Parameters
        ----------
        name : str
            rule name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.delete_event_rule(
            name="name",
        )
        """
        _response = self._raw_client.delete_event_rule(name, request_options=request_options)
        return _response.data

    def run_event_rule(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        The rule's actions will run in background. SFTPGo will not monitor any concurrency and such. If you want to be notified at the end of the execution please add an appropriate action

        Parameters
        ----------
        name : str
            on-demand rule name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_manager.run_event_rule(
            name="name",
        )
        """
        _response = self._raw_client.run_event_rule(name, request_options=request_options)
        return _response.data


class AsyncEventManagerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventManagerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventManagerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventManagerClient
        """
        return self._raw_client

    async def get_event_actons(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetEventActonsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BaseEventAction]:
        """
        Returns an array with one or more event actions

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetEventActonsRequestOrder]
            Ordering actions by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BaseEventAction]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.get_event_actons()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event_actons(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_event_action(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[EventActionTypes] = OMIT,
        options: typing.Optional[BaseEventActionOptions] = OMIT,
        rules: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseEventAction:
        """
        Adds a new event actions

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        description : typing.Optional[str]
            optional description

        type : typing.Optional[EventActionTypes]

        options : typing.Optional[BaseEventActionOptions]

        rules : typing.Optional[typing.Sequence[str]]
            list of event rules names associated with this action

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseEventAction
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.add_event_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_event_action(
            confidential_data=confidential_data,
            id=id,
            name=name,
            description=description,
            type=type,
            options=options,
            rules=rules,
            request_options=request_options,
        )
        return _response.data

    async def get_event_action_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseEventAction:
        """
        Returns the event action with the given name if it exists.

        Parameters
        ----------
        name : str
            action name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseEventAction
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.get_event_action_by_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event_action_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    async def update_event_action(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[EventActionTypes] = OMIT,
        options: typing.Optional[BaseEventActionOptions] = OMIT,
        rules: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing event action

        Parameters
        ----------
        name_ : str
            action name

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        description : typing.Optional[str]
            optional description

        type : typing.Optional[EventActionTypes]

        options : typing.Optional[BaseEventActionOptions]

        rules : typing.Optional[typing.Sequence[str]]
            list of event rules names associated with this action

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.update_event_action(
                name_="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_event_action(
            name_,
            id=id,
            name=name,
            description=description,
            type=type,
            options=options,
            rules=rules,
            request_options=request_options,
        )
        return _response.data

    async def delete_event_action(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Deletes an existing event action

        Parameters
        ----------
        name : str
            action name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.delete_event_action(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_event_action(name, request_options=request_options)
        return _response.data

    async def get_event_rules(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetEventRulesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EventRule]:
        """
        Returns an array with one or more event rules

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetEventRulesRequestOrder]
            Ordering rules by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventRule]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.get_event_rules()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event_rules(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_event_rule(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        actions: typing.Optional[typing.Sequence[EventActionMinimal]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        trigger: typing.Optional[EventTriggerTypes] = OMIT,
        conditions: typing.Optional[EventConditions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventRule:
        """
        Adds a new event rule

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        actions : typing.Optional[typing.Sequence[EventActionMinimal]]

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        status : typing.Optional[int]
            status:
              * `0` disabled
              * `1` enabled

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

        trigger : typing.Optional[EventTriggerTypes]

        conditions : typing.Optional[EventConditions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRule
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.add_event_rule()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_event_rule(
            confidential_data=confidential_data,
            actions=actions,
            id=id,
            name=name,
            status=status,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            trigger=trigger,
            conditions=conditions,
            request_options=request_options,
        )
        return _response.data

    async def get_event_rile_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventRule:
        """
        Returns the event rule with the given name if it exists.

        Parameters
        ----------
        name : str
            rule name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRule
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.get_event_rile_by_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event_rile_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    async def update_event_rule(
        self,
        name_: str,
        *,
        actions: typing.Optional[typing.Sequence[EventActionMinimal]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        trigger: typing.Optional[EventTriggerTypes] = OMIT,
        conditions: typing.Optional[EventConditions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing event rule

        Parameters
        ----------
        name_ : str
            rule name

        actions : typing.Optional[typing.Sequence[EventActionMinimal]]

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name

        status : typing.Optional[int]
            status:
              * `0` disabled
              * `1` enabled

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

        trigger : typing.Optional[EventTriggerTypes]

        conditions : typing.Optional[EventConditions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.update_event_rule(
                name_="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_event_rule(
            name_,
            actions=actions,
            id=id,
            name=name,
            status=status,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            trigger=trigger,
            conditions=conditions,
            request_options=request_options,
        )
        return _response.data

    async def delete_event_rule(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Deletes an existing event rule

        Parameters
        ----------
        name : str
            rule name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.delete_event_rule(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_event_rule(name, request_options=request_options)
        return _response.data

    async def run_event_rule(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        The rule's actions will run in background. SFTPGo will not monitor any concurrency and such. If you want to be notified at the end of the execution please add an appropriate action

        Parameters
        ----------
        name : str
            on-demand rule name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_manager.run_event_rule(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_event_rule(name, request_options=request_options)
        return _response.data
