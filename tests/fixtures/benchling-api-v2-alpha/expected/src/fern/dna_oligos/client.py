

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.async_task_link import AsyncTaskLink
from ..types.custom_fields import CustomFields
from ..types.dna_oligo_helm import DnaOligoHelm
from ..types.dna_oligos_paginated_list_helm import DnaOligosPaginatedListHelm
from ..types.fields import Fields
from ..types.naming_strategy import NamingStrategy
from ..types.oligo_create_helm import OligoCreateHelm
from ..types.schema_fields_query_param import SchemaFieldsQueryParam
from .raw_client import AsyncRawDnaOligosClient, RawDnaOligosClient
from .types.list_dna_oligos_helm_request_sort import ListDnaOligosHelmRequestSort


OMIT = typing.cast(typing.Any, ...)


class DnaOligosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDnaOligosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDnaOligosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDnaOligosClient
        """
        return self._raw_client

    def list_dna_oligos_helm(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListDnaOligosHelmRequestSort] = None,
        modified_at: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_includes: typing.Optional[str] = None,
        bases: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        mentioned_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        schema_fields: typing.Optional[SchemaFieldsQueryParam] = None,
        archive_reason: typing.Optional[str] = None,
        mentions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ids: typing.Optional[str] = None,
        entity_registry_ids_any_of: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DnaOligosPaginatedListHelm:
        """
        List DNA Oligos with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListDnaOligosHelmRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        name : typing.Optional[str]
            Name of a DNA Oligo. Restricts results to those with the specified name, alias, or entity registry ID.

        name_includes : typing.Optional[str]
            Name substring of a DNA Oligo. Restricts results to those with names, aliases, or entity registry IDs that include the provided substring.

        bases : typing.Optional[str]
            Full bases of the DNA Oligo. Restricts results to those with the specified bases, case-insensitive, allowing for circular or reverse complement matches. Does not allow partial matching or loose matching via degenerate bases.

        folder_id : typing.Optional[str]
            ID of a folder. Restricts results to those in the folder.

        mentioned_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of entry IDs. Restricts results to DNA Oligos mentioned in those entries.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        registry_id : typing.Optional[str]
            ID of a registry. Restricts results to those registered in this registry. Specifying "null" returns unregistered items.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        schema_fields : typing.Optional[SchemaFieldsQueryParam]
            Schema field value. For Integer, Float, and Date type fields, supports the >= and <= operators. If present, the schemaId param must also be present. Restricts results to those with a field of whose value matches the filter.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived DNA Oligos.

        mentions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of item IDs. Restricts results to those that mention the given items in the description.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        entity_registry_ids_any_of : typing.Optional[str]
            Comma-separated list of entity registry IDs. Restricts results to those that match any of the specified registry IDs.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligosPaginatedListHelm
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dna_oligos.list_dna_oligos_helm(
            modified_at="> 2022-03-01 AND < 2022-04-01",
            ids="seq_yWs5X7lv,seq_RhYGVnHF",
            entity_registry_ids_any_of="TP001,TP002",
            names_any_of="MyName1, MyName2",
            names_any_of_case_sensitive="MyName1,MyName2",
        )
        """
        _response = self._raw_client.list_dna_oligos_helm(
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            modified_at=modified_at,
            name=name,
            name_includes=name_includes,
            bases=bases,
            folder_id=folder_id,
            mentioned_in=mentioned_in,
            project_id=project_id,
            registry_id=registry_id,
            schema_id=schema_id,
            schema_fields=schema_fields,
            archive_reason=archive_reason,
            mentions=mentions,
            ids=ids,
            entity_registry_ids_any_of=entity_registry_ids_any_of,
            names_any_of=names_any_of,
            names_any_of_case_sensitive=names_any_of_case_sensitive,
            request_options=request_options,
        )
        return _response.data

    def create_dna_oligo_with_helm(
        self,
        *,
        name: str,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        entity_registry_id: typing.Optional[str] = OMIT,
        naming_strategy: typing.Optional[NamingStrategy] = OMIT,
        registry_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DnaOligoHelm:
        """
        Create a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        name : str
            Name of the Oligo.

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        entity_registry_id : typing.Optional[str]
            Entity registry ID to set for the registered entity. Cannot specify both entityRegistryId and namingStrategy at the same time.

        naming_strategy : typing.Optional[NamingStrategy]

        registry_id : typing.Optional[str]
            Registry ID into which entity should be registered. this is the ID of the registry which was configured for a particular organization
            To get available registryIds, use the [/registries endpoint](#/Registry/listRegistries)

            Required in order for entities to be created directly in the registry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligoHelm
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dna_oligos.create_dna_oligo_with_helm(
            name="name",
        )
        """
        _response = self._raw_client.create_dna_oligo_with_helm(
            name=name,
            helm=helm,
            aliases=aliases,
            author_ids=author_ids,
            bases=bases,
            custom_fields=custom_fields,
            fields=fields,
            folder_id=folder_id,
            schema_id=schema_id,
            entity_registry_id=entity_registry_id,
            naming_strategy=naming_strategy,
            registry_id=registry_id,
            request_options=request_options,
        )
        return _response.data

    def get_dna_oligo_helm(
        self, oligo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DnaOligoHelm:
        """
        Get a DNA Oligo with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligoHelm
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dna_oligos.get_dna_oligo_helm(
            oligo_id="oligo_id",
        )
        """
        _response = self._raw_client.get_dna_oligo_helm(oligo_id, request_options=request_options)
        return _response.data

    def update_dna_oligo_helm(
        self,
        oligo_id: str,
        *,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DnaOligoHelm:
        """
        Update a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        name : typing.Optional[str]
            Name of the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligoHelm
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dna_oligos.update_dna_oligo_helm(
            oligo_id="oligo_id",
        )
        """
        _response = self._raw_client.update_dna_oligo_helm(
            oligo_id,
            helm=helm,
            aliases=aliases,
            author_ids=author_ids,
            bases=bases,
            custom_fields=custom_fields,
            fields=fields,
            folder_id=folder_id,
            name=name,
            schema_id=schema_id,
            request_options=request_options,
        )
        return _response.data

    def bulk_create_dna_oligos_helm(
        self,
        *,
        dna_oligos: typing.Optional[typing.Sequence[OligoCreateHelm]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Bulk Create DNA Oligos with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        dna_oligos : typing.Optional[typing.Sequence[OligoCreateHelm]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dna_oligos.bulk_create_dna_oligos_helm()
        """
        _response = self._raw_client.bulk_create_dna_oligos_helm(dna_oligos=dna_oligos, request_options=request_options)
        return _response.data


class AsyncDnaOligosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDnaOligosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDnaOligosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDnaOligosClient
        """
        return self._raw_client

    async def list_dna_oligos_helm(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListDnaOligosHelmRequestSort] = None,
        modified_at: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_includes: typing.Optional[str] = None,
        bases: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        mentioned_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        schema_fields: typing.Optional[SchemaFieldsQueryParam] = None,
        archive_reason: typing.Optional[str] = None,
        mentions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ids: typing.Optional[str] = None,
        entity_registry_ids_any_of: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DnaOligosPaginatedListHelm:
        """
        List DNA Oligos with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListDnaOligosHelmRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        name : typing.Optional[str]
            Name of a DNA Oligo. Restricts results to those with the specified name, alias, or entity registry ID.

        name_includes : typing.Optional[str]
            Name substring of a DNA Oligo. Restricts results to those with names, aliases, or entity registry IDs that include the provided substring.

        bases : typing.Optional[str]
            Full bases of the DNA Oligo. Restricts results to those with the specified bases, case-insensitive, allowing for circular or reverse complement matches. Does not allow partial matching or loose matching via degenerate bases.

        folder_id : typing.Optional[str]
            ID of a folder. Restricts results to those in the folder.

        mentioned_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of entry IDs. Restricts results to DNA Oligos mentioned in those entries.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        registry_id : typing.Optional[str]
            ID of a registry. Restricts results to those registered in this registry. Specifying "null" returns unregistered items.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        schema_fields : typing.Optional[SchemaFieldsQueryParam]
            Schema field value. For Integer, Float, and Date type fields, supports the >= and <= operators. If present, the schemaId param must also be present. Restricts results to those with a field of whose value matches the filter.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived DNA Oligos.

        mentions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of item IDs. Restricts results to those that mention the given items in the description.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        entity_registry_ids_any_of : typing.Optional[str]
            Comma-separated list of entity registry IDs. Restricts results to those that match any of the specified registry IDs.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligosPaginatedListHelm
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
            await client.dna_oligos.list_dna_oligos_helm(
                modified_at="> 2022-03-01 AND < 2022-04-01",
                ids="seq_yWs5X7lv,seq_RhYGVnHF",
                entity_registry_ids_any_of="TP001,TP002",
                names_any_of="MyName1, MyName2",
                names_any_of_case_sensitive="MyName1,MyName2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_dna_oligos_helm(
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            modified_at=modified_at,
            name=name,
            name_includes=name_includes,
            bases=bases,
            folder_id=folder_id,
            mentioned_in=mentioned_in,
            project_id=project_id,
            registry_id=registry_id,
            schema_id=schema_id,
            schema_fields=schema_fields,
            archive_reason=archive_reason,
            mentions=mentions,
            ids=ids,
            entity_registry_ids_any_of=entity_registry_ids_any_of,
            names_any_of=names_any_of,
            names_any_of_case_sensitive=names_any_of_case_sensitive,
            request_options=request_options,
        )
        return _response.data

    async def create_dna_oligo_with_helm(
        self,
        *,
        name: str,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        entity_registry_id: typing.Optional[str] = OMIT,
        naming_strategy: typing.Optional[NamingStrategy] = OMIT,
        registry_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DnaOligoHelm:
        """
        Create a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        name : str
            Name of the Oligo.

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        entity_registry_id : typing.Optional[str]
            Entity registry ID to set for the registered entity. Cannot specify both entityRegistryId and namingStrategy at the same time.

        naming_strategy : typing.Optional[NamingStrategy]

        registry_id : typing.Optional[str]
            Registry ID into which entity should be registered. this is the ID of the registry which was configured for a particular organization
            To get available registryIds, use the [/registries endpoint](#/Registry/listRegistries)

            Required in order for entities to be created directly in the registry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligoHelm
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dna_oligos.create_dna_oligo_with_helm(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dna_oligo_with_helm(
            name=name,
            helm=helm,
            aliases=aliases,
            author_ids=author_ids,
            bases=bases,
            custom_fields=custom_fields,
            fields=fields,
            folder_id=folder_id,
            schema_id=schema_id,
            entity_registry_id=entity_registry_id,
            naming_strategy=naming_strategy,
            registry_id=registry_id,
            request_options=request_options,
        )
        return _response.data

    async def get_dna_oligo_helm(
        self, oligo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DnaOligoHelm:
        """
        Get a DNA Oligo with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligoHelm
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
            await client.dna_oligos.get_dna_oligo_helm(
                oligo_id="oligo_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dna_oligo_helm(oligo_id, request_options=request_options)
        return _response.data

    async def update_dna_oligo_helm(
        self,
        oligo_id: str,
        *,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DnaOligoHelm:
        """
        Update a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        name : typing.Optional[str]
            Name of the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DnaOligoHelm
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
            await client.dna_oligos.update_dna_oligo_helm(
                oligo_id="oligo_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_dna_oligo_helm(
            oligo_id,
            helm=helm,
            aliases=aliases,
            author_ids=author_ids,
            bases=bases,
            custom_fields=custom_fields,
            fields=fields,
            folder_id=folder_id,
            name=name,
            schema_id=schema_id,
            request_options=request_options,
        )
        return _response.data

    async def bulk_create_dna_oligos_helm(
        self,
        *,
        dna_oligos: typing.Optional[typing.Sequence[OligoCreateHelm]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Bulk Create DNA Oligos with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        dna_oligos : typing.Optional[typing.Sequence[OligoCreateHelm]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            Accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dna_oligos.bulk_create_dna_oligos_helm()


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_create_dna_oligos_helm(
            dna_oligos=dna_oligos, request_options=request_options
        )
        return _response.data
