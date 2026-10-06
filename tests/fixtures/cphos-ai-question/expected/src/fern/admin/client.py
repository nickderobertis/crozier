

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.admin_stats import AdminStats
from ..types.message_response import MessageResponse
from ..types.page_task_list_item import PageTaskListItem
from ..types.page_token_info import PageTokenInfo
from ..types.page_user_info import PageUserInfo
from ..types.token_created import TokenCreated
from ..types.user_detail import UserDetail
from ..types.user_info import UserInfo
from .raw_client import AsyncRawAdminClient, RawAdminClient
from .types.create_token_request_role import CreateTokenRequestRole


OMIT = typing.cast(typing.Any, ...)


class AdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminClient
        """
        return self._raw_client

    def list_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageUserInfo:
        """
        分页列出用户，支持模糊搜索与排序。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        q : typing.Optional[str]
            按 user_id / label 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageUserInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.list_users()
        """
        _response = self._raw_client.list_users(
            limit=limit, offset=offset, q=q, order=order, request_options=request_options
        )
        return _response.data

    def create_user(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> UserInfo:
        """
        创建一个新用户（随后可为其签发 token）。

        Parameters
        ----------
        label : typing.Optional[str]
            用户备注名（如团队 / 用途）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.create_user()
        """
        _response = self._raw_client.create_user(label=label, request_options=request_options)
        return _response.data

    def get_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UserDetail:
        """
        返回用户详情（含未吊销 token 数与任务数）。

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDetail
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.get_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    def delete_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> MessageResponse:
        """
        删除用户并级联吊销 / 删除其 token、任务记录与磁盘产物。

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.delete_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    def update_user(
        self, user_id: str, *, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserInfo:
        """
        更新指定用户的 label。

        Parameters
        ----------
        user_id : str

        label : str
            新的用户备注名。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.update_user(
            user_id="user_id",
            label="label",
        )
        """
        _response = self._raw_client.update_user(user_id, label=label, request_options=request_options)
        return _response.data

    def list_user_tasks(
        self,
        user_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTaskListItem:
        """
        查看任意用户的任务历史。

        Parameters
        ----------
        user_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTaskListItem
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.list_user_tasks(
            user_id="user_id",
        )
        """
        _response = self._raw_client.list_user_tasks(
            user_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def list_tokens(
        self,
        *,
        user_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTokenInfo:
        """
        分页列出 token 元数据（不含明文）；可按 user_id 过滤、模糊搜索与排序。

        Parameters
        ----------
        user_id : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        q : typing.Optional[str]
            按 token id / label 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTokenInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.list_tokens()
        """
        _response = self._raw_client.list_tokens(
            user_id=user_id, limit=limit, offset=offset, q=q, order=order, request_options=request_options
        )
        return _response.data

    def create_token(
        self,
        *,
        user_id: str,
        role: typing.Optional[CreateTokenRequestRole] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenCreated:
        """
        为指定用户签发一个不透明 token，明文仅此一次返回。

        Parameters
        ----------
        user_id : str
            目标用户 ID。

        role : typing.Optional[CreateTokenRequestRole]
            token 角色。

        label : typing.Optional[str]
            token 备注（如分发对象）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenCreated
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.create_token(
            user_id="user_id",
        )
        """
        _response = self._raw_client.create_token(
            user_id=user_id, role=role, label=label, request_options=request_options
        )
        return _response.data

    def revoke_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        吊销指定 token。

        Parameters
        ----------
        token_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.revoke_token(
            token_id="token_id",
        )
        """
        _response = self._raw_client.revoke_token(token_id, request_options=request_options)
        return _response.data

    def list_all_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        mode: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTaskListItem:
        """
        跨用户列出全部任务，支持状态 / 模式 / 主题过滤与排序。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]
            按状态过滤，可逗号分隔。

        mode : typing.Optional[str]
            按命题模式过滤。

        q : typing.Optional[str]
            按 topic 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTaskListItem
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.list_all_tasks()
        """
        _response = self._raw_client.list_all_tasks(
            limit=limit, offset=offset, status=status, mode=mode, q=q, order=order, request_options=request_options
        )
        return _response.data

    def get_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> AdminStats:
        """
        返回任务 / 用户 / token 计数与累计 token 用量、API 费用，供仪表盘使用。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminStats
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.admin.get_stats()
        """
        _response = self._raw_client.get_stats(request_options=request_options)
        return _response.data


class AsyncAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminClient
        """
        return self._raw_client

    async def list_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageUserInfo:
        """
        分页列出用户，支持模糊搜索与排序。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        q : typing.Optional[str]
            按 user_id / label 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageUserInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.list_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(
            limit=limit, offset=offset, q=q, order=order, request_options=request_options
        )
        return _response.data

    async def create_user(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> UserInfo:
        """
        创建一个新用户（随后可为其签发 token）。

        Parameters
        ----------
        label : typing.Optional[str]
            用户备注名（如团队 / 用途）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.create_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(label=label, request_options=request_options)
        return _response.data

    async def get_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UserDetail:
        """
        返回用户详情（含未吊销 token 数与任务数）。

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDetail
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.get_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    async def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        删除用户并级联吊销 / 删除其 token、任务记录与磁盘产物。

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.delete_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    async def update_user(
        self, user_id: str, *, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserInfo:
        """
        更新指定用户的 label。

        Parameters
        ----------
        user_id : str

        label : str
            新的用户备注名。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.update_user(
                user_id="user_id",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(user_id, label=label, request_options=request_options)
        return _response.data

    async def list_user_tasks(
        self,
        user_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTaskListItem:
        """
        查看任意用户的任务历史。

        Parameters
        ----------
        user_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTaskListItem
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.list_user_tasks(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_tasks(
            user_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def list_tokens(
        self,
        *,
        user_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTokenInfo:
        """
        分页列出 token 元数据（不含明文）；可按 user_id 过滤、模糊搜索与排序。

        Parameters
        ----------
        user_id : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        q : typing.Optional[str]
            按 token id / label 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTokenInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.list_tokens()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tokens(
            user_id=user_id, limit=limit, offset=offset, q=q, order=order, request_options=request_options
        )
        return _response.data

    async def create_token(
        self,
        *,
        user_id: str,
        role: typing.Optional[CreateTokenRequestRole] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenCreated:
        """
        为指定用户签发一个不透明 token，明文仅此一次返回。

        Parameters
        ----------
        user_id : str
            目标用户 ID。

        role : typing.Optional[CreateTokenRequestRole]
            token 角色。

        label : typing.Optional[str]
            token 备注（如分发对象）。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenCreated
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.create_token(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_token(
            user_id=user_id, role=role, label=label, request_options=request_options
        )
        return _response.data

    async def revoke_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        吊销指定 token。

        Parameters
        ----------
        token_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.revoke_token(
                token_id="token_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_token(token_id, request_options=request_options)
        return _response.data

    async def list_all_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        mode: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageTaskListItem:
        """
        跨用户列出全部任务，支持状态 / 模式 / 主题过滤与排序。

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]
            按状态过滤，可逗号分隔。

        mode : typing.Optional[str]
            按命题模式过滤。

        q : typing.Optional[str]
            按 topic 模糊搜索。

        order : typing.Optional[str]
            按创建时间排序：ASC / DESC。

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageTaskListItem
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.list_all_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_tasks(
            limit=limit, offset=offset, status=status, mode=mode, q=q, order=order, request_options=request_options
        )
        return _response.data

    async def get_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> AdminStats:
        """
        返回任务 / 用户 / token 计数与累计 token 用量、API 费用，供仪表盘使用。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminStats
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.admin.get_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stats(request_options=request_options)
        return _response.data
