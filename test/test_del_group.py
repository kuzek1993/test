
import time
def test_delete_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.group.return_to_group()
    app.session.logout()
    time.sleep(1)