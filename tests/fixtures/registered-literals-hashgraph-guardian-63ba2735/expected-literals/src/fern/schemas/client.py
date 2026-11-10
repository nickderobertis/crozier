

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_schema import ExportSchema
from ..types.schema import Schema
from ..types.schema_document import SchemaDocument
from ..types.schema_dto import SchemaDto
from ..types.task import Task
from ..types.task_dto import TaskDto
from .raw_client import AsyncRawSchemasClient, RawSchemasClient
from .types.get_schemas_system_entity_schema_entity_request_schema_entity import (
    GetSchemasSystemEntitySchemaEntityRequestSchemaEntity,
)


OMIT = typing.cast(typing.Any, ...)


class SchemasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchemasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchemasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchemasClient
        """
        return self._raw_client

    def returns_all_schemas(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all schemas.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.returns_all_schemas()
        """
        _response = self._raw_client.returns_all_schemas(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    def returns_all_schemas_by_topic_id(
        self,
        topic_id: str,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all schemas by topicId.

        Parameters
        ----------
        topic_id : str
            Topic ID.

        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.returns_all_schemas_by_topic_id(
            topic_id="0.0.00000001",
        )
        """
        _response = self._raw_client.returns_all_schemas_by_topic_id(
            topic_id, page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_new_schema(
        self,
        topic_id_: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Creates new schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id_ : str
            Topic ID.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.create_new_schema(
            topic_id_="0.0.00000001",
            id="id",
            name="name",
            description="description",
            entity="entity",
            document="document",
        )
        """
        _response = self._raw_client.create_new_schema(
            topic_id_,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    def schema_api_get_schema_by_type(
        self, schema_type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaDto:
        """
        Finds the schema using the json document type.

        Parameters
        ----------
        schema_type : str
            Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_get_schema_by_type(
            schema_type="schemaType",
        )
        """
        _response = self._raw_client.schema_api_get_schema_by_type(schema_type, request_options=request_options)
        return _response.data

    def schema_api_get_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[SchemaDto]:
        """
        Returns a list of schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemaDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_get_all()
        """
        _response = self._raw_client.schema_api_get_all(request_options=request_options)
        return _response.data

    def schema_api_get_sub(
        self,
        *,
        category: typing.Optional[str] = None,
        topic_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SchemaDto]:
        """
        Returns a list of schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        category : typing.Optional[str]
            Schema category

        topic_id : typing.Optional[str]
            Topic Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemaDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_get_sub()
        """
        _response = self._raw_client.schema_api_get_sub(
            category=category, topic_id=topic_id, request_options=request_options
        )
        return _response.data

    def schema_api_copy_schema_async(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Copy schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_copy_schema_async(
            request="string",
        )
        """
        _response = self._raw_client.schema_api_copy_schema_async(request=request, request_options=request_options)
        return _response.data

    def updates_the_schema(
        self,
        schema_id: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Updates the system schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.updates_the_schema(
            schema_id="schemaId",
            id="id",
            name="name",
            description="description",
            entity="entity",
            document="document",
        )
        """
        _response = self._raw_client.updates_the_schema(
            schema_id,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    def deletes_the_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Deletes the system schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.deletes_the_schema(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.deletes_the_schema(schema_id, request_options=request_options)
        return _response.data

    def publishes_the_schema(
        self,
        schema_id: str,
        *,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Makes the selected scheme active. Other schemes of the same type become inactive. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.publishes_the_schema(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.publishes_the_schema(schema_id, version=version, request_options=request_options)
        return _response.data

    def publishes_the_schema_with_the_provided_internal_schema_id_onto_ipfs_sends_a_message_featuring_ipfs_cid_into_the_corresponding_hedera_topic(
        self,
        schema_id: str,
        *,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Publishes the schema with the provided (internal) schema ID onto IPFS, sends a message featuring IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.publishes_the_schema_with_the_provided_internal_schema_id_onto_ipfs_sends_a_message_featuring_ipfs_cid_into_the_corresponding_hedera_topic(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.publishes_the_schema_with_the_provided_internal_schema_id_onto_ipfs_sends_a_message_featuring_ipfs_cid_into_the_corresponding_hedera_topic(
            schema_id, version=version, request_options=request_options
        )
        return _response.data

    def schema_preview_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Previews the schema from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_preview_from_ipfs()
        """
        _response = self._raw_client.schema_preview_from_ipfs(message_id=message_id, request_options=request_options)
        return _response.data

    def schema_preview_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Previews the schema from a zip file. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_preview_from_a_zip_file()
        """
        _response = self._raw_client.schema_preview_from_a_zip_file(request_options=request_options)
        return _response.data

    def imports_new_schema_from_ipfs(
        self,
        topic_id: str,
        *,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Imports new schema from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic ID.

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.imports_new_schema_from_ipfs(
            topic_id="0.0.00000001",
        )
        """
        _response = self._raw_client.imports_new_schema_from_ipfs(
            topic_id, message_id=message_id, request_options=request_options
        )
        return _response.data

    def imports_new_schema_from_a_zip_file(
        self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Imports new schema from a zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.imports_new_schema_from_a_zip_file(
            topic_id="0.0.00000001",
        )
        """
        _response = self._raw_client.imports_new_schema_from_a_zip_file(topic_id, request_options=request_options)
        return _response.data

    def list_hedera_message_i_ds_of_published_schemas(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportSchema:
        """
        Returns Hedera message IDs of the published schemas, these messages contain IPFS CIDs of these schema files. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Selected schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportSchema
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.list_hedera_message_i_ds_of_published_schemas(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.list_hedera_message_i_ds_of_published_schemas(
            schema_id, request_options=request_options
        )
        return _response.data

    def return_zip_file_with_schemas(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns schema files for the schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Selected schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.return_zip_file_with_schemas(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.return_zip_file_with_schemas(schema_id, request_options=request_options)
        return _response.data

    def returns_all_system_schemas_by_username(
        self,
        username: str,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all system schemas by username. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        username : str
            Username.

        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set.

        page_size : typing.Optional[int]
            The number of items to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.returns_all_system_schemas_by_username(
            username="username",
        )
        """
        _response = self._raw_client.returns_all_system_schemas_by_username(
            username, page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    def creates_new_system_schema(
        self,
        username: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates new system schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        username : str
            Username.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.creates_new_system_schema(
            username="username",
            id="id",
            name="name",
            description="description",
            entity="entity",
            document="document",
        )
        """
        _response = self._raw_client.creates_new_system_schema(
            username,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    def returns_schema_by_schema_type(
        self,
        schema_entity: GetSchemasSystemEntitySchemaEntityRequestSchemaEntity,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Schema:
        """
        Finds the schema using the schema type.

        Parameters
        ----------
        schema_entity : GetSchemasSystemEntitySchemaEntityRequestSchemaEntity
            schema type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.returns_schema_by_schema_type(
            schema_entity="STANDARD_REGISTRY",
        )
        """
        _response = self._raw_client.returns_schema_by_schema_type(schema_entity, request_options=request_options)
        return _response.data

    def schema_api_get_policy_export_xlsx(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Returns a xlsx file containing schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_get_policy_export_xlsx(
            schema_id="schemaId",
        )
        """
        with self._raw_client.schema_api_get_policy_export_xlsx(schema_id, request_options=request_options) as r:
            yield from r.data

    def schema_api_import_policy_from_xlsx(
        self, topic_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new schema from a xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_import_policy_from_xlsx(
            topic_id="topicId",
            request="string",
        )
        """
        _response = self._raw_client.schema_api_import_policy_from_xlsx(
            topic_id, request=request, request_options=request_options
        )
        return _response.data

    def schema_api_import_policy_from_xlsx_async(
        self, topic_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new schema from a xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_import_policy_from_xlsx_async(
            topic_id="topicId",
            request="string",
        )
        """
        _response = self._raw_client.schema_api_import_policy_from_xlsx_async(
            topic_id, request=request, request_options=request_options
        )
        return _response.data

    def schema_api_import_policy_from_xlsx_preview(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Previews the schema from a xlsx file. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_import_policy_from_xlsx_preview(
            request="string",
        )
        """
        _response = self._raw_client.schema_api_import_policy_from_xlsx_preview(
            request=request, request_options=request_options
        )
        return _response.data

    def schema_api_export_template(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Returns a list of schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.schema_api_export_template()
        """
        with self._raw_client.schema_api_export_template(request_options=request_options) as r:
            yield from r.data

    def returns_schema_by_type(self, type: str, *, request_options: typing.Optional[RequestOptions] = None) -> Schema:
        """
        Finds the schema using the json document type.

        Parameters
        ----------
        type : str
            JSON type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schemas.returns_schema_by_type(
            type="type",
        )
        """
        _response = self._raw_client.returns_schema_by_type(type, request_options=request_options)
        return _response.data


class AsyncSchemasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchemasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchemasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchemasClient
        """
        return self._raw_client

    async def returns_all_schemas(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all schemas.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.returns_all_schemas()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_schemas(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def returns_all_schemas_by_topic_id(
        self,
        topic_id: str,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all schemas by topicId.

        Parameters
        ----------
        topic_id : str
            Topic ID.

        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.returns_all_schemas_by_topic_id(
                topic_id="0.0.00000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_schemas_by_topic_id(
            topic_id, page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_new_schema(
        self,
        topic_id_: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Creates new schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id_ : str
            Topic ID.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.create_new_schema(
                topic_id_="0.0.00000001",
                id="id",
                name="name",
                description="description",
                entity="entity",
                document="document",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_new_schema(
            topic_id_,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    async def schema_api_get_schema_by_type(
        self, schema_type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaDto:
        """
        Finds the schema using the json document type.

        Parameters
        ----------
        schema_type : str
            Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_get_schema_by_type(
                schema_type="schemaType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_api_get_schema_by_type(schema_type, request_options=request_options)
        return _response.data

    async def schema_api_get_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SchemaDto]:
        """
        Returns a list of schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemaDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_get_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_api_get_all(request_options=request_options)
        return _response.data

    async def schema_api_get_sub(
        self,
        *,
        category: typing.Optional[str] = None,
        topic_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SchemaDto]:
        """
        Returns a list of schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        category : typing.Optional[str]
            Schema category

        topic_id : typing.Optional[str]
            Topic Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemaDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_get_sub()


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_api_get_sub(
            category=category, topic_id=topic_id, request_options=request_options
        )
        return _response.data

    async def schema_api_copy_schema_async(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Copy schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_copy_schema_async(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_api_copy_schema_async(
            request=request, request_options=request_options
        )
        return _response.data

    async def updates_the_schema(
        self,
        schema_id: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Updates the system schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.updates_the_schema(
                schema_id="schemaId",
                id="id",
                name="name",
                description="description",
                entity="entity",
                document="document",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_schema(
            schema_id,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    async def deletes_the_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Deletes the system schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.deletes_the_schema(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_schema(schema_id, request_options=request_options)
        return _response.data

    async def publishes_the_schema(
        self,
        schema_id: str,
        *,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Makes the selected scheme active. Other schemes of the same type become inactive. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.publishes_the_schema(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publishes_the_schema(
            schema_id, version=version, request_options=request_options
        )
        return _response.data

    async def publishes_the_schema_with_the_provided_internal_schema_id_onto_ipfs_sends_a_message_featuring_ipfs_cid_into_the_corresponding_hedera_topic(
        self,
        schema_id: str,
        *,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Publishes the schema with the provided (internal) schema ID onto IPFS, sends a message featuring IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.publishes_the_schema_with_the_provided_internal_schema_id_onto_ipfs_sends_a_message_featuring_ipfs_cid_into_the_corresponding_hedera_topic(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publishes_the_schema_with_the_provided_internal_schema_id_onto_ipfs_sends_a_message_featuring_ipfs_cid_into_the_corresponding_hedera_topic(
            schema_id, version=version, request_options=request_options
        )
        return _response.data

    async def schema_preview_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Previews the schema from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_preview_from_ipfs()


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_preview_from_ipfs(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    async def schema_preview_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Previews the schema from a zip file. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_preview_from_a_zip_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_preview_from_a_zip_file(request_options=request_options)
        return _response.data

    async def imports_new_schema_from_ipfs(
        self,
        topic_id: str,
        *,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Imports new schema from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic ID.

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.imports_new_schema_from_ipfs(
                topic_id="0.0.00000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_schema_from_ipfs(
            topic_id, message_id=message_id, request_options=request_options
        )
        return _response.data

    async def imports_new_schema_from_a_zip_file(
        self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Imports new schema from a zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.imports_new_schema_from_a_zip_file(
                topic_id="0.0.00000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_schema_from_a_zip_file(topic_id, request_options=request_options)
        return _response.data

    async def list_hedera_message_i_ds_of_published_schemas(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportSchema:
        """
        Returns Hedera message IDs of the published schemas, these messages contain IPFS CIDs of these schema files. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Selected schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportSchema
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.list_hedera_message_i_ds_of_published_schemas(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_hedera_message_i_ds_of_published_schemas(
            schema_id, request_options=request_options
        )
        return _response.data

    async def return_zip_file_with_schemas(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns schema files for the schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Selected schema ID.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.return_zip_file_with_schemas(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_zip_file_with_schemas(schema_id, request_options=request_options)
        return _response.data

    async def returns_all_system_schemas_by_username(
        self,
        username: str,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all system schemas by username. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        username : str
            Username.

        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set.

        page_size : typing.Optional[int]
            The number of items to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.returns_all_system_schemas_by_username(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_system_schemas_by_username(
            username, page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def creates_new_system_schema(
        self,
        username: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates new system schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        username : str
            Username.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.creates_new_system_schema(
                username="username",
                id="id",
                name="name",
                description="description",
                entity="entity",
                document="document",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_system_schema(
            username,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    async def returns_schema_by_schema_type(
        self,
        schema_entity: GetSchemasSystemEntitySchemaEntityRequestSchemaEntity,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Schema:
        """
        Finds the schema using the schema type.

        Parameters
        ----------
        schema_entity : GetSchemasSystemEntitySchemaEntityRequestSchemaEntity
            schema type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.returns_schema_by_schema_type(
                schema_entity="STANDARD_REGISTRY",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_schema_by_schema_type(schema_entity, request_options=request_options)
        return _response.data

    async def schema_api_get_policy_export_xlsx(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns a xlsx file containing schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_get_policy_export_xlsx(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.schema_api_get_policy_export_xlsx(schema_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def schema_api_import_policy_from_xlsx(
        self, topic_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new schema from a xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_import_policy_from_xlsx(
                topic_id="topicId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_api_import_policy_from_xlsx(
            topic_id, request=request, request_options=request_options
        )
        return _response.data

    async def schema_api_import_policy_from_xlsx_async(
        self, topic_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new schema from a xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        topic_id : str
            Topic Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_import_policy_from_xlsx_async(
                topic_id="topicId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_api_import_policy_from_xlsx_async(
            topic_id, request=request, request_options=request_options
        )
        return _response.data

    async def schema_api_import_policy_from_xlsx_preview(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Previews the schema from a xlsx file. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_import_policy_from_xlsx_preview(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schema_api_import_policy_from_xlsx_preview(
            request=request, request_options=request_options
        )
        return _response.data

    async def schema_api_export_template(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns a list of schemas. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.schema_api_export_template()


        asyncio.run(main())
        """
        async with self._raw_client.schema_api_export_template(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def returns_schema_by_type(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Schema:
        """
        Finds the schema using the json document type.

        Parameters
        ----------
        type : str
            JSON type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schemas.returns_schema_by_type(
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_schema_by_type(type, request_options=request_options)
        return _response.data
