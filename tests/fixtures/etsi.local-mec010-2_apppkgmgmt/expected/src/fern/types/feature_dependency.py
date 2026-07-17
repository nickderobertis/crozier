

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FeatureDependency(UniversalBaseModel):
    feature_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="featureName"),
        pydantic.Field(
            alias="featureName", description="The name of the feature, for example, UserApps, UEIdentity, etc."
        ),
    ]
    """
    The name of the feature, for example, UserApps, UEIdentity, etc.
    """

    version: str = pydantic.Field()
    """
    The version of the feature.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
