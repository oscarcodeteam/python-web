from fabric.api import run, task

# CD
@task
def pull():
    run('cd python-web && git pull')