# -*- coding: utf-8 -*-
# Standard library imports
from contextlib import contextmanager

# Local imports
from .dialogs import ProgressDialog


def disable_when_suppressed(fn):
    '''Disables the method when the suppressed flag is enabled.'''

    def run(self, *args, **kwargs):
        if not self._suppressed:
            return fn(self, *args, **kwargs)
    return run


class UIReporter(object):
    '''A reporter for cpenv that displays reports in a ProgresDialog.'''

    def __init__(self, app, engine):
        self._dialog = None
        self._suppressed = False
        self.app = app
        self.engine = engine

    @property
    def dialog(self):
        '''Get the ProgressDialog'''

        if self._dialog is None:
            self._dialog = ProgressDialog(self.engine._get_dialog_parent())
        return self._dialog

    @contextmanager
    def suppressed(self):
        '''Context manager that suppresses the reporting dialog.'''
        try:
            self._suppressed = True
            yield
        finally:
            self._suppressed = False

    @disable_when_suppressed
    def start_resolve(self, requirements):
        '''Called when a Resolver.resolve is called with some requirements.'''

        max_size = len(requirements)
        self.dialog.show()
        self.dialog.set_label('Resolving requirements')
        self.dialog.set_progress(max_size=max_size)

    @disable_when_suppressed
    def find_requirement(self, requirement):
        '''Called just before attempting to resolve a requirement.'''

        value, max_value = self.dialog.value(), self.dialog.max_value()
        self.dialog.set_frame('{} of {} - {}...'.format(
            value + 1,
            max_value,
            requirement,
        ))

    @disable_when_suppressed
    def resolve_requirement(self, requirement, module_spec):
        '''Called when a a requirement is resolved.'''

        self.dialog.set_progress(chunk_size=1)

    @disable_when_suppressed
    def end_resolve(self, resolved, unresolved):
        '''Called when Resolver.resolve is done.'''

        if unresolved:
            self.dialog.error(
                label='Failed to resolve',
                message='\n  '.join(unresolved),
            )
        else:
            self.dialog.set_label('Done!')
            self.dialog.hide()

    @disable_when_suppressed
    def start_localize(self, module_specs):
        '''Called when Localizer.localize is called with a list of specs.'''

        max_size = len(module_specs)
        self._count = 1
        self._total = max_size
        self.dialog.show()
        self.dialog.set_label('Localizing modules')
        self.dialog.set_progress(max_size=max_size)

    @disable_when_suppressed
    def localize_module(self, module_spec, module):
        '''Called when a module is localized.'''

        self.dialog.set_frame('{} of {} - {}...'.format(
            self._count,
            self._total,
            module_spec.qual_name,
        ))
        self._count += 1

    @disable_when_suppressed
    def end_localize(self, localized):
        '''Called when Localizer.localize is done.'''

        self.dialog.set_label('Localized %s modules!' % len(localized))
        self.dialog.hide()

    @disable_when_suppressed
    def start_progress(self, label, max_size, data):
        '''Called when a download is started.'''
        self.dialog.set_progress(max_size=max_size)

    @disable_when_suppressed
    def update_progress(self, label, chunk_size, data):
        '''Called each time a chunk is downloaded.'''
        self.dialog.set_progress(chunk_size=chunk_size)

    @disable_when_suppressed
    def end_progress(self, label, data):
        '''Called when a download is finished.'''
