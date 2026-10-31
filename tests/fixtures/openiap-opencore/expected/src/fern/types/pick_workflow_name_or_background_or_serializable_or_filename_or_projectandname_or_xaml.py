

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PickWorkflowNameOrBackgroundOrSerializableOrFilenameOrProjectandnameOrXaml(UniversalBaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """

    name: str
    background: bool
    serializable: typing_extensions.Annotated[
        bool, FieldMetadata(alias="Serializable"), pydantic.Field(alias="Serializable")
    ]
    filename: typing_extensions.Annotated[str, FieldMetadata(alias="Filename"), pydantic.Field(alias="Filename")]
    projectandname: str
    xaml: typing_extensions.Annotated[str, FieldMetadata(alias="Xaml"), pydantic.Field(alias="Xaml")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
