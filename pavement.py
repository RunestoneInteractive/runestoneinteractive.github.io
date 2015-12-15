import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

sys.path.append(os.getcwd())
sys.path.append('../modules')


######## CHANGE THIS ##########
project_name = "html"
###############################

master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = './build/html'
dest = '../../static'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/"+project_name,
        sourcedir="source",
        outdir="./build/"+project_name,
        confdir="source",
        project_name = project_name,
        template_args = {
            'course_id':project_name,
            'login_required':'false',
            'appname':master_app,
            'loglevel':0,
            'course_url':master_url,
            'use_services': 'true',
            'python3': 'true',
        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.
