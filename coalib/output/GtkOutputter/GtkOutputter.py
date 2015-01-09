"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import os
from coalib.misc.StringConstants import StringConstants
from coalib.output.ColorPrinter import ColorPrinter
from coalib.output.LOG_LEVEL import LOG_LEVEL
from coalib.output.LogPrinter import LogPrinter
from coalib.output.Outputter import Outputter
from gi.repository import Gtk


class GtkOutputter(LogPrinter, ColorPrinter, Outputter):
    def __init__(self, log_level=LOG_LEVEL.WARNING, timestamp_format="%X"):
        LogPrinter.__init__(self, log_level=log_level, timestamp_format=timestamp_format)
        ColorPrinter.__init__(self)
        Outputter.__init__(self)

        path = os.path.join(StringConstants.coalib_root, "output", "GtkOutputter", "ui", "main_window.xml")
        builder = Gtk.Builder()
        builder.add_from_file(path)
        handlers = {
            "onDeleteWindow": Gtk.main_quit,
            "onPressMePressed": lambda x: print("hellp")
        }
        builder.connect_signals(handlers)

        window = builder.get_object("main_window")
        window.show_all()
        Gtk.main()
