

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ai_secret import AiSecret
from ..types.ai_secret_id_param import AiSecretIdParam
from ..types.ai_secret_name import AiSecretName
from ..types.ai_secret_type import AiSecretType
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawAiSecretsClient, RawAiSecretsClient
from .types.get_ai_secret_response import GetAiSecretResponse


OMIT = typing.cast(typing.Any, ...)


class AiSecretsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAiSecretsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAiSecretsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAiSecretsClient
        """
        return self._raw_client

    def get_ai_secret(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        ai_secret_name: typing.Optional[AiSecretName] = None,
        org_name: typing.Optional[OrgName] = None,
        ai_secret_type: typing.Optional[AiSecretType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAiSecretResponse:
        """
        List out all ai_secrets. The ai_secrets are sorted by creation date, with the most recently-created ai_secrets coming first

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

        ai_secret_name : typing.Optional[AiSecretName]
            Name of the ai_secret to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        ai_secret_type : typing.Optional[AiSecretType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAiSecretResponse
            Returns a list of ai_secret objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_secrets.get_ai_secret()
        """
        _response = self._raw_client.get_ai_secret(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            ai_secret_name=ai_secret_name,
            org_name=org_name,
            ai_secret_type=ai_secret_type,
            request_options=request_options,
        )
        return _response.data

    def post_ai_secret(
        self,
        *,
        name: str,
        type: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Create a new ai_secret. If there is an existing ai_secret with the same name as the one specified in the request, will return the existing ai_secret unmodified

        Parameters
        ----------
        name : str
            Name of the AI secret

        type : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        secret : typing.Optional[str]
            Secret value. If omitted in a PUT request, the existing secret value will be left intact, not replaced with null.

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the new ai_secret object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_secrets.post_ai_secret(
            name="name",
        )
        """
        _response = self._raw_client.post_ai_secret(
            name=name, type=type, metadata=metadata, secret=secret, org_name=org_name, request_options=request_options
        )
        return _response.data

    def put_ai_secret(
        self,
        *,
        name: str,
        type: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Create or replace ai_secret. If there is an existing ai_secret with the same name as the one specified in the request, will replace the existing ai_secret with the provided fields

        Parameters
        ----------
        name : str
            Name of the AI secret

        type : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        secret : typing.Optional[str]
            Secret value. If omitted in a PUT request, the existing secret value will be left intact, not replaced with null.

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the new ai_secret object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_secrets.put_ai_secret(
            name="name",
        )
        """
        _response = self._raw_client.put_ai_secret(
            name=name, type=type, metadata=metadata, secret=secret, org_name=org_name, request_options=request_options
        )
        return _response.data

    def delete_ai_secret(
        self,
        *,
        name: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Delete a single ai_secret

        Parameters
        ----------
        name : str
            Name of the AI secret

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the deleted ai_secret object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_secrets.delete_ai_secret(
            name="name",
        )
        """
        _response = self._raw_client.delete_ai_secret(name=name, org_name=org_name, request_options=request_options)
        return _response.data

    def get_ai_secret_id(
        self, ai_secret_id: AiSecretIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AiSecret:
        """
        Get an ai_secret object by its id

        Parameters
        ----------
        ai_secret_id : AiSecretIdParam
            AiSecret id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the ai_secret object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_secrets.get_ai_secret_id(
            ai_secret_id="ai_secret_id",
        )
        """
        _response = self._raw_client.get_ai_secret_id(ai_secret_id, request_options=request_options)
        return _response.data

    def delete_ai_secret_id(
        self, ai_secret_id: AiSecretIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AiSecret:
        """
        Delete an ai_secret object by its id

        Parameters
        ----------
        ai_secret_id : AiSecretIdParam
            AiSecret id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the deleted ai_secret object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_secrets.delete_ai_secret_id(
            ai_secret_id="ai_secret_id",
        )
        """
        _response = self._raw_client.delete_ai_secret_id(ai_secret_id, request_options=request_options)
        return _response.data

    def patch_ai_secret_id(
        self,
        ai_secret_id: AiSecretIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Partially update an ai_secret object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        ai_secret_id : AiSecretIdParam
            AiSecret id

        name : typing.Optional[str]
            Name of the AI secret

        type : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the ai_secret object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_secrets.patch_ai_secret_id(
            ai_secret_id="ai_secret_id",
        )
        """
        _response = self._raw_client.patch_ai_secret_id(
            ai_secret_id, name=name, type=type, metadata=metadata, secret=secret, request_options=request_options
        )
        return _response.data


class AsyncAiSecretsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAiSecretsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAiSecretsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAiSecretsClient
        """
        return self._raw_client

    async def get_ai_secret(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        ai_secret_name: typing.Optional[AiSecretName] = None,
        org_name: typing.Optional[OrgName] = None,
        ai_secret_type: typing.Optional[AiSecretType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAiSecretResponse:
        """
        List out all ai_secrets. The ai_secrets are sorted by creation date, with the most recently-created ai_secrets coming first

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

        ai_secret_name : typing.Optional[AiSecretName]
            Name of the ai_secret to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        ai_secret_type : typing.Optional[AiSecretType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAiSecretResponse
            Returns a list of ai_secret objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_secrets.get_ai_secret()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ai_secret(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            ai_secret_name=ai_secret_name,
            org_name=org_name,
            ai_secret_type=ai_secret_type,
            request_options=request_options,
        )
        return _response.data

    async def post_ai_secret(
        self,
        *,
        name: str,
        type: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Create a new ai_secret. If there is an existing ai_secret with the same name as the one specified in the request, will return the existing ai_secret unmodified

        Parameters
        ----------
        name : str
            Name of the AI secret

        type : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        secret : typing.Optional[str]
            Secret value. If omitted in a PUT request, the existing secret value will be left intact, not replaced with null.

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the new ai_secret object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_secrets.post_ai_secret(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_ai_secret(
            name=name, type=type, metadata=metadata, secret=secret, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def put_ai_secret(
        self,
        *,
        name: str,
        type: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Create or replace ai_secret. If there is an existing ai_secret with the same name as the one specified in the request, will replace the existing ai_secret with the provided fields

        Parameters
        ----------
        name : str
            Name of the AI secret

        type : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        secret : typing.Optional[str]
            Secret value. If omitted in a PUT request, the existing secret value will be left intact, not replaced with null.

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the new ai_secret object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_secrets.put_ai_secret(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_ai_secret(
            name=name, type=type, metadata=metadata, secret=secret, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def delete_ai_secret(
        self,
        *,
        name: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Delete a single ai_secret

        Parameters
        ----------
        name : str
            Name of the AI secret

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the deleted ai_secret object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_secrets.delete_ai_secret(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ai_secret(
            name=name, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def get_ai_secret_id(
        self, ai_secret_id: AiSecretIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AiSecret:
        """
        Get an ai_secret object by its id

        Parameters
        ----------
        ai_secret_id : AiSecretIdParam
            AiSecret id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the ai_secret object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_secrets.get_ai_secret_id(
                ai_secret_id="ai_secret_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ai_secret_id(ai_secret_id, request_options=request_options)
        return _response.data

    async def delete_ai_secret_id(
        self, ai_secret_id: AiSecretIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AiSecret:
        """
        Delete an ai_secret object by its id

        Parameters
        ----------
        ai_secret_id : AiSecretIdParam
            AiSecret id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the deleted ai_secret object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_secrets.delete_ai_secret_id(
                ai_secret_id="ai_secret_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ai_secret_id(ai_secret_id, request_options=request_options)
        return _response.data

    async def patch_ai_secret_id(
        self,
        ai_secret_id: AiSecretIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiSecret:
        """
        Partially update an ai_secret object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        ai_secret_id : AiSecretIdParam
            AiSecret id

        name : typing.Optional[str]
            Name of the AI secret

        type : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiSecret
            Returns the ai_secret object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_secrets.patch_ai_secret_id(
                ai_secret_id="ai_secret_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_ai_secret_id(
            ai_secret_id, name=name, type=type, metadata=metadata, secret=secret, request_options=request_options
        )
        return _response.data
