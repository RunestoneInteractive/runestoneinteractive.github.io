import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
import pkg_resources

sys.path.append(os.getcwd())
sys.path.append('../modules')


######## CHANGE THIS ##########
project_name = "html"
###############################

master_url = 'https://runestone.academy'
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
            'use_services': 'false',
            'python3': 'true',
            'jobe_server': 'https://cryptic-headland-94862.herokuapp.com/http://jobe2.cosc.canterbury.ac.nz',
            'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
            'proxy_uri_files': '/jobe/index.php/restapi/files/'
        }
    )
)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version


from runestone import build  # build is called implicitly by the paver driver.
