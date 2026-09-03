

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .purpose_type import PurposeType


class Purpose(UniversalBaseModel):
    """
    Relying Parties should indicate the purpose of using eSignet (e.g., for login, verification) during registration, allowing for specific customisation.
    """

    type: PurposeType
    title: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    It will appear in the screen as the title of login page. It will be multilingual language map and @none when no language map is present, @none is compulsory if you are providing title object.
    """

    sub_title: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="subTitle"),
        pydantic.Field(
            alias="subTitle",
            description="It will appear in the screen below the title of login page. It will also be multilingual language map and @none when no language map is present, @none is compulsory if you are providing subTitle object.",
        ),
    ] = None
    """
    It will appear in the screen below the title of login page. It will also be multilingual language map and @none when no language map is present, @none is compulsory if you are providing subTitle object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
