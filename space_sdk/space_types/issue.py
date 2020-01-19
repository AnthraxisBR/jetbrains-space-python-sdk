from space_sdk.space_types import Empty
from space_sdk.object_types.base_type import RequestType
from space_sdk.space_types.check_types import (
    is_nullable, required, is_str, is_date, is_list, is_bool
)


class Issue(RequestType):
    title: list = [required, is_str]

    description: list = [is_nullable, is_str]

    assignee: list = [is_nullable, is_str]

    status: list = [required, is_str]

    dueDate: list = [is_nullable, is_date]

    tags: list = [required, is_list]

    def __init__(self, title: str = Empty, description=Empty, assignee: str = Empty, status: str = Empty, dueDate: str = Empty, tags: list = Empty):
        """

        :param title:
        :param description:
        :param assignee:
        :param status:
        :param dueDate:
        :param tags:
        """
        self.title.append(title)
        self.description.append(description)
        self.assignee.append(assignee)
        self.status.append(status)
        self.dueDate.append(dueDate)
        self.tags.append(tags)

        super(Issue, self).__init__()

    def __todict__(self, kind=None):
        """

        :param kind:
        :return:
        """
        self.validate_object()

        if kind is None or kind == 'create':
            self.only_available_attrs(['title', 'description', 'assignee', 'status', 'dueDate', 'tags'])
            return self.validated_dict
        elif kind == 'update':
            self.not_allowed_attr('tags')
            return self.validated_dict


class IssueResolved(RequestType):
    resolved: list = [required, is_bool]

    def __init__(self, resolved: bool = Empty):
        """

        :param resolved:
        """
        self.resolved.append(resolved)
        super(IssueResolved, self).__init__()


    def __todict__(self):
        """

        :return:
        """
        self.validate_object()

        self.only_available_attrs(['resolved'])
        return self.validated_dict