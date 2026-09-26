

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ProjectsCreateProjectLabelsItem(UniversalBaseModel):
    label_id: float = pydantic.Field()
    """
    Tag ID
    """

    budget: typing.Optional[float] = pydantic.Field(default=None)
    """
    Budget allocated for this tag
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this tag is required for time entries
    """

    default: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this tag is selected by default
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
