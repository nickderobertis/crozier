

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.users import Users


class PatchUsersResponse(UniversalBaseModel):
    message: typing.Optional[str] = None
    errors: typing.Optional[typing.List[str]] = None
    docs: typing.Optional[typing.List[Users]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
