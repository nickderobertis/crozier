

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommunicationModelsFileUploadType(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The file upload type ID"),
    ] = None
    """
    The file upload type ID
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the file upload type"),
    ] = None
    """
    The name of the file upload type
    """

    name_string_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NameStringId"),
        pydantic.Field(alias="NameStringId", description="The string translation id of the file upload type"),
    ] = None
    """
    The string translation id of the file upload type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
