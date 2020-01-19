from ..object_types.base_type import (
    RequestType
)

from ..space_types.check_types import (
    is_str, is_nullable, required
)

from ..space_types.custom_types import Empty


class Checklist(RequestType):
    projectId: list = [is_nullable]

    name: list = [required, is_str]

    description: list = [is_nullable, is_str]

    owner: list = [is_nullable, is_str]

    tag: list = [is_nullable, is_str]

    def __init__(self, name: str = Empty, projectId=Empty, owner: str = Empty, tag: str = Empty,
                 description: str = Empty):
        """

        :param name:
        :param projectId:
        :param owner:
        :param tag:
        :param description:
        """
        self.projectId.append(projectId)
        self.name.append(name)
        self.owner.append(owner)
        self.tag.append(tag)
        self.description.append(description)

        super(Checklist, self).__init__()

    def __todict__(self, kind=None):
        """

        :param kind:
        :return:
        """
        self.validate_object()

        if kind is None or kind == 'create':
            self.only_available_attrs(['description', 'owner', 'tag'])
            return self.validated_dict
        elif kind == 'update':
            self.not_allowed_attr('projectId')
            return self.validated_dict


class ChecklistImport(RequestType):
    """

    """
    projectId: list = [is_nullable]

    name: list = [required, is_str]

    tabIndentedLines: list = [required, is_str]

    def __init__(self, name: str = Empty, projectId=Empty, tabIndentedLines: str = Empty):
        """

        :param name:
        :param projectId:
        :param tabIndentedLines:
        """
        self.projectId.append(projectId)
        self.name.append(name)
        self.tabIndentedLines.append(tabIndentedLines)

        super(ChecklistImport, self).__init__()

    def __todict__(self):
        """

        :return:
        """
        self.validate_object()
        return self.validated_dict


class ChecklistImportLines(RequestType):
    """

    """
    targetParentId: list = [required, is_str]

    afterItemId: list = [is_nullable, is_str]

    tabIndentedLines: list = [required, is_str]

    def __init__(self, targetParentId: str = Empty, afterItemId=Empty, tabIndentedLines: str = Empty):
        """

        :param targetParentId:
        :param afterItemId:
        :param tabIndentedLines:
        """
        self.targetParentId.append(targetParentId)
        self.afterItemId.append(afterItemId)
        self.tabIndentedLines.append(tabIndentedLines)

        super(ChecklistImportLines, self).__init__()

    def __todict__(self):
        """"
        """
        self.validate_object()
        return self.validated_dict
