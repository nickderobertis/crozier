

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2LogListItemWorkflow(UniversalBaseModel):
    """
    Workflow summary for a full-detail result.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workflow identifier, or null when unavailable.
    """

    name: str = pydantic.Field()
    """
    Workflow name.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workflow description, or null when unset.
    """

    deleted: bool = pydantic.Field()
    """
    Whether the workflow has been deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
