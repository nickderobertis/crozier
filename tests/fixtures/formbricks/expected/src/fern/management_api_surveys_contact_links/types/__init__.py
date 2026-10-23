



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_contact_links_by_segment_response import GetContactLinksBySegmentResponse
    from .get_contact_links_by_segment_response_data_item import GetContactLinksBySegmentResponseDataItem
    from .get_contact_links_by_segment_response_meta import GetContactLinksBySegmentResponseMeta
    from .get_personalized_survey_link_response import GetPersonalizedSurveyLinkResponse
    from .get_personalized_survey_link_response_data import GetPersonalizedSurveyLinkResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "GetContactLinksBySegmentResponse": ".get_contact_links_by_segment_response",
    "GetContactLinksBySegmentResponseDataItem": ".get_contact_links_by_segment_response_data_item",
    "GetContactLinksBySegmentResponseMeta": ".get_contact_links_by_segment_response_meta",
    "GetPersonalizedSurveyLinkResponse": ".get_personalized_survey_link_response",
    "GetPersonalizedSurveyLinkResponseData": ".get_personalized_survey_link_response_data",
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
    "GetContactLinksBySegmentResponse",
    "GetContactLinksBySegmentResponseDataItem",
    "GetContactLinksBySegmentResponseMeta",
    "GetPersonalizedSurveyLinkResponse",
    "GetPersonalizedSurveyLinkResponseData",
]
