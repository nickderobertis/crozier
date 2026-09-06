

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.env_var import EnvVar
from ..types.env_var_id_param import EnvVarIdParam
from ..types.env_var_name import EnvVarName
from ..types.env_var_object_id import EnvVarObjectId
from ..types.env_var_object_type import EnvVarObjectType
from ..types.ids import Ids
from .raw_client import AsyncRawEnvVarsClient, RawEnvVarsClient
from .types.get_env_var_response import GetEnvVarResponse
from .types.post_env_var_request_object_type import PostEnvVarRequestObjectType
from .types.put_env_var_request_object_type import PutEnvVarRequestObjectType


OMIT = typing.cast(typing.Any, ...)


class EnvVarsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnvVarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnvVarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnvVarsClient
        """
        return self._raw_client

    def get_env_var(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        env_var_name: typing.Optional[EnvVarName] = None,
        object_type: typing.Optional[EnvVarObjectType] = None,
        object_id: typing.Optional[EnvVarObjectId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEnvVarResponse:
        """
        List out all env_vars. The env_vars are sorted by creation date, with the most recently-created env_vars coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        env_var_name : typing.Optional[EnvVarName]
            Name of the env_var to search for

        object_type : typing.Optional[EnvVarObjectType]
            The type of the object the environment variable is scoped for

        object_id : typing.Optional[EnvVarObjectId]
            The id of the object the environment variable is scoped for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEnvVarResponse
            Returns a list of env_var objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_vars.get_env_var()
        """
        _response = self._raw_client.get_env_var(
            limit=limit,
            ids=ids,
            env_var_name=env_var_name,
            object_type=object_type,
            object_id=object_id,
            request_options=request_options,
        )
        return _response.data

    def post_env_var(
        self,
        *,
        object_type: PostEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvVar:
        """
        Create a new env_var. If there is an existing env_var with the same name as the one specified in the request, will return the existing env_var unmodified

        Parameters
        ----------
        object_type : PostEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the new env_var object

        Examples
        --------
        from fern.env_vars import PostEnvVarRequestObjectType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_vars.post_env_var(
            object_type=PostEnvVarRequestObjectType.ORGANIZATION,
            object_id="object_id",
            name="name",
        )
        """
        _response = self._raw_client.post_env_var(
            object_type=object_type,
            object_id=object_id,
            name=name,
            value=value,
            metadata=metadata,
            secret_type=secret_type,
            request_options=request_options,
        )
        return _response.data

    def put_env_var(
        self,
        *,
        object_type: PutEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvVar:
        """
        Create or replace env_var. If there is an existing env_var with the same name as the one specified in the request, will replace the existing env_var with the provided fields

        Parameters
        ----------
        object_type : PutEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the new env_var object

        Examples
        --------
        from fern.env_vars import PutEnvVarRequestObjectType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_vars.put_env_var(
            object_type=PutEnvVarRequestObjectType.ORGANIZATION,
            object_id="object_id",
            name="name",
        )
        """
        _response = self._raw_client.put_env_var(
            object_type=object_type,
            object_id=object_id,
            name=name,
            value=value,
            metadata=metadata,
            secret_type=secret_type,
            request_options=request_options,
        )
        return _response.data

    def get_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvVar:
        """
        Get an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the env_var object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_vars.get_env_var_id(
            env_var_id="env_var_id",
        )
        """
        _response = self._raw_client.get_env_var_id(env_var_id, request_options=request_options)
        return _response.data

    def delete_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvVar:
        """
        Delete an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the deleted env_var object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_vars.delete_env_var_id(
            env_var_id="env_var_id",
        )
        """
        _response = self._raw_client.delete_env_var_id(env_var_id, request_options=request_options)
        return _response.data

    def patch_env_var_id(
        self,
        env_var_id: EnvVarIdParam,
        *,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvVar:
        """
        Partially update an env_var object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the env_var object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.env_vars.patch_env_var_id(
            env_var_id="env_var_id",
            name="name",
        )
        """
        _response = self._raw_client.patch_env_var_id(
            env_var_id,
            name=name,
            value=value,
            metadata=metadata,
            secret_type=secret_type,
            request_options=request_options,
        )
        return _response.data


class AsyncEnvVarsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnvVarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnvVarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnvVarsClient
        """
        return self._raw_client

    async def get_env_var(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        env_var_name: typing.Optional[EnvVarName] = None,
        object_type: typing.Optional[EnvVarObjectType] = None,
        object_id: typing.Optional[EnvVarObjectId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEnvVarResponse:
        """
        List out all env_vars. The env_vars are sorted by creation date, with the most recently-created env_vars coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        env_var_name : typing.Optional[EnvVarName]
            Name of the env_var to search for

        object_type : typing.Optional[EnvVarObjectType]
            The type of the object the environment variable is scoped for

        object_id : typing.Optional[EnvVarObjectId]
            The id of the object the environment variable is scoped for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEnvVarResponse
            Returns a list of env_var objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_vars.get_env_var()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_env_var(
            limit=limit,
            ids=ids,
            env_var_name=env_var_name,
            object_type=object_type,
            object_id=object_id,
            request_options=request_options,
        )
        return _response.data

    async def post_env_var(
        self,
        *,
        object_type: PostEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvVar:
        """
        Create a new env_var. If there is an existing env_var with the same name as the one specified in the request, will return the existing env_var unmodified

        Parameters
        ----------
        object_type : PostEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the new env_var object

        Examples
        --------
        import asyncio

        from fern.env_vars import PostEnvVarRequestObjectType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_vars.post_env_var(
                object_type=PostEnvVarRequestObjectType.ORGANIZATION,
                object_id="object_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_env_var(
            object_type=object_type,
            object_id=object_id,
            name=name,
            value=value,
            metadata=metadata,
            secret_type=secret_type,
            request_options=request_options,
        )
        return _response.data

    async def put_env_var(
        self,
        *,
        object_type: PutEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvVar:
        """
        Create or replace env_var. If there is an existing env_var with the same name as the one specified in the request, will replace the existing env_var with the provided fields

        Parameters
        ----------
        object_type : PutEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the new env_var object

        Examples
        --------
        import asyncio

        from fern.env_vars import PutEnvVarRequestObjectType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_vars.put_env_var(
                object_type=PutEnvVarRequestObjectType.ORGANIZATION,
                object_id="object_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_env_var(
            object_type=object_type,
            object_id=object_id,
            name=name,
            value=value,
            metadata=metadata,
            secret_type=secret_type,
            request_options=request_options,
        )
        return _response.data

    async def get_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvVar:
        """
        Get an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the env_var object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_vars.get_env_var_id(
                env_var_id="env_var_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_env_var_id(env_var_id, request_options=request_options)
        return _response.data

    async def delete_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvVar:
        """
        Delete an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the deleted env_var object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_vars.delete_env_var_id(
                env_var_id="env_var_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_env_var_id(env_var_id, request_options=request_options)
        return _response.data

    async def patch_env_var_id(
        self,
        env_var_id: EnvVarIdParam,
        *,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvVar:
        """
        Partially update an env_var object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvVar
            Returns the env_var object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.env_vars.patch_env_var_id(
                env_var_id="env_var_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_env_var_id(
            env_var_id,
            name=name,
            value=value,
            metadata=metadata,
            secret_type=secret_type,
            request_options=request_options,
        )
        return _response.data
