



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_dpp_result import CreateDppResult
    from .data_element import (
        DataElement,
        DataElement_DataElementCollection,
        DataElement_MultiLanguageDataElement,
        DataElement_MultiValuedDataElement,
        DataElement_RelatedResource,
        DataElement_SingleValuedDataElement,
    )
    from .data_element_base import DataElementBase
    from .data_element_collection import DataElementCollection
    from .digital_product_passport import DigitalProductPassport
    from .digital_product_passport_compressed import DigitalProductPassportCompressed
    from .digital_product_passport_full import DigitalProductPassportFull
    from .dpp_envelope import DppEnvelope
    from .dpp_id_page import DppIdPage
    from .dpp_status import DppStatus
    from .granularity import Granularity
    from .identifier import Identifier
    from .message import Message
    from .message_type_enum import MessageTypeEnum
    from .multi_language_data_element import MultiLanguageDataElement
    from .multi_language_value import MultiLanguageValue
    from .multi_valued_data_element import MultiValuedDataElement
    from .multi_valued_data_element_value_item import MultiValuedDataElementValueItem
    from .multi_valued_data_element_value_item_zero import MultiValuedDataElementValueItemZero
    from .register_result import RegisterResult
    from .related_resource import RelatedResource
    from .result import Result
    from .single_valued_data_element import SingleValuedDataElement
    from .single_valued_data_element_value import SingleValuedDataElementValue
    from .status_code import StatusCode
    from .timestamp import Timestamp
_dynamic_imports: typing.Dict[str, str] = {
    "CreateDppResult": ".create_dpp_result",
    "DataElement": ".data_element",
    "DataElementBase": ".data_element_base",
    "DataElementCollection": ".data_element_collection",
    "DataElement_DataElementCollection": ".data_element",
    "DataElement_MultiLanguageDataElement": ".data_element",
    "DataElement_MultiValuedDataElement": ".data_element",
    "DataElement_RelatedResource": ".data_element",
    "DataElement_SingleValuedDataElement": ".data_element",
    "DigitalProductPassport": ".digital_product_passport",
    "DigitalProductPassportCompressed": ".digital_product_passport_compressed",
    "DigitalProductPassportFull": ".digital_product_passport_full",
    "DppEnvelope": ".dpp_envelope",
    "DppIdPage": ".dpp_id_page",
    "DppStatus": ".dpp_status",
    "Granularity": ".granularity",
    "Identifier": ".identifier",
    "Message": ".message",
    "MessageTypeEnum": ".message_type_enum",
    "MultiLanguageDataElement": ".multi_language_data_element",
    "MultiLanguageValue": ".multi_language_value",
    "MultiValuedDataElement": ".multi_valued_data_element",
    "MultiValuedDataElementValueItem": ".multi_valued_data_element_value_item",
    "MultiValuedDataElementValueItemZero": ".multi_valued_data_element_value_item_zero",
    "RegisterResult": ".register_result",
    "RelatedResource": ".related_resource",
    "Result": ".result",
    "SingleValuedDataElement": ".single_valued_data_element",
    "SingleValuedDataElementValue": ".single_valued_data_element_value",
    "StatusCode": ".status_code",
    "Timestamp": ".timestamp",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "CreateDppResult",
    "DataElement",
    "DataElementBase",
    "DataElementCollection",
    "DataElement_DataElementCollection",
    "DataElement_MultiLanguageDataElement",
    "DataElement_MultiValuedDataElement",
    "DataElement_RelatedResource",
    "DataElement_SingleValuedDataElement",
    "DigitalProductPassport",
    "DigitalProductPassportCompressed",
    "DigitalProductPassportFull",
    "DppEnvelope",
    "DppIdPage",
    "DppStatus",
    "Granularity",
    "Identifier",
    "Message",
    "MessageTypeEnum",
    "MultiLanguageDataElement",
    "MultiLanguageValue",
    "MultiValuedDataElement",
    "MultiValuedDataElementValueItem",
    "MultiValuedDataElementValueItemZero",
    "RegisterResult",
    "RelatedResource",
    "Result",
    "SingleValuedDataElement",
    "SingleValuedDataElementValue",
    "StatusCode",
    "Timestamp",
]
