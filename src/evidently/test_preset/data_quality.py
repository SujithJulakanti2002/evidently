from typing import List
from typing import Optional

from evidently.base_metric import InputData
from evidently.test_preset.test_preset import TestPreset
from evidently.tests import TestAllColumnsMostCommonValueShare
from evidently.tests import TestAllColumnsShareOfMissingValues
from evidently.tests import TestHighlyCorrelatedColumns
from evidently.tests import TestNumberOfConstantColumns
from evidently.tests import TestNumberOfDuplicatedColumns
from evidently.tests import TestNumberOfDuplicatedRows
from evidently.utils.data_operations import DatasetColumns


class DataQualityTestPreset(TestPreset):
    """
    Data Quality tests.

    Contains tests:
    - `TestAllColumnsShareOfMissingValues`
    - `TestAllColumnsMostCommonValueShare`
    - `TestNumberOfConstantColumns`
    - `TestNumberOfDuplicatedColumns`
    - `TestNumberOfDuplicatedRows`
    - `TestHighlyCorrelatedColumns`
    """

    columns: Optional[List[str]]

    def __init__(
        self,
        columns: Optional[List[str]] = None,
    ):
        super().__init__()
        self.columns = columns

    def generate_tests(self, data: InputData, columns: DatasetColumns):
        return [
            TestAllColumnsShareOfMissingValues(columns=self.columns),
            TestAllColumnsMostCommonValueShare(columns=self.columns),
            TestNumberOfConstantColumns(),
            TestNumberOfDuplicatedColumns(),
            TestNumberOfDuplicatedRows(),
            TestHighlyCorrelatedColumns(),
        ]
