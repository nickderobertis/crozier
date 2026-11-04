

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesDraftRegistrationsSubjectsResponseRelationships(UniversalBaseModel):
    """
    Links to other entities or entity collections that have a relationship to the file entity.
    """

    children: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the children for this Subject.
    """

    parent: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the parent for this Subject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
