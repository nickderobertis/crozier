

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_authorization_codes_shared_models_authorization_code import (
    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode,
)
from ..types.authorization_codes_shared_models_authorization_code import AuthorizationCodesSharedModelsAuthorizationCode
from ..types.authorization_codes_shared_models_authorization_contact_information import (
    AuthorizationCodesSharedModelsAuthorizationContactInformation,
)
from ..types.authorization_codes_shared_models_code_validation_model import (
    AuthorizationCodesSharedModelsCodeValidationModel,
)
from ..types.authorization_codes_shared_models_parameter import AuthorizationCodesSharedModelsParameter
from .raw_client import AsyncRawAuthorizationcodesClient, RawAuthorizationcodesClient


OMIT = typing.cast(typing.Any, ...)


class AuthorizationcodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorizationcodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorizationcodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorizationcodesClient
        """
        return self._raw_client

    def getauthorizationcodes(
        self,
        *,
        code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        definition_id: typing.Optional[str] = None,
        created_by_user_id: typing.Optional[int] = None,
        deleted_by_user_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode:
        """
        Additional searches: validationParameters[Name]=Value and dataParameters[Name]=Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.

        Parameters
        ----------
        code : typing.Optional[str]
            Optional. If provided, searches for entities with the provided authorization code.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        definition_id : typing.Optional[str]
            Optional. If specified, filters codes by definition id.

        created_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those created by the given User ID.

        deleted_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those deleted by the given User ID.

        include_deleted : typing.Optional[bool]
            Optional. Whether to include deleted codes. 'False' by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodes.getauthorizationcodes()
        """
        _response = self._raw_client.getauthorizationcodes(
            code=code,
            limit=limit,
            offset=offset,
            definition_id=definition_id,
            created_by_user_id=created_by_user_id,
            deleted_by_user_id=deleted_by_user_id,
            include_deleted=include_deleted,
            request_options=request_options,
        )
        return _response.data

    def postauthorizationcode(
        self,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodes.postauthorizationcode()
        """
        _response = self._raw_client.postauthorizationcode(
            code=code,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_parameters=data_parameters,
            definition_id=definition_id,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            effective_date=effective_date,
            id=id,
            is_deleted=is_deleted,
            validation_parameters=validation_parameters,
            request_options=request_options,
        )
        return _response.data

    def getauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsAuthorizationCode:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsAuthorizationCode
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodes.getauthorizationcode(
            id=1,
        )
        """
        _response = self._raw_client.getauthorizationcode(id, request_options=request_options)
        return _response.data

    def putauthorizationcode(
        self,
        id_: int,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The id of the authorization code.

        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodes.putauthorizationcode(
            id_=1,
        )
        """
        _response = self._raw_client.putauthorizationcode(
            id_,
            code=code,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_parameters=data_parameters,
            definition_id=definition_id,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            effective_date=effective_date,
            id=id,
            is_deleted=is_deleted,
            validation_parameters=validation_parameters,
            request_options=request_options,
        )
        return _response.data

    def deleteauthorizationcode(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodes.deleteauthorizationcode(
            id=1,
        )
        """
        _response = self._raw_client.deleteauthorizationcode(id, request_options=request_options)
        return _response.data

    def getcontactinformation(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsAuthorizationContactInformation:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsAuthorizationContactInformation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodes.getcontactinformation(
            id=1,
        )
        """
        _response = self._raw_client.getcontactinformation(id, request_options=request_options)
        return _response.data

    def validateauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsCodeValidationModel:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsCodeValidationModel
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodes.validateauthorizationcode(
            id=1,
        )
        """
        _response = self._raw_client.validateauthorizationcode(id, request_options=request_options)
        return _response.data


class AsyncAuthorizationcodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorizationcodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorizationcodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorizationcodesClient
        """
        return self._raw_client

    async def getauthorizationcodes(
        self,
        *,
        code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        definition_id: typing.Optional[str] = None,
        created_by_user_id: typing.Optional[int] = None,
        deleted_by_user_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode:
        """
        Additional searches: validationParameters[Name]=Value and dataParameters[Name]=Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.

        Parameters
        ----------
        code : typing.Optional[str]
            Optional. If provided, searches for entities with the provided authorization code.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        definition_id : typing.Optional[str]
            Optional. If specified, filters codes by definition id.

        created_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those created by the given User ID.

        deleted_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those deleted by the given User ID.

        include_deleted : typing.Optional[bool]
            Optional. Whether to include deleted codes. 'False' by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcodes.getauthorizationcodes()


        asyncio.run(main())
        """
        _response = await self._raw_client.getauthorizationcodes(
            code=code,
            limit=limit,
            offset=offset,
            definition_id=definition_id,
            created_by_user_id=created_by_user_id,
            deleted_by_user_id=deleted_by_user_id,
            include_deleted=include_deleted,
            request_options=request_options,
        )
        return _response.data

    async def postauthorizationcode(
        self,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcodes.postauthorizationcode()


        asyncio.run(main())
        """
        _response = await self._raw_client.postauthorizationcode(
            code=code,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_parameters=data_parameters,
            definition_id=definition_id,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            effective_date=effective_date,
            id=id,
            is_deleted=is_deleted,
            validation_parameters=validation_parameters,
            request_options=request_options,
        )
        return _response.data

    async def getauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsAuthorizationCode:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsAuthorizationCode
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcodes.getauthorizationcode(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getauthorizationcode(id, request_options=request_options)
        return _response.data

    async def putauthorizationcode(
        self,
        id_: int,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The id of the authorization code.

        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

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
            await client.authorizationcodes.putauthorizationcode(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putauthorizationcode(
            id_,
            code=code,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_parameters=data_parameters,
            definition_id=definition_id,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            effective_date=effective_date,
            id=id,
            is_deleted=is_deleted,
            validation_parameters=validation_parameters,
            request_options=request_options,
        )
        return _response.data

    async def deleteauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

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
            await client.authorizationcodes.deleteauthorizationcode(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteauthorizationcode(id, request_options=request_options)
        return _response.data

    async def getcontactinformation(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsAuthorizationContactInformation:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsAuthorizationContactInformation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcodes.getcontactinformation(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontactinformation(id, request_options=request_options)
        return _response.data

    async def validateauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsCodeValidationModel:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsCodeValidationModel
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcodes.validateauthorizationcode(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validateauthorizationcode(id, request_options=request_options)
        return _response.data
