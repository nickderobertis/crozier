

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SequenceFeatureCustomField(UniversalBaseModel):
    """
    A name and value pair associated with a sequence feature (annotation or translation). For genbank imports, these are the qualifiers associated with each feature.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the custom field
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Value of the custom field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
