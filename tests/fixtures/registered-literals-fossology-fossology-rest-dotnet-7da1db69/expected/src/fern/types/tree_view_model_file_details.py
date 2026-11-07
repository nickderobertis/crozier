

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TreeViewModelFileDetails(UniversalBaseModel):
    """
    Details about the file.
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="The name of the file."),
    ] = None
    """
    The name of the file.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the item.
    """

    upload_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uploadId"),
        pydantic.Field(alias="uploadId", description="The ID of the upload."),
    ] = None
    """
    The ID of the upload.
    """

    agent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="agentId"),
        pydantic.Field(alias="agentId", description="The ID of the agent."),
    ] = None
    """
    The ID of the agent.
    """

    is_container: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isContainer"),
        pydantic.Field(alias="isContainer", description="Indicates if the item is a folder or file."),
    ] = None
    """
    Indicates if the item is a folder or file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
