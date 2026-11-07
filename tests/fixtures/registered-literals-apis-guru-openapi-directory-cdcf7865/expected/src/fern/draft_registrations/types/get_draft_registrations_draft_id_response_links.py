

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetDraftRegistrationsDraftIdResponseLinks(UniversalBaseModel):
    """
    URLs to alternative representations of the draft registration entity.
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the draft registration's page on the OSF.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
