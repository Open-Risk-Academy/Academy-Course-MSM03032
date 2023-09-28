"""
   Copyright 2022 - 2023 Open Risk (www.openriskmanagement.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from pymongo import Connection
db = Connection().map_reduce_example
db.things.insert({"x": 1, "tags": ["dog", "cat"]})
db.things.insert({"x": 2, "tags": ["cat"]})
db.things.insert({"x": 3, "tags": ["mouse", "cat", "dog"]})
db.things.insert({"x": 4, "tags": []})

map = Code("function () {"
            "  this.tags.forEach(function(z) {"
            "    emit(z, 1);"
            "  });"
            "}")

reduce = Code("function (key, values) {"
               "  var total = 0;"
               "  for (var i = 0; i < values.length; i++) {"
               "    total += values[i];"
               "  }"
               "  return total;"
               "}")

result = db.things.map_reduce(map, reduce, "myresults")
for doc in result.find():
   print(doc)