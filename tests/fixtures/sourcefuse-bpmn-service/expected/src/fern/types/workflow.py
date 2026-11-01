

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Workflow(UniversalBaseModel):
    deleted: typing.Optional[bool] = None
    deleted_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="deletedOn"), pydantic.Field(alias="deletedOn")
    ] = None
    deleted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deletedBy"), pydantic.Field(alias="deletedBy")
    ] = None
    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdOn"), pydantic.Field(alias="createdOn")
    ] = None
    modified_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modifiedOn"), pydantic.Field(alias="modifiedOn")
    ] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    modified_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")
    ] = None
    id: typing.Optional[str] = None
    workflow_version: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="workflowVersion"),
        pydantic.Field(alias="workflowVersion", description="Last deployed workflow version"),
    ]
    """
    Last deployed workflow version
    """

    external_identifier: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="externalIdentifier"),
        pydantic.Field(
            alias="externalIdentifier",
            description="The key that is used to identify the workflow in the respective workflow engine.",
        ),
    ]
    """
    The key that is used to identify the workflow in the respective workflow engine.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the workflow
    """

    provider: str = pydantic.Field()
    """
    Provider could be the engine that will handle the workflow - camunda, zeebe, etc
    """

    input_schema: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="inputSchema"),
        pydantic.Field(alias="inputSchema", description="Schema used for validation during workflow execution"),
    ]
    """
    Schema used for validation during workflow execution
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the workflow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
