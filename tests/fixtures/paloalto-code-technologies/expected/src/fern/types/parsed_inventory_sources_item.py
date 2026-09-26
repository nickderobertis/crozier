

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .parsed_inventory_sources_item_arguments import ParsedInventorySourcesItemArguments


class ParsedInventorySourcesItem(UniversalBaseModel):
    arguments: typing.Optional[ParsedInventorySourcesItemArguments] = pydantic.Field(default=None)
    """
    Pipeline tool arguments
    """

    cas_id: typing_extensions.Annotated[str, FieldMetadata(alias="casId"), pydantic.Field(alias="casId")]
    file_path: typing_extensions.Annotated[
        str, FieldMetadata(alias="filePath"), pydantic.Field(alias="filePath", description="Pipeline tool CI file path")
    ]
    """
    Pipeline tool CI file path
    """

    line_number: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="lineNumber"),
        pydantic.Field(alias="lineNumber", description="Pipeline tool line number in CI file"),
    ]
    """
    Pipeline tool line number in CI file
    """

    name: str = pydantic.Field()
    """
    Pipeline tool name
    """

    repo_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="repoId"), pydantic.Field(alias="repoId", description="VCS repository ID")
    ]
    """
    VCS repository ID
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="VCS workspace/integration ID"),
    ]
    """
    VCS workspace/integration ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
