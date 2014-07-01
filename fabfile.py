import os

from fabric.api import *

@task(alias='l')
def localhost():
    """Sets up environment for use on localhost"""
    env.run = local
    env.project_venv = os.getenv('DHP_VENV')
    env.project_path = os.getenv('DHP_PATH')

@task(alias='r')
def remote():
    """Sets up environment for use on remote machine"""
    env.hosts = ['www@danehillard.com']
    env.key_filename = os.getenv('DHP_KEY_FILE')
    env.run = run
    env.project_venv = 'dhp'
    env.project_path = 'dhp'

@task
def manage(*args):
    """Runs `./manage.py {args}`"""
    with prefix('workon {venv}'.format(venv=env.project_venv)):
        env.run('./manage.py {args}'.format(args=' '.join(args)))

@task
def sass(search_path='.'):
    """Compiles SASS files in place as CSS."""
    env.run('for file in `find {path} -name "*.sass"`; do sass $file:${{file%.sass}}.css; done'.format(
        path=search_path
    ))

@task
def static():
    """Runs 'sass' and 'collectstatic' tasks"""
    sass()
    collectstatic()

@task
def collectstatic():
    """Runs `./manage.py collectstatic --noinput -i *.sass`"""
    manage('collectstatic --noinput -i *.sass')

@task
def syncdb():
    """Runs `./manage.py syncdb --noinput`"""
    manage('syncdb --noinput')

@task
def migrate(*args):
    """Runs `./manage.py migrate --noinput {args}`"""
    manage('migrate --noinput {args}'.format(args=' '.join(args)))

@task
def db():
    """Runs 'syncdb' and 'migrate' tasks"""
    syncdb()
    migrate()

@task
def stage():
    """Prompts user about each chunk of changed code, adds them to the commit, then commits and pushes them."""
    git_add('-p')
    git_commit()
    git_push()

@task
def reload():
    """Touches WSGI file to reload the app in the webserver"""
    env.run('touch apache/django.wsgi')

@task
def git_pull(repository='', branch=''):
    """Runs `git pull {repo} {branch}`"""
    env.run('git pull {repo} {br}'.format(repo=repository, br=branch))

@task
def git_push(repository='', branch=''):
    """Runs `git push {repo} {branch}`"""
    env.run('git push {repo} {br}'.format(repo=repository, br=branch))

@task
def git_commit(*args):
    """Runs `git commit {args}`"""
    env.run('git commit {args}'.format(args=' '.join(args)))

@task
def git_add(*args):
    """Runs `git add {args}`"""
    env.run('git add {args}'.format(args=' '.join(args)))

@task
def deps():
    """Updates dependencies via `pip install -r requirements.txt`"""
    with prefix('workon {venv}'.format(venv=env.project_venv)):
        env.run('pip install --upgrade -r requirements.txt')

@task
def deploy():
    """Runs 'git_pull', 'db', 'static', 'deps', 'reload'"""
    with cd(env.project_path):
        git_pull()
        deps()
        db()
        static()
        reload()
