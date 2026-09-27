

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PostApiBridgeReadRequestGetParameterValuesData(UniversalBaseModel):
    model_uid: typing_extensions.Annotated[str, FieldMetadata(alias="ModelUID"), pydantic.Field(alias="ModelUID")]
    ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="Ids"), pydantic.Field(alias="Ids")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
