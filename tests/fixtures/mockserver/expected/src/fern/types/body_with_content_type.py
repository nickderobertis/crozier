

import typing

from .body_with_content_type_base64bytes import BodyWithContentTypeBase64Bytes
from .body_with_content_type_content_type import BodyWithContentTypeContentType
from .body_with_content_type_json import BodyWithContentTypeJson
from .body_with_content_type_string import BodyWithContentTypeString
from .body_with_content_type_xml import BodyWithContentTypeXml

BodyWithContentType = typing.Union[
    BodyWithContentTypeBase64Bytes,
    BodyWithContentTypeJson,
    typing.Dict[str, typing.Any],
    BodyWithContentTypeString,
    str,
    BodyWithContentTypeXml,
    BodyWithContentTypeContentType,
]
