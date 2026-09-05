

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .product_template_get import ProductTemplateGet


class ProductGet(UniversalBaseModel):
    name: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    short_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shortName"),
        pydantic.Field(alias="shortName", description="Short display name for SMS"),
    ] = None
    """
    Short display name for SMS
    """

    vendor: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    vendor attributes
    """

    issues: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Reference to issues tracker
    """

    manuals: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    List of manuals
    """

    support: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    List of support resources
    """

    login_settings: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="loginSettings"), pydantic.Field(alias="loginSettings")
    ]
    max_open_studies_per_user: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxOpenStudiesPerUser"),
        pydantic.Field(alias="maxOpenStudiesPerUser"),
    ] = None
    is_payment_enabled: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isPaymentEnabled"), pydantic.Field(alias="isPaymentEnabled")
    ]
    credits_per_usd: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="creditsPerUsd"), pydantic.Field(alias="creditsPerUsd")
    ] = None
    templates: typing.Optional[typing.List[ProductTemplateGet]] = pydantic.Field(default=None)
    """
    List of templates available to this product for communications (e.g. emails, sms, etc)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
