

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkTokenCreateInstitutionData(UniversalBaseModel):
    """
    A map containing data used to highlight institutions in Link.
    """

    routing_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The routing number of the bank to highlight.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
