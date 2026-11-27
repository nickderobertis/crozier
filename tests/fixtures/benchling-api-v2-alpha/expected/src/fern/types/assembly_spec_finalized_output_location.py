

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblySpecFinalizedOutputLocation(UniversalBaseModel):
    construct_folder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="constructFolderId"),
        pydantic.Field(
            alias="constructFolderId", description="API identifier of the folder in which to create the constructs"
        ),
    ]
    """
    API identifier of the folder in which to create the constructs
    """

    construct_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="constructSchemaId"),
        pydantic.Field(
            alias="constructSchemaId",
            description="API identifier of the schema to which the constructs should be assigned",
        ),
    ] = None
    """
    API identifier of the schema to which the constructs should be assigned
    """

    fragment_folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fragmentFolderId"),
        pydantic.Field(
            alias="fragmentFolderId",
            description="API identifier of the folder in which to create the fragments, if any. If not specified, fragments will not be created.",
        ),
    ] = None
    """
    API identifier of the folder in which to create the fragments, if any. If not specified, fragments will not be created.
    """

    fragment_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fragmentSchemaId"),
        pydantic.Field(
            alias="fragmentSchemaId",
            description="API identifier of the schema to which the constructs should be assigned. If specified, `fragmentFolderId` must also be specified.",
        ),
    ] = None
    """
    API identifier of the schema to which the constructs should be assigned. If specified, `fragmentFolderId` must also be specified.
    """

    primer_folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="primerFolderId"),
        pydantic.Field(
            alias="primerFolderId",
            description="API identifier of the folder in which to create the primers, if any. If not specified, primers will not be created as Benchling oligos, but will still be referencable in the context of the assembly, if they were designed.",
        ),
    ] = None
    """
    API identifier of the folder in which to create the primers, if any. If not specified, primers will not be created as Benchling oligos, but will still be referencable in the context of the assembly, if they were designed.
    """

    primer_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="primerSchemaId"),
        pydantic.Field(
            alias="primerSchemaId",
            description="API identifier of the schema to which the primers should be assigned. If specified, `primerFolderId` must also be specified.",
        ),
    ] = None
    """
    API identifier of the schema to which the primers should be assigned. If specified, `primerFolderId` must also be specified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
