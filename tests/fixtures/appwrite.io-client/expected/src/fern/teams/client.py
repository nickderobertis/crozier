

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.membership import Membership
from ..types.membership_list import MembershipList
from ..types.team import Team
from ..types.team_list import TeamList
from .raw_client import AsyncRawTeamsClient, RawTeamsClient


OMIT = typing.cast(typing.Any, ...)


class TeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeamsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeamList:
        """
        Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's teams. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamList
            Teams List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.list()
        """
        _response = self._raw_client.list(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    def create(
        self,
        *,
        name: str,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.

        Parameters
        ----------
        name : str
            Team name. Max length: 128 chars.

        roles : typing.Optional[typing.Sequence[str]]
            Array of strings. Use this param to set the roles in the team for the user who created it. The default role is **owner**. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.create(
            name="name",
        )
        """
        _response = self._raw_client.create(name=name, roles=roles, request_options=request_options)
        return _response.data

    def get(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Get a team by its unique ID. All team members have read access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.get(
            team_id="teamId",
        )
        """
        _response = self._raw_client.get(team_id, request_options=request_options)
        return _response.data

    def update(self, team_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Update a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        name : str
            Team name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.update(
            team_id="teamId",
            name="name",
        )
        """
        _response = self._raw_client.update(team_id, name=name, request_options=request_options)
        return _response.data

    def delete(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.delete(
            team_id="teamId",
        )
        """
        _response = self._raw_client.delete(team_id, request_options=request_options)
        return _response.data

    def get_memberships(
        self,
        team_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MembershipList:
        """
        Get a team members by the team unique ID. All team members have read access for this list of resources.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MembershipList
            Memberships List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.get_memberships(
            team_id="teamId",
        )
        """
        _response = self._raw_client.get_memberships(
            team_id, search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    def create_membership(
        self,
        team_id: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Membership:
        """
        Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member's email address if the member doesn't exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.

        Use the 'URL' parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.

        Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL's are the once from domains you have set when added your platforms in the console interface.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        email : str
            New team member email.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        url : str
            URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        name : typing.Optional[str]
            New team member name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Membership
            Membership

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.create_membership(
            team_id="teamId",
            email="email",
            roles=["roles"],
            url="url",
        )
        """
        _response = self._raw_client.create_membership(
            team_id, email=email, roles=roles, url=url, name=name, request_options=request_options
        )
        return _response.data

    def delete_membership(
        self, team_id: str, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.delete_membership(
            team_id="teamId",
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.delete_membership(team_id, membership_id, request_options=request_options)
        return _response.data

    def update_membership_roles(
        self,
        team_id: str,
        membership_id: str,
        *,
        roles: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Membership:
        """


        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Membership
            Membership

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.update_membership_roles(
            team_id="teamId",
            membership_id="membershipId",
            roles=["roles"],
        )
        """
        _response = self._raw_client.update_membership_roles(
            team_id, membership_id, roles=roles, request_options=request_options
        )
        return _response.data

    def update_membership_status(
        self,
        team_id: str,
        membership_id: str,
        *,
        secret: str,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Membership:
        """
        Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        secret : str
            Secret key.

        user_id : str
            User unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Membership
            Membership

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.teams.update_membership_status(
            team_id="teamId",
            membership_id="membershipId",
            secret="secret",
            user_id="userId",
        )
        """
        _response = self._raw_client.update_membership_status(
            team_id, membership_id, secret=secret, user_id=user_id, request_options=request_options
        )
        return _response.data


class AsyncTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeamsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeamList:
        """
        Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's teams. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamList
            Teams List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        *,
        name: str,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.

        Parameters
        ----------
        name : str
            Team name. Max length: 128 chars.

        roles : typing.Optional[typing.Sequence[str]]
            Array of strings. Use this param to set the roles in the team for the user who created it. The default role is **owner**. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(name=name, roles=roles, request_options=request_options)
        return _response.data

    async def get(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Get a team by its unique ID. All team members have read access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.get(
                team_id="teamId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(team_id, request_options=request_options)
        return _response.data

    async def update(self, team_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Update a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        name : str
            Team name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.update(
                team_id="teamId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(team_id, name=name, request_options=request_options)
        return _response.data

    async def delete(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.delete(
                team_id="teamId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(team_id, request_options=request_options)
        return _response.data

    async def get_memberships(
        self,
        team_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MembershipList:
        """
        Get a team members by the team unique ID. All team members have read access for this list of resources.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MembershipList
            Memberships List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.get_memberships(
                team_id="teamId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_memberships(
            team_id, search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    async def create_membership(
        self,
        team_id: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Membership:
        """
        Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member's email address if the member doesn't exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.

        Use the 'URL' parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.

        Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL's are the once from domains you have set when added your platforms in the console interface.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        email : str
            New team member email.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        url : str
            URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        name : typing.Optional[str]
            New team member name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Membership
            Membership

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.create_membership(
                team_id="teamId",
                email="email",
                roles=["roles"],
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_membership(
            team_id, email=email, roles=roles, url=url, name=name, request_options=request_options
        )
        return _response.data

    async def delete_membership(
        self, team_id: str, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.delete_membership(
                team_id="teamId",
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_membership(team_id, membership_id, request_options=request_options)
        return _response.data

    async def update_membership_roles(
        self,
        team_id: str,
        membership_id: str,
        *,
        roles: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Membership:
        """


        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Membership
            Membership

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.update_membership_roles(
                team_id="teamId",
                membership_id="membershipId",
                roles=["roles"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_membership_roles(
            team_id, membership_id, roles=roles, request_options=request_options
        )
        return _response.data

    async def update_membership_status(
        self,
        team_id: str,
        membership_id: str,
        *,
        secret: str,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Membership:
        """
        Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        secret : str
            Secret key.

        user_id : str
            User unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Membership
            Membership

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.update_membership_status(
                team_id="teamId",
                membership_id="membershipId",
                secret="secret",
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_membership_status(
            team_id, membership_id, secret=secret, user_id=user_id, request_options=request_options
        )
        return _response.data
