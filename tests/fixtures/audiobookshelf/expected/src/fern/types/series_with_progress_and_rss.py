

import typing

from .series import Series
from .series_with_progress_and_rss_progress import SeriesWithProgressAndRssProgress

SeriesWithProgressAndRss = typing.Union[Series, SeriesWithProgressAndRssProgress]
