

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_list import ArtifactList
from .success import Success
from .warning_message import WarningMessage


class UpdateJobOutput(UniversalBaseModel):
    """
    Output structure for the UpateJob operation.
    """

    success: typing_extensions.Annotated[
        typing.Optional[Success], FieldMetadata(alias="Success"), pydantic.Field(alias="Success")
    ] = None
    warning_message: typing_extensions.Annotated[
        typing.Optional[WarningMessage], FieldMetadata(alias="WarningMessage"), pydantic.Field(alias="WarningMessage")
    ] = None
    artifact_list: typing_extensions.Annotated[
        typing.Optional[ArtifactList], FieldMetadata(alias="ArtifactList"), pydantic.Field(alias="ArtifactList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
