

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserLegalNameListing(UniversalBaseModel):
    legal_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    All legal names that can be used by the user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
