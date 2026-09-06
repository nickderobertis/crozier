

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommunicationModelsFileUploadIndexField(UniversalBaseModel):
    field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Field"),
        pydantic.Field(alias="Field", description="The name of the file upload index field"),
    ] = None
    """
    The name of the file upload index field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
