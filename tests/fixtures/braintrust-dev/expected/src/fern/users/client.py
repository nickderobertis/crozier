

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.starting_after import StartingAfter
from ..types.user import User
from ..types.user_email import UserEmail
from ..types.user_family_name import UserFamilyName
from ..types.user_given_name import UserGivenName
from ..types.user_id_param import UserIdParam
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.get_user_response import GetUserResponse


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

    def get_user(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        given_name: typing.Optional[UserGivenName] = None,
        family_name: typing.Optional[UserFamilyName] = None,
        email: typing.Optional[UserEmail] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserResponse:
        """
        List out all users. The users are sorted by creation date, with the most recently-created users coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        given_name : typing.Optional[UserGivenName]
            Given name of the user to search for. You may pass the param multiple times to filter for more than one given name

        family_name : typing.Optional[UserFamilyName]
            Family name of the user to search for. You may pass the param multiple times to filter for more than one family name

        email : typing.Optional[UserEmail]
            Email of the user to search for. You may pass the param multiple times to filter for more than one email

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserResponse
            Returns a list of user objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_user()
        """
        _response = self._raw_client.get_user(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            given_name=given_name,
            family_name=family_name,
            email=email,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def get_user_id(self, user_id: UserIdParam, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get a user object by its id

        Parameters
        ----------
        user_id : UserIdParam
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Returns the user object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_user_id(
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_user_id(user_id, request_options=request_options)
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

    async def get_user(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        given_name: typing.Optional[UserGivenName] = None,
        family_name: typing.Optional[UserFamilyName] = None,
        email: typing.Optional[UserEmail] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserResponse:
        """
        List out all users. The users are sorted by creation date, with the most recently-created users coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        given_name : typing.Optional[UserGivenName]
            Given name of the user to search for. You may pass the param multiple times to filter for more than one given name

        family_name : typing.Optional[UserFamilyName]
            Family name of the user to search for. You may pass the param multiple times to filter for more than one family name

        email : typing.Optional[UserEmail]
            Email of the user to search for. You may pass the param multiple times to filter for more than one email

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserResponse
            Returns a list of user objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            given_name=given_name,
            family_name=family_name,
            email=email,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def get_user_id(
        self, user_id: UserIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Get a user object by its id

        Parameters
        ----------
        user_id : UserIdParam
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Returns the user object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_user_id(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_id(user_id, request_options=request_options)
        return _response.data
