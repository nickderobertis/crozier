

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesDraftRegistrationsSubjectsResponseAttributes(UniversalBaseModel):
    """
    The attributes of the Subject.
    """

    taxonomy_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the taxonomy used to name subjects (`bepress`)
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the subject (`Arts and Humanities`)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
