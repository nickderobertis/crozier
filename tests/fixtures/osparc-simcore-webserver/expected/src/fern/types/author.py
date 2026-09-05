

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lower_case_email_str import LowerCaseEmailStr


class Author(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the author
    """

    email: LowerCaseEmailStr = pydantic.Field()
    """
    Email address
    """

    affiliation: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
