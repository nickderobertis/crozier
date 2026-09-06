

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorization_codes_shared_models_authorization_code_definition import (
    AuthorizationCodesSharedModelsAuthorizationCodeDefinition,
)
from ..types.authorization_codes_shared_models_authorization_code_definition_duration_units import (
    AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits,
)
from ..types.authorization_codes_shared_models_data_field import AuthorizationCodesSharedModelsDataField
from ..types.authorization_codes_shared_models_validation_field import AuthorizationCodesSharedModelsValidationField
from .raw_client import AsyncRawAuthorizationcodedefinitionsClient, RawAuthorizationcodedefinitionsClient


OMIT = typing.cast(typing.Any, ...)


class AuthorizationcodedefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorizationcodedefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorizationcodedefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorizationcodedefinitionsClient
        """
        return self._raw_client

    def getauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsAuthorizationCodeDefinition:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsAuthorizationCodeDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodedefinitions.getauthorizationcodedefinition(
            id="id",
        )
        """
        _response = self._raw_client.getauthorizationcodedefinition(id, request_options=request_options)
        return _response.data

    def postauthorizationcodedefinition(
        self,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodedefinitions.postauthorizationcodedefinition(
            name="Name",
        )
        """
        _response = self._raw_client.postauthorizationcodedefinition(
            name=name,
            authorization_id=authorization_id,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_fields=data_fields,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            description=description,
            duration_accuracy=duration_accuracy,
            duration_amount=duration_amount,
            duration_units=duration_units,
            hash_length=hash_length,
            id=id,
            is_deleted=is_deleted,
            random_length=random_length,
            validation_fields=validation_fields,
            request_options=request_options,
        )
        return _response.data

    def addcategorytodefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodedefinitions.addcategorytodefinition(
            id="ID",
            category_id="categoryID",
        )
        """
        _response = self._raw_client.addcategorytodefinition(id, category_id, request_options=request_options)
        return _response.data

    def removecategoryfromdefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodedefinitions.removecategoryfromdefinition(
            id="ID",
            category_id="categoryID",
        )
        """
        _response = self._raw_client.removecategoryfromdefinition(id, category_id, request_options=request_options)
        return _response.data

    def putauthorizationcodedefinition(
        self,
        id_: str,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            The ID of the authorization code definition.

        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodedefinitions.putauthorizationcodedefinition(
            id_="id",
            name="Name",
        )
        """
        _response = self._raw_client.putauthorizationcodedefinition(
            id_,
            name=name,
            authorization_id=authorization_id,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_fields=data_fields,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            description=description,
            duration_accuracy=duration_accuracy,
            duration_amount=duration_amount,
            duration_units=duration_units,
            hash_length=hash_length,
            id=id,
            is_deleted=is_deleted,
            random_length=random_length,
            validation_fields=validation_fields,
            request_options=request_options,
        )
        return _response.data

    def deleteauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcodedefinitions.deleteauthorizationcodedefinition(
            id="id",
        )
        """
        _response = self._raw_client.deleteauthorizationcodedefinition(id, request_options=request_options)
        return _response.data


class AsyncAuthorizationcodedefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorizationcodedefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorizationcodedefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorizationcodedefinitionsClient
        """
        return self._raw_client

    async def getauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationCodesSharedModelsAuthorizationCodeDefinition:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationCodesSharedModelsAuthorizationCodeDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcodedefinitions.getauthorizationcodedefinition(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getauthorizationcodedefinition(id, request_options=request_options)
        return _response.data

    async def postauthorizationcodedefinition(
        self,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcodedefinitions.postauthorizationcodedefinition(
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postauthorizationcodedefinition(
            name=name,
            authorization_id=authorization_id,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_fields=data_fields,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            description=description,
            duration_accuracy=duration_accuracy,
            duration_amount=duration_amount,
            duration_units=duration_units,
            hash_length=hash_length,
            id=id,
            is_deleted=is_deleted,
            random_length=random_length,
            validation_fields=validation_fields,
            request_options=request_options,
        )
        return _response.data

    async def addcategorytodefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

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
            await client.authorizationcodedefinitions.addcategorytodefinition(
                id="ID",
                category_id="categoryID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addcategorytodefinition(id, category_id, request_options=request_options)
        return _response.data

    async def removecategoryfromdefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

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
            await client.authorizationcodedefinitions.removecategoryfromdefinition(
                id="ID",
                category_id="categoryID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removecategoryfromdefinition(
            id, category_id, request_options=request_options
        )
        return _response.data

    async def putauthorizationcodedefinition(
        self,
        id_: str,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            The ID of the authorization code definition.

        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

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
            await client.authorizationcodedefinitions.putauthorizationcodedefinition(
                id_="id",
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putauthorizationcodedefinition(
            id_,
            name=name,
            authorization_id=authorization_id,
            created_by_user_id=created_by_user_id,
            created_date=created_date,
            data_fields=data_fields,
            deleted_by_user_id=deleted_by_user_id,
            deleted_date=deleted_date,
            description=description,
            duration_accuracy=duration_accuracy,
            duration_amount=duration_amount,
            duration_units=duration_units,
            hash_length=hash_length,
            id=id,
            is_deleted=is_deleted,
            random_length=random_length,
            validation_fields=validation_fields,
            request_options=request_options,
        )
        return _response.data

    async def deleteauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

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
            await client.authorizationcodedefinitions.deleteauthorizationcodedefinition(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteauthorizationcodedefinition(id, request_options=request_options)
        return _response.data
