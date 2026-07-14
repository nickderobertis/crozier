

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TelnetUser(UniversalBaseModel):
    groups: typing.Optional[typing.List[str]] = None
    has_password: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="hasPassword")] = None
    password: typing.Optional[str] = None
    username: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
