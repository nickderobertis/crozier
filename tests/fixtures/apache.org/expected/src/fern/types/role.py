

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_resource import ActionResource


class Role(UniversalBaseModel):
    """
    a role item.

    *New in version 2.1.0*
    """

    actions: typing.Optional[typing.List[ActionResource]] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the role
    
    *Changed in version 2.3.0*&#58; A minimum character length requirement ('minLength') is added.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
