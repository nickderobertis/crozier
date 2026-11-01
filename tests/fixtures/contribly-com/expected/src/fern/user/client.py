

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.linked_profile import LinkedProfile
from ..types.user import User
from .raw_client import AsyncRawUserClient, RawUserClient


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def list_users(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        minimum_contributions: typing.Optional[float] = None,
        linked_profile: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        submitted_before: typing.Optional[dt.datetime] = None,
        submitted_after: typing.Optional[dt.datetime] = None,
        username: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to the users who have contributed to this assignment.

        country : typing.Optional[str]
            Restrict results to the users who have submitted a contribution with a public location located within this country.

        minimum_contributions : typing.Optional[float]
            Restrict results to the users who have submitted at least this many contributions.

        linked_profile : typing.Optional[str]
            Restrict results to the users who a linked profile of this type.

        owned_by : typing.Optional[str]
            Restrict results to the users who are owned by of this owner.

        submitted_before : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution before this date time.

        submitted_after : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution after this date time.

        username : typing.Optional[str]
            Restrict results to the user with this username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            A list of users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.list_users()
        """
        _response = self._raw_client.list_users(
            assignment=assignment,
            country=country,
            minimum_contributions=minimum_contributions,
            linked_profile=linked_profile,
            owned_by=owned_by,
            submitted_before=submitted_before,
            submitted_after=submitted_after,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def retrieve_a_single_user_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.retrieve_a_single_user_by_id(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_a_single_user_by_id(id, request_options=request_options)
        return _response.data

    def retrieve_a_users_linked_profile_by_type(
        self, id: str, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LinkedProfile:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        type : str
            Type of the linked profile to fetch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkedProfile
            Successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.retrieve_a_users_linked_profile_by_type(
            id="id",
            type="type",
        )
        """
        _response = self._raw_client.retrieve_a_users_linked_profile_by_type(id, type, request_options=request_options)
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def list_users(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        minimum_contributions: typing.Optional[float] = None,
        linked_profile: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        submitted_before: typing.Optional[dt.datetime] = None,
        submitted_after: typing.Optional[dt.datetime] = None,
        username: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to the users who have contributed to this assignment.

        country : typing.Optional[str]
            Restrict results to the users who have submitted a contribution with a public location located within this country.

        minimum_contributions : typing.Optional[float]
            Restrict results to the users who have submitted at least this many contributions.

        linked_profile : typing.Optional[str]
            Restrict results to the users who a linked profile of this type.

        owned_by : typing.Optional[str]
            Restrict results to the users who are owned by of this owner.

        submitted_before : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution before this date time.

        submitted_after : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution after this date time.

        username : typing.Optional[str]
            Restrict results to the user with this username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            A list of users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.list_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(
            assignment=assignment,
            country=country,
            minimum_contributions=minimum_contributions,
            linked_profile=linked_profile,
            owned_by=owned_by,
            submitted_before=submitted_before,
            submitted_after=submitted_after,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_a_single_user_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.retrieve_a_single_user_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_single_user_by_id(id, request_options=request_options)
        return _response.data

    async def retrieve_a_users_linked_profile_by_type(
        self, id: str, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LinkedProfile:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        type : str
            Type of the linked profile to fetch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkedProfile
            Successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.retrieve_a_users_linked_profile_by_type(
                id="id",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_users_linked_profile_by_type(
            id, type, request_options=request_options
        )
        return _response.data
