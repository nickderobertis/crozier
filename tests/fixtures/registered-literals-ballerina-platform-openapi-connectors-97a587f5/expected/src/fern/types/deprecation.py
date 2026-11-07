

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Deprecation(UniversalBaseModel):
    """
    Defines the dates of deprecation for the different use cases of a model.
    Usually base models support 1 year of fine tuning after creation. Inference is typically supported 2 years after creation of base or
    fine tuned models. The exact dates are specified in the properties.
    """

    fine_tune: typing.Optional[int] = pydantic.Field(default=None)
    """
    The end date of fine tune support of this model. Will be `null` for fine tune models.
    """

    inference: int = pydantic.Field()
    """
    The end date of inference support of this model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
