

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SignalPersonName(UniversalBaseModel):
    """
    The user's legal name
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's family name / surname
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's given name. If the user has a one-word name, it should be provided in this field.
    """

    middle_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's middle name
    """

    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's name prefix (e.g. "Mr.")
    """

    suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's name suffix (e.g. "II")
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
