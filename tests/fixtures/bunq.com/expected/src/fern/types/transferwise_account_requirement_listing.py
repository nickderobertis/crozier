

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transferwise_requirement_field import TransferwiseRequirementField


class TransferwiseAccountRequirementListing(UniversalBaseModel):
    fields: typing.Optional[typing.List[TransferwiseRequirementField]] = pydantic.Field(default=None)
    """
    The fields which the user needs to fill.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label of the possible recipient account type to show to the user.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A possible recipient account type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
