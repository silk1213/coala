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
from collections import OrderedDict
import sys

from coalib.parsing.LineParser import LineParser
from coalib.parsing.Parser import Parser
from coalib.settings.Setting import Setting
from coalib.settings.Settings import Settings
from coalib.misc.i18n import _


class ConfParser(Parser):
    def __init__(self,
                 key_value_delimiters=['=', ':'],
                 comment_seperators=['#', ';', '//'],
                 key_delimiters=[',', ' '],
                 section_name_surroundings={'[': "]"}):
        Parser.__init__(self)
        self.line_parser = LineParser(key_value_delimiters,
                                      comment_seperators,
                                      key_delimiters,
                                      section_name_surroundings)
        # Declare it
        self.sections = None
        self.__rand_helper = None
        self.__init_sections()

    def parse(self, input_data, overwrite=False):
        """
        Parses the input and adds the new data to the existing

        :param input_data: filename
        :param overwrite: behaves like reparse if this is True
        :return a non empty string containing an error message on failure
        """
        if sys.version_info < (3, 3):  # pragma: no cover
            err = IOError
        else:  # pragma: no cover
            err = FileNotFoundError

        try:
            f = open(input_data, "r", encoding='utf-8')
            lines = f.readlines()
            f.close()

            if overwrite:
                self.__init_sections()

            self.__parse_lines(lines, input_data)
        except err:
            return _("Failed reading file. Please make sure to provide a file that is existent and "
                     "you have the permission to read it.")

    def reparse(self, input_data):
        """
        Parses the input and overwrites all existent data

        :param input_data: filename
        :return a non empty string containing an error message on failure
        """
        return self.parse(input_data, overwrite=True)

    def export_to_settings(self):
        """
        :return a dict of Settings objects representing the current parsed things
        """
        return self.sections

    def get_section(self, name, create_if_not_exists=False):
        key = self.__refine_key(name)
        sec = self.sections.get(key, None)
        if sec is not None:
            return sec

        if not create_if_not_exists:
            raise IndexError

        retval = self.sections[key] = Settings(str(name), self.sections["default"])
        return retval

    @staticmethod
    def __refine_key(key):
        return str(key).lower().strip()

    def __add_comment(self, section, comment, origin):
        key = "COMMENT"+str(self.__rand_helper)
        self.__rand_helper += 1
        section._add_or_create_setting(Setting(comment, comment, origin), custom_key=key)

    def __parse_lines(self, lines, origin):
        current_section_name = "default"
        current_section = self.get_section(current_section_name)
        current_keys = []

        for line in lines:
            section_name, keys, value, comment = self.line_parser.parse(line)

            if comment is not "":
                self.__add_comment(current_section, comment, origin)

            if section_name != "":
                current_section_name = section_name
                current_section = self.get_section(current_section_name, True)
                current_keys = []
                continue

            if keys != []:
                current_keys = keys

            for key in current_keys:
                current_section._add_or_create_setting(Setting(key, value, origin),
                                                       allow_appending=(keys == []))

    def __init_sections(self):
        self.sections = OrderedDict()
        self.sections["default"] = Settings("Default")
        self.__rand_helper = 0