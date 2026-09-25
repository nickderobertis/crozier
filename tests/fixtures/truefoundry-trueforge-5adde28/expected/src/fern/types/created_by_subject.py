

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreatedBySubject(UniversalBaseModel):
    """
    Who created this resource.
    """

    subject_display_name: str = pydantic.Field()
    """
    Display name.
    """

    subject_id: str = pydantic.Field()
    """
    Subject id.
    """

    subject_type: str = pydantic.Field()
    """
    Subject type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
