

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.license import License
from ...types.obligation import Obligation


class GetLicenseByShortnameResponse(License):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id key
    """

    obligations: typing.Optional[typing.List[Obligation]] = pydantic.Field(default=None)
    """
    Obligations associated with the license
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
