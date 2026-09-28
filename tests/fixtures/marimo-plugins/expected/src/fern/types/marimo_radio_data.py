

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoRadioData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ] = None
    inline: typing.Optional[bool] = None
    label: typing.Optional[str] = None
    options: typing.List[str]
    disabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
