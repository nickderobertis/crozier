

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.description_safe_str import DescriptionSafeStr
from ..types.envelope_dict_str_any import EnvelopeDictStrAny
from ..types.envelope_group_get import EnvelopeGroupGet
from ..types.envelope_group_user_get import EnvelopeGroupUserGet
from ..types.envelope_list_group_user_get import EnvelopeListGroupUserGet
from ..types.envelope_list_resource_hit import EnvelopeListResourceHit
from ..types.envelope_my_groups_get import EnvelopeMyGroupsGet
from ..types.envelope_research_resource import EnvelopeResearchResource
from ..types.group_access_rights import GroupAccessRights
from ..types.group_id_int import GroupIdInt
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.name_safe_str import NameSafeStr
from ..types.user_id_int import UserIdInt
from ..types.user_name_safe_id import UserNameSafeId
from .raw_client import AsyncRawGroupsClient, RawGroupsClient
from .types.get_group_classifiers_request_tree_view import GetGroupClassifiersRequestTreeView


OMIT = typing.cast(typing.Any, ...)


class GroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroupsClient
        """
        return self._raw_client

    def list_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeMyGroupsGet:
        """
        List all groups (organizations, primary, everyone and products) I belong to

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyGroupsGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.list_groups()
        """
        _response = self._raw_client.list_groups(request_options=request_options)
        return _response.data

    def create_group(
        self,
        *,
        label: NameSafeStr,
        description: DescriptionSafeStr,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGroupGet:
        """
        Creates an organization group

        Parameters
        ----------
        label : NameSafeStr

        description : DescriptionSafeStr

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.create_group(
            label="label",
            description="description",
        )
        """
        _response = self._raw_client.create_group(
            label=label, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    def get_group(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGroupGet:
        """
        Get an organization group

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.get_group(
            gid=1,
        )
        """
        _response = self._raw_client.get_group(gid, request_options=request_options)
        return _response.data

    def delete_group(self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes organization groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.delete_group(
            gid=1,
        )
        """
        _response = self._raw_client.delete_group(gid, request_options=request_options)
        return _response.data

    def update_group(
        self,
        gid: GroupIdInt,
        *,
        label: typing.Optional[NameSafeStr] = OMIT,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGroupGet:
        """
        Updates organization groups

        Parameters
        ----------
        gid : GroupIdInt

        label : typing.Optional[NameSafeStr]

        description : typing.Optional[DescriptionSafeStr]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.update_group(
            gid=1,
        )
        """
        _response = self._raw_client.update_group(
            gid, label=label, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    def get_all_group_users(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListGroupUserGet:
        """
        Gets users in organization or primary groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListGroupUserGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.get_all_group_users(
            gid=1,
        )
        """
        _response = self._raw_client.get_all_group_users(gid, request_options=request_options)
        return _response.data

    def add_group_user(
        self,
        gid: GroupIdInt,
        *,
        uid: typing.Optional[UserIdInt] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        email: typing.Optional[LowerCaseEmailStr] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a user to an organization group using their username, user ID, or email (subject to privacy settings)

        Parameters
        ----------
        gid : GroupIdInt

        uid : typing.Optional[UserIdInt]

        user_name : typing.Optional[UserNameSafeId]

        email : typing.Optional[LowerCaseEmailStr]
            Accessible only if the user has opted to share their email in privacy settings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.add_group_user(
            gid=1,
        )
        """
        _response = self._raw_client.add_group_user(
            gid, uid=uid, user_name=user_name, email=email, request_options=request_options
        )
        return _response.data

    def get_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGroupUserGet:
        """
        Gets specific user in an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupUserGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.get_group_user(
            gid=1,
            uid=1,
        )
        """
        _response = self._raw_client.get_group_user(gid, uid, request_options=request_options)
        return _response.data

    def delete_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a user from an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.delete_group_user(
            gid=1,
            uid=1,
        )
        """
        _response = self._raw_client.delete_group_user(gid, uid, request_options=request_options)
        return _response.data

    def update_group_user(
        self,
        gid: GroupIdInt,
        uid: UserIdInt,
        *,
        access_rights: GroupAccessRights,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGroupUserGet:
        """
        Updates user (access-rights) to an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        access_rights : GroupAccessRights

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupUserGet
            Successful Response

        Examples
        --------
        from fern import FernApi, GroupAccessRights

        client = FernApi()
        client.groups.update_group_user(
            gid=1,
            uid=1,
            access_rights=GroupAccessRights(
                read=True,
                write=False,
                delete=False,
            ),
        )
        """
        _response = self._raw_client.update_group_user(
            gid, uid, access_rights=access_rights, request_options=request_options
        )
        return _response.data

    def get_group_classifiers(
        self,
        gid: GroupIdInt,
        *,
        tree_view: typing.Optional[GetGroupClassifiersRequestTreeView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeDictStrAny:
        """
        Parameters
        ----------
        gid : GroupIdInt

        tree_view : typing.Optional[GetGroupClassifiersRequestTreeView]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictStrAny
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.get_group_classifiers(
            gid=1,
        )
        """
        _response = self._raw_client.get_group_classifiers(gid, tree_view=tree_view, request_options=request_options)
        return _response.data

    def get_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeResearchResource:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeResearchResource
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.get_scicrunch_resource(
            rrid="rrid",
        )
        """
        _response = self._raw_client.get_scicrunch_resource(rrid, request_options=request_options)
        return _response.data

    def add_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeResearchResource:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeResearchResource
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.add_scicrunch_resource(
            rrid="rrid",
        )
        """
        _response = self._raw_client.add_scicrunch_resource(rrid, request_options=request_options)
        return _response.data

    def search_scicrunch_resources(
        self, *, guess_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListResourceHit:
        """
        Parameters
        ----------
        guess_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListResourceHit
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.search_scicrunch_resources(
            guess_name="guess_name",
        )
        """
        _response = self._raw_client.search_scicrunch_resources(guess_name=guess_name, request_options=request_options)
        return _response.data


class AsyncGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroupsClient
        """
        return self._raw_client

    async def list_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeMyGroupsGet:
        """
        List all groups (organizations, primary, everyone and products) I belong to

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyGroupsGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.list_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_groups(request_options=request_options)
        return _response.data

    async def create_group(
        self,
        *,
        label: NameSafeStr,
        description: DescriptionSafeStr,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGroupGet:
        """
        Creates an organization group

        Parameters
        ----------
        label : NameSafeStr

        description : DescriptionSafeStr

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.create_group(
                label="label",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_group(
            label=label, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    async def get_group(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGroupGet:
        """
        Get an organization group

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.get_group(
                gid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group(gid, request_options=request_options)
        return _response.data

    async def delete_group(self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes organization groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.delete_group(
                gid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group(gid, request_options=request_options)
        return _response.data

    async def update_group(
        self,
        gid: GroupIdInt,
        *,
        label: typing.Optional[NameSafeStr] = OMIT,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGroupGet:
        """
        Updates organization groups

        Parameters
        ----------
        gid : GroupIdInt

        label : typing.Optional[NameSafeStr]

        description : typing.Optional[DescriptionSafeStr]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.update_group(
                gid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_group(
            gid, label=label, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    async def get_all_group_users(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListGroupUserGet:
        """
        Gets users in organization or primary groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListGroupUserGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.get_all_group_users(
                gid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_group_users(gid, request_options=request_options)
        return _response.data

    async def add_group_user(
        self,
        gid: GroupIdInt,
        *,
        uid: typing.Optional[UserIdInt] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        email: typing.Optional[LowerCaseEmailStr] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a user to an organization group using their username, user ID, or email (subject to privacy settings)

        Parameters
        ----------
        gid : GroupIdInt

        uid : typing.Optional[UserIdInt]

        user_name : typing.Optional[UserNameSafeId]

        email : typing.Optional[LowerCaseEmailStr]
            Accessible only if the user has opted to share their email in privacy settings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.add_group_user(
                gid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_group_user(
            gid, uid=uid, user_name=user_name, email=email, request_options=request_options
        )
        return _response.data

    async def get_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGroupUserGet:
        """
        Gets specific user in an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupUserGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.get_group_user(
                gid=1,
                uid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_user(gid, uid, request_options=request_options)
        return _response.data

    async def delete_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a user from an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.delete_group_user(
                gid=1,
                uid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group_user(gid, uid, request_options=request_options)
        return _response.data

    async def update_group_user(
        self,
        gid: GroupIdInt,
        uid: UserIdInt,
        *,
        access_rights: GroupAccessRights,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGroupUserGet:
        """
        Updates user (access-rights) to an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        access_rights : GroupAccessRights

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGroupUserGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GroupAccessRights

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.update_group_user(
                gid=1,
                uid=1,
                access_rights=GroupAccessRights(
                    read=True,
                    write=False,
                    delete=False,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_group_user(
            gid, uid, access_rights=access_rights, request_options=request_options
        )
        return _response.data

    async def get_group_classifiers(
        self,
        gid: GroupIdInt,
        *,
        tree_view: typing.Optional[GetGroupClassifiersRequestTreeView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeDictStrAny:
        """
        Parameters
        ----------
        gid : GroupIdInt

        tree_view : typing.Optional[GetGroupClassifiersRequestTreeView]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictStrAny
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.get_group_classifiers(
                gid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_classifiers(
            gid, tree_view=tree_view, request_options=request_options
        )
        return _response.data

    async def get_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeResearchResource:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeResearchResource
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.get_scicrunch_resource(
                rrid="rrid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_scicrunch_resource(rrid, request_options=request_options)
        return _response.data

    async def add_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeResearchResource:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeResearchResource
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.add_scicrunch_resource(
                rrid="rrid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_scicrunch_resource(rrid, request_options=request_options)
        return _response.data

    async def search_scicrunch_resources(
        self, *, guess_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListResourceHit:
        """
        Parameters
        ----------
        guess_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListResourceHit
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.search_scicrunch_resources(
                guess_name="guess_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_scicrunch_resources(
            guess_name=guess_name, request_options=request_options
        )
        return _response.data
