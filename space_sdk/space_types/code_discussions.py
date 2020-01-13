from space_sdk.space_types import Empty
from space_sdk.object_types.base_type import RequestType
from space_sdk.space_types.check_types import (
    is_nullable, required, is_str, is_list
)


class GitFile(RequestType):
    commit: str = [required, is_str]
    path: str = [required, is_str]
    blob: str = [required, is_str]
    type: str = [required, is_str]

    def __todict__(self):
        """

        :return:
        """
        self.validate_object()

        self.only_available_attrs(['commit', 'path', 'blob', 'type'])
        return self.validated_dict


class GitCommitChange(RequestType):
    change_type: str = [required]

    old: GitFile = [is_nullable]

    new: GitFile = [is_nullable]

    revision: str = [required, is_str]

    def __todict__(self):
        """

        :return:
        """
        self.validate_object()

        self.only_available_attrs(['commit', 'path', 'blob', 'type'])
        return self.validated_dict


class CodeDiscussionsByChange(RequestType):
    revisions: list = [required, is_list]

    change: GitCommitChange = [is_nullable, is_str]

    def __init__(self, title: str = Empty, description=Empty, assignee: str = Empty, status: str = Empty,
                 dueDate: str = Empty, tags: list = Empty):
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
