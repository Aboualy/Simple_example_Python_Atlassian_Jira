from Connector import Connector
from jira import JIRA



#options = {'server': 'https://appnix.atlassian.net'}
#jira = JIRA(options, basic_auth=('****@gmail.com', '****'))

jira = Connector("https://appnix.atlassian.net","****@gmail.com","****").getContent()

# Get all projects viewable by anonymous users.
#projects = jira.projects()

#http://jira.readthedocs.io/en/master/examples.html
#From the docs at https://pythonhosted.org/jira/:

#Searching for new issues
#JIRA treats an empty assignee field as 'unassigned'. You can search for it with 'assignee is empty' –  and updatedDate < '2018-03-23' and created < -1d
#For tomorrow we use due > now() AND due <= 2d
#today: updatedDate >= startOfDay() and updatedDate < endOfDay()
#yesterday: updatedDate < -1d AND updatedDate > -2d ORDER BY updatedDate asc

def getIssues():
    issues = jira.search_issues('assignee = EMPTY and created < -3d', jql_str= "project= nixpro ", startAt=0, maxResults=False, validate_query=True,
              fields=None, expand=None, json_result=None)
    return issues


# Get an issue.
issue = jira.issue('NIX-1')
tr = jira.transitions(issue)


#To change status, you need to do transaction above the issue. Transition is just operation that is defined in 'workflow', and transit issue from one status to another.
jira.transition_issue(issue, transition='In Progress')


# Change the issue's description.
issue.update(description='Hello world.')

# Add a comment to the issue.
#jira.add_comment(issue, 'Comment text')



#issue_list = jira.search_issues("assignee = currentUser() AND resolution = Unresolved  and status != Closed and updatedDate < '2018-03-20' and project='nixpro' ORDER BY updatedDate DESC")
#print (issue_list)

#issue_list = jira.search_issues("assignee = currentUser() AND resolution = Unresolved  and status != Closed and updatedDate < '2018-03-20' and project='PROJECT' ORDER BY updatedDate DESC")

#assignee = EMPTY and created < -1d   assignee = currentUser() and due < endOfWeek()
#issue.update(summary='new summary', description='A new summary was added')
#issue.update(assignee={'name': 'new_user'})    # reassigning in update requires issue edit permission






# Find all comments made by Atlassians on this issue.
#atl_comments = [comment for comment in issue.fields.comment.comments
               # if re.search(r'@atlassian.com$', comment.author.emailAddress)]
