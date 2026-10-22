

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurveyHiddenFields(UniversalBaseModel):
    """
    Hidden fields configuration
    """

    enabled: bool
    field_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="fieldIds"), pydantic.Field(alias="fieldIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
