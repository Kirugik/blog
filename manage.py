from app import create_app
from flask_script import Manager,Server
from app.models import User, Post, Comment, Like  


# Creating app instance
app = create_app('development')    


# Instantiate Manager class by passing in the app instance
manager = Manager(app)



# Create a command line argument to tell us how to run our application
# Then, use the add_command method to create a new command 'server' which will launch the app server 
manager.add_command('server',Server) 

# @manager.command 
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests) 


@manager.shell 
def make_shell_context():
    return dict(app = app,User=User, Post=Post, Comment=Comment, Like=Like) 

# Calling the run method on the Manager instance(manager) to run the application 
if __name__ == '__main__': 
    manager.run() 