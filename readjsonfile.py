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

import json
import numpy as np
filehandle = open("portfolio2.json","r")
json_data= filehandle.read()
data = json.loads(json_data)

x = np.array(data['Exposure'])    