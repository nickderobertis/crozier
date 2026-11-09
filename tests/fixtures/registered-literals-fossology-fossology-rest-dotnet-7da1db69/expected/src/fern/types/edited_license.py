

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EditedLicense(UniversalBaseModel):
    id: typing.Optional[int] = None
    short_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="shortName"), pydantic.Field(alias="shortName")
    ] = None
    count: typing.Optional[int] = None
    spdx_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
