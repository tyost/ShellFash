'''
Provides dependency injection.
'''
import inject
inject.configure_once()

#
# Methods exposed from inject.
#


def params(*args, **kwargs):
    return inject.params(*args, **kwargs)
params.__doc__ = inject.params.__doc__