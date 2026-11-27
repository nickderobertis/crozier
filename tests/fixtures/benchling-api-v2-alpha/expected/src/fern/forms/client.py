

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.form_definition import FormDefinition
from ..types.form_definitions_paginated_list import FormDefinitionsPaginatedList
from .raw_client import AsyncRawFormsClient, RawFormsClient
from .types.get_form_definitions_request_sort import GetFormDefinitionsRequestSort


class FormsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFormsClient
        """
        return self._raw_client

    def get_form_definitions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        sort: typing.Optional[GetFormDefinitionsRequestSort] = None,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormDefinitionsPaginatedList:
        """
        Lists available form definitions. Only the latest version along is returned for each definition.

        Parameters
        ----------
        next_token : typing.Optional[str]
            Token for pagination

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        sort : typing.Optional[GetFormDefinitionsRequestSort]
            Sets the sort-order of the response. Valid sorts are modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order.

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormDefinitionsPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.forms.get_form_definitions(
            modified_at="> 2022-03-01 AND < 2022-04-01",
            returning="formDefinitions.id,formDefinitions.modifiedAt",
        )
        """
        _response = self._raw_client.get_form_definitions(
            next_token=next_token,
            page_size=page_size,
            modified_at=modified_at,
            sort=sort,
            returning=returning,
            request_options=request_options,
        )
        return _response.data

    def get_form_definition(
        self,
        form_definition_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormDefinition:
        """
        Get a specific form definition. Only the latest version is returned

        Parameters
        ----------
        form_definition_id : str
            API ID of the specific form definition desired

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.forms.get_form_definition(
            form_definition_id="fmdef_W7KgYydE",
            returning="id,modifiedAt",
        )
        """
        _response = self._raw_client.get_form_definition(
            form_definition_id, returning=returning, request_options=request_options
        )
        return _response.data


class AsyncFormsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFormsClient
        """
        return self._raw_client

    async def get_form_definitions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        sort: typing.Optional[GetFormDefinitionsRequestSort] = None,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormDefinitionsPaginatedList:
        """
        Lists available form definitions. Only the latest version along is returned for each definition.

        Parameters
        ----------
        next_token : typing.Optional[str]
            Token for pagination

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        sort : typing.Optional[GetFormDefinitionsRequestSort]
            Sets the sort-order of the response. Valid sorts are modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order.

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormDefinitionsPaginatedList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.forms.get_form_definitions(
                modified_at="> 2022-03-01 AND < 2022-04-01",
                returning="formDefinitions.id,formDefinitions.modifiedAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form_definitions(
            next_token=next_token,
            page_size=page_size,
            modified_at=modified_at,
            sort=sort,
            returning=returning,
            request_options=request_options,
        )
        return _response.data

    async def get_form_definition(
        self,
        form_definition_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormDefinition:
        """
        Get a specific form definition. Only the latest version is returned

        Parameters
        ----------
        form_definition_id : str
            API ID of the specific form definition desired

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.forms.get_form_definition(
                form_definition_id="fmdef_W7KgYydE",
                returning="id,modifiedAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form_definition(
            form_definition_id, returning=returning, request_options=request_options
        )
        return _response.data
