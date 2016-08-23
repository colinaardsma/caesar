#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

form = """
<form method="post">
    <label>Amount to Shift:
        <input type="number" name="shift" />
    </label>
    <label><h1>Enter Some Text</h1>
        <textarea name="text" style="height: 10em; width: 40em;">%(text)s</textarea>
    </label><br>
    <input type="submit" />
</form>
"""

def shift(text, shift):
    text = cgi.escape(text)
    shift = int(cgi.escape(shift)) % 26
    new = ""
    for char in text:
        if char.isalpha() == True:
            newCharNum = ord(char) + shift
            if char.isupper() == True:
                if newCharNum > ord('Z'):
                    newCharNum -= 26
                    newChar = chr(newCharNum)
                else:
                    newChar = chr(newCharNum)
            else:
                if newCharNum > ord('z'):
                    newCharNum -= 26
                    newChar = chr(newCharNum)
                else:
                    newChar = chr(newCharNum)
        else:
            newChar = char
        new += newChar
    return new

class MainHandler(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.write(form % {"text": text})

    def get(self):
        self.write_form()

    def post(self):
        text = shift(self.request.get('text'), self.request.get('shift'))
        self.write_form(text)
        #self.response.write(text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
