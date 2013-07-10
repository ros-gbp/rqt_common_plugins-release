# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from .base_filter import BaseFilter


class NodeFilter(BaseFilter):
    """
    Contains filter logic for a single node filter
    If the message's node text matches any of the text in the stored list
    then it is considered a match.
    """

    def __init__(self):
        super(NodeFilter, self).__init__()
        self._list = []

    def set_list(self, list_):
        """
        Setter for _list
        :param list_" list of items to store for filtering ''list of QListWidgetItem''
        :emits filter_changed_signal: If _enabled is true
        """
        self._list = list_
        if self.is_enabled():
            self.start_emit_timer()

    def test_message(self, message):
        """
        Tests if the message matches the filter.
        If the message's node text matches any of the text in the stored list
        then it is considered a match.
        :param message: the message to be tested against the filters, ''Message''
        :returns: True if the message matches, ''bool''
        """
        if self.is_enabled():
            for item in self._list:
                if message._node == item.text():
                    return True
        return False
