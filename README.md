# aboo
Aph's Banana-based Obscure Observations.
An API for banana.
## Installation
```bash
pip install aboo
```
or clone the repo
```bash
git clone repo
```
## Example Usage
```py
import io

from aboo import Banana
from PIL import Image

my_api_key = "my_api_key"
my_cse_id = "my_cse_id"
banana = Banana(my_api_key, my_cse_id)
im = Image.open(io.BytesIO(banana.get_random_banana()))
im.show()
```
## License
MIT