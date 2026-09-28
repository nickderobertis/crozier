

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoCheckboxData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        bool, FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    label: typing.Optional[str] = None
    disabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
