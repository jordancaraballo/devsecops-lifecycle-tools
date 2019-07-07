## Create gitlab issues using the API
## Purpose: Threat model for manual review sections
## Author: Jordan A Caraballo-Vega <jordancaraballo>
## REQUIREMENTS: packages <python-gitlab>
##               files <python-gitlab.cfg> or other config file
##               threat model <threat_model.md>
## Examples are placed in the examples directory for reference.
## To install python-gitlan with conda: conda install -c conda-forge python-gitlab
##-----------------------------------------------------------------------------------------
# Import Libraries
##-----------------------------------------------------------------------------------------
import gitlab       # python-gitlab API wrapper
import requests     # to create sessions
import configparser # to parse configuration file
##-----------------------------------------------------------------------------------------
# Function
##-----------------------------------------------------------------------------------------
# Input: ssl_components: dict
#        url: string
#        token: string
# Output: session to gitlab API
def init_session(ssl_cert, ssl_key, url, token, ssl_ver_bool=False):
    session = requests.Session()
    session.cert = (ssl_cert, ssl_key)
    gl = gitlab.Gitlab(url, token, session=session, ssl_verify=ssl_ver_bool)
    gl.auth()
    return gl

# Input: threat_model: string (filename)
# Output: list with sections and questions from threat model
def parse_file(threat_model):
    questions_list = list()
    with open(threat_model) as f:
        for line in f.readlines()[1:]:
            temp_line = line.strip().replace(" <br />", "").replace("# ", "").replace("#", "")
            if temp_line:
                questions_list.append(temp_line.split(': '))
    return questions_list

# Input: gitlab session (found at init_session)
# Output: list with all of the projects
def get_projects(gl):
    return gl.projects.list()

# Input: gitlab session (found at init_session)
# Output: list of specified project issues (issue objects)
def get_issues(gl, project_id):
    return gl.projects.get(project_id).issues.list()

# Input: gitlab session (found at init_session)
#        project_id: integer
#        issue_title: string
#        issue_description: string
def create_issues_one(gl, project_id, issue_title='Default', issue_description='Something'):
    issue = gl.projects.get(project_id).issues.create({'title': issue_title,
                                                       'description': issue_description})
    return 1

# Input: gitlab session (found at init_session)
#        project_id: integer
#        threat_model: filename string
# Output: creates and posts issues
def create_issues_mult(gl, threat_model):
    questions  = parse_file(threat_model) # parse threat_model file
    project_id = int(questions[1][1])     # get project id from file
    
    # Iterate over questions and section titles
    temp_title = ''
    for q in questions[2:]:
        if len(q) == 1:
            temp_title = q[0]
        else:
            # Temporarily creating issues for every question. Ideally, create an if statement
            # here to parse yes and no, or keywords to determine if issues need to be created.
            gl.projects.get(project_id).issues.create({'title': temp_title + " "  + q[0],
                                                       'description': q[1] + ": " + q[2]})
    return 1

# Just for reference: does not work at this time
def get_issues_all():
    open_issues = gl.issues.list(state='opened')
    closed_issues = gl.issues.list(state='closed')
    tagged_issues = gl.issues.list(labels=['foo', 'bar'])
##-----------------------------------------------------------------------------------------
# Main
##-----------------------------------------------------------------------------------------
if __name__ == "__main__":

    # Read configuration file
    config = configparser.ConfigParser()
    config.read('/etc/python-gitlab.cfg')
    devsecops = config['devsecops']
    
    # Initiate session
    gl = init_session(devsecops['ssl_cert'], devsecops['ssl_key'], devsecops['url'], devsecops['http_password']) 
    
    #create_issues_one(gl, project_id, 'New Bug', 'Testing new Bug')
    create_issues_mult(gl, devsecops['threat_model'])
