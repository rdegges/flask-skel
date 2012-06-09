"""Flask management script."""


from flaskext.script import Manager

from skel import app


# Build a manager instance:
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
