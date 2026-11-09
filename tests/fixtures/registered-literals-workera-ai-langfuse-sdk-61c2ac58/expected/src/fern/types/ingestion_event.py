

import typing

from .ingestion_event_eight import IngestionEventEight
from .ingestion_event_five import IngestionEventFive
from .ingestion_event_four import IngestionEventFour
from .ingestion_event_nine import IngestionEventNine
from .ingestion_event_one import IngestionEventOne
from .ingestion_event_seven import IngestionEventSeven
from .ingestion_event_six import IngestionEventSix
from .ingestion_event_three import IngestionEventThree
from .ingestion_event_two import IngestionEventTwo
from .ingestion_event_zero import IngestionEventZero

IngestionEvent = typing.Union[
    IngestionEventZero,
    IngestionEventOne,
    IngestionEventTwo,
    IngestionEventThree,
    IngestionEventFour,
    IngestionEventFive,
    IngestionEventSix,
    IngestionEventSeven,
    IngestionEventEight,
    IngestionEventNine,
]
