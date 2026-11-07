

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetDraftRegistrationsDraftIdResponseAttributesNodeLicense(UniversalBaseModel):
    copyright_holders: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of names of copyright holders for the license.
    """

    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    The year the copyright was made.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
