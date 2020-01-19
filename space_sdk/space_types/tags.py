from space_sdk.space_types import Empty
from space_sdk.object_types.base_type import RequestType
from space_sdk.space_types.check_types import (
    is_nullable, required, is_str, is_list
)


class HierarchicalTag(RequestType):
    parentTagId: list = [is_nullable, is_str]

    path: list = [required, is_list]

    def __init__(self, parentTagId: str = Empty, path: list = Empty):
        """

        :param parentTagId:
        :param path:
        """
        self.parentTagId.append(parentTagId)
        self.path.append(path)
        super(HierarchicalTag, self).__init__()

    def __todict__(self):
        """

        :return:
        """
        self.validate_object()

        self.only_available_attrs(['parentTagId', 'path'])
        return self.validated_dict
