

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_envelope import ListEnvelope
from ..types.list_list import ListList
from ..types.sync_result import SyncResult
from .raw_client import AsyncRawListsClient, RawListsClient


OMIT = typing.cast(typing.Any, ...)


class ListsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawListsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawListsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawListsClient
        """
        return self._raw_client

    def alle_lijsten_opvragen(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListList:
        """
        All lists in an array of list objects. The list objects have been ordered in an array with the name 'data'. No parameters need to be provided.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListList
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.lists.alle_lijsten_opvragen()
        """
        _response = self._raw_client.alle_lijsten_opvragen(request_options=request_options)
        return _response.data

    def lijst_toevoegen(
        self,
        *,
        name: str,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. You may use these in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        name : str
            Name given to the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.lists.lijst_toevoegen(
            name="Nieuwsbrief",
        )
        """
        _response = self._raw_client.lijst_toevoegen(
            name=name,
            locked=locked,
            remarks=remarks,
            subscribe_notification_email=subscribe_notification_email,
            unsubscribe_notification_email=unsubscribe_notification_email,
            request_options=request_options,
        )
        return _response.data

    def lijst_opvragen(self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ListEnvelope:
        """
        All information about a list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.lists.lijst_opvragen(
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.lijst_opvragen(list_id, request_options=request_options)
        return _response.data

    def lijst_wijzigen(
        self,
        list_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEnvelope:
        """
        You will only have to include the fields that need to be modified in the application. Fields that are not mentioned will keep their current value. As soon as a field is mentioned, it is checked and may therefore cause an error message. A code is displayed with this error message. You may use this code in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            A name for the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.lists.lijst_wijzigen(
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.lijst_wijzigen(
            list_id,
            name=name,
            locked=locked,
            remarks=remarks,
            subscribe_notification_email=subscribe_notification_email,
            unsubscribe_notification_email=unsubscribe_notification_email,
            request_options=request_options,
        )
        return _response.data

    def lijst_verwijderen(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEnvelope:
        """
        This permanently deletes a list. If the list does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.lists.lijst_verwijderen(
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.lijst_verwijderen(list_id, request_options=request_options)
        return _response.data

    def lijst_synchroniseren_bulk(
        self,
        list_id: str,
        *,
        actions: str,
        members: typing.Dict[str, typing.Any],
        member_id: str,
        email: str,
        custom_fields: typing.Dict[str, typing.Any],
        mode_verouderd: typing.Optional[str] = OMIT,
        source_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncResult:
        """
        Adds, updates or unsubscribes multiple subscribers in one request. This endpoint is off by default: an account without access gets a 401 with the message "Not permitted to issue bulk requests (1)". Contact Laposta to have it enabled for your account.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        actions : str
            An array with at least one of the following options: add, update, or unsubscribe_excluded. These determine whether members may be added, updated and/or unsubscribed (read details below).

        members : typing.Dict[str, typing.Any]
            An array with member objects. A minimum of 1, maximum of 500,000.

        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        email : str
            The email address of the relation to be changed or added. If the member_id is also specified, then a new email address can be specified here for the existing relation.

        custom_fields : typing.Dict[str, typing.Any]
            A JSON object where the key is the name of the extra field and the value is the value of the extra field.

        mode_verouderd : typing.Optional[str]
            For backwards compatibility you can still pass edit, add or add_and_edit, but this parameter is being phased out. Do not send mode together with actions.

        source_url : typing.Optional[str]
            The URL from which the relation was registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncResult
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.lists.lijst_synchroniseren_bulk(
            list_id="BaImMu3JZA",
            actions="string",
            members={"key": "value"},
            member_id="ZKfjhLJHfl",
            email="relatie@example.net",
            custom_fields={"key": "value"},
        )
        """
        _response = self._raw_client.lijst_synchroniseren_bulk(
            list_id,
            actions=actions,
            members=members,
            member_id=member_id,
            email=email,
            custom_fields=custom_fields,
            mode_verouderd=mode_verouderd,
            source_url=source_url,
            request_options=request_options,
        )
        return _response.data

    def lijst_leegmaken(self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ListEnvelope:
        """
        This permanently purges all active subscribers from a list, but doesn't delete the list itself. If the list does not exist, an error message is displayed. In response, you are shown another list object.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.lists.lijst_leegmaken(
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.lijst_leegmaken(list_id, request_options=request_options)
        return _response.data


class AsyncListsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawListsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawListsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawListsClient
        """
        return self._raw_client

    async def alle_lijsten_opvragen(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListList:
        """
        All lists in an array of list objects. The list objects have been ordered in an array with the name 'data'. No parameters need to be provided.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListList
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.lists.alle_lijsten_opvragen()


        asyncio.run(main())
        """
        _response = await self._raw_client.alle_lijsten_opvragen(request_options=request_options)
        return _response.data

    async def lijst_toevoegen(
        self,
        *,
        name: str,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. You may use these in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        name : str
            Name given to the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.lists.lijst_toevoegen(
                name="Nieuwsbrief",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lijst_toevoegen(
            name=name,
            locked=locked,
            remarks=remarks,
            subscribe_notification_email=subscribe_notification_email,
            unsubscribe_notification_email=unsubscribe_notification_email,
            request_options=request_options,
        )
        return _response.data

    async def lijst_opvragen(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEnvelope:
        """
        All information about a list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.lists.lijst_opvragen(
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lijst_opvragen(list_id, request_options=request_options)
        return _response.data

    async def lijst_wijzigen(
        self,
        list_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEnvelope:
        """
        You will only have to include the fields that need to be modified in the application. Fields that are not mentioned will keep their current value. As soon as a field is mentioned, it is checked and may therefore cause an error message. A code is displayed with this error message. You may use this code in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            A name for the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.lists.lijst_wijzigen(
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lijst_wijzigen(
            list_id,
            name=name,
            locked=locked,
            remarks=remarks,
            subscribe_notification_email=subscribe_notification_email,
            unsubscribe_notification_email=unsubscribe_notification_email,
            request_options=request_options,
        )
        return _response.data

    async def lijst_verwijderen(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEnvelope:
        """
        This permanently deletes a list. If the list does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.lists.lijst_verwijderen(
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lijst_verwijderen(list_id, request_options=request_options)
        return _response.data

    async def lijst_synchroniseren_bulk(
        self,
        list_id: str,
        *,
        actions: str,
        members: typing.Dict[str, typing.Any],
        member_id: str,
        email: str,
        custom_fields: typing.Dict[str, typing.Any],
        mode_verouderd: typing.Optional[str] = OMIT,
        source_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncResult:
        """
        Adds, updates or unsubscribes multiple subscribers in one request. This endpoint is off by default: an account without access gets a 401 with the message "Not permitted to issue bulk requests (1)". Contact Laposta to have it enabled for your account.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        actions : str
            An array with at least one of the following options: add, update, or unsubscribe_excluded. These determine whether members may be added, updated and/or unsubscribed (read details below).

        members : typing.Dict[str, typing.Any]
            An array with member objects. A minimum of 1, maximum of 500,000.

        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        email : str
            The email address of the relation to be changed or added. If the member_id is also specified, then a new email address can be specified here for the existing relation.

        custom_fields : typing.Dict[str, typing.Any]
            A JSON object where the key is the name of the extra field and the value is the value of the extra field.

        mode_verouderd : typing.Optional[str]
            For backwards compatibility you can still pass edit, add or add_and_edit, but this parameter is being phased out. Do not send mode together with actions.

        source_url : typing.Optional[str]
            The URL from which the relation was registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncResult
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.lists.lijst_synchroniseren_bulk(
                list_id="BaImMu3JZA",
                actions="string",
                members={"key": "value"},
                member_id="ZKfjhLJHfl",
                email="relatie@example.net",
                custom_fields={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lijst_synchroniseren_bulk(
            list_id,
            actions=actions,
            members=members,
            member_id=member_id,
            email=email,
            custom_fields=custom_fields,
            mode_verouderd=mode_verouderd,
            source_url=source_url,
            request_options=request_options,
        )
        return _response.data

    async def lijst_leegmaken(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEnvelope:
        """
        This permanently purges all active subscribers from a list, but doesn't delete the list itself. If the list does not exist, an error message is displayed. In response, you are shown another list object.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.lists.lijst_leegmaken(
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lijst_leegmaken(list_id, request_options=request_options)
        return _response.data
