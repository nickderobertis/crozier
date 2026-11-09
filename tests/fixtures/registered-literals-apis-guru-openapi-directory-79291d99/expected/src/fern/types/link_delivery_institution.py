

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkDeliveryInstitution(UniversalBaseModel):
    """
    Information related to the financial institution.
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid institution identifier
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full institution name, such as 'Wells Fargo'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
