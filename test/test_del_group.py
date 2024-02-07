
import time
def test_delete_first_group(app):
    app.group.delete_first_group()
    app.group.return_to_group()
    time.sleep(1)