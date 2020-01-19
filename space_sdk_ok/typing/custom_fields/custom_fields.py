from ..base_type import (
    RecordType,
    RequestType
)
from ..consts import CF_values


class CustomField(RequestType):
    id: str

    arenaId: str


class CustomFieldValue(RequestType):
    field: CustomField

    value: CF_values


class CustomFieldValues(RequestType):
    customFieldValues: [CustomFieldValue]
g

class CustomColumnValuesWithSchemaData(RecordType):
    pass


class customFields(RecordType):
    CustomColumnValuesWithSchemaData: CustomColumnValuesWithSchemaData
