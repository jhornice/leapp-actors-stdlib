class LeappError(Exception):
    def __init__(self, message):
        super(LeappError, self).__init__(message)


class InvalidTopicItemError(LeappError):
    def __init__(self, message):
        super(InvalidTopicItemError, self).__init__(message)


class InvalidTopicDefinitionError(LeappError):
    def __init__(self, message):
        super(InvalidTopicDefinitionError, self).__init__(message)


class InvalidTagDefinitionError(LeappError):
    def __init__(self, message):
        super(InvalidTagDefinitionError, self).__init__(message)


class MissingActorAttributeError(LeappError):
    def __init__(self, message):
        super(MissingActorAttributeError, self).__init__(message)


class WrongAttributeTypeError(LeappError):
    def __init__(self, message):
        super(WrongAttributeTypeError, self).__init__(message)


class ModelDefinitionError(LeappError):
    def __init__(self, message):
        super(ModelDefinitionError, self).__init__(message)


class TagFilterUsageError(LeappError):
    def __init__(self, message):
        super(TagFilterUsageError, self).__init__(message)


class CyclingDependenciesError(LeappError):
    def __init__(self, message):
        super(CyclingDependenciesError, self).__init__(message)


class UnsupportedDefinitionKindError(LeappError):
    def __init__(self, message):
        super(UnsupportedDefinitionKindError, self).__init__(message)


class ModuleNameAlreadyExistsError(LeappError):
    def __init__(self, message):
        super(ModuleNameAlreadyExistsError, self).__init__(message)


class ActorInspectionFailedError(LeappError):
    def __init__(self, message):
        super(ActorInspectionFailedError, self).__init__(message)


class MultipleActorsError(LeappError):
    def __init__(self, path):
        super(MultipleActorsError, self).__init__(
            'Multiple actors found in {path}. Inspection failed'.format(path=path))


class RepoItemPathDoesNotExistError(LeappError):
    def __init__(self, kind, rel_path, full_path):
        super(RepoItemPathDoesNotExistError, self).__init__(
            'Could not find {kind} item with relative path: {rel_path} at {full_path}'.format(
                kind=kind, rel_path=rel_path, full_path=full_path))


class ActorDiscoveryExecutionError(LeappError):
    def __init__(self, message):
        super(ActorDiscoveryExecutionError, self).__init__(message)
