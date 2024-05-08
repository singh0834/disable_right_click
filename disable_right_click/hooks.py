from . import __version__ as app_version

app_name = "disable_right_click"
app_title = "Disable Right Click"
app_publisher = "OneHash"
app_description = "Disable right click add on"
app_email = "digital@onehash.ao"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_js = "/assets/disable_right_click/js/disable_right_click.js"
web_include_js = "/assets/disable_right_click/js/disable_right_click.js"
# include js, css files in header of desk.html
# app_include_css = "/assets/disable_right_click/css/disable_right_click.css"
# app_include_js = "/assets/disable_right_click/js/disable_right_click.js"

# include js, css files in header of web template
# web_include_css = "/assets/disable_right_click/css/disable_right_click.css"
# web_include_js = "/assets/disable_right_click/js/disable_right_click.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "disable_right_click/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "disable_right_click.utils.jinja_methods",
#	"filters": "disable_right_click.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "disable_right_click.install.before_install"
# after_install = "disable_right_click.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "disable_right_click.uninstall.before_uninstall"
# after_uninstall = "disable_right_click.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "disable_right_click.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------
scheduler_events = {
    "cron": {
        "* * * * *": [
            "disable_right_click.api.executejob"
        ]
    }
}
# scheduler_events = {
# 	"all": [
# 		"disable_right_click.api.executejob"
# 	],
# 	# "daily": [
# 	# 	"disable_right_click.tasks.daily"
# 	# ],
# 	# "hourly": [
# 	# 	"disable_right_click.tasks.hourly"
# 	# ],
# 	# "weekly": [
# 	# 	"disable_right_click.tasks.weekly"
# 	# ],
# 	# "monthly": [
# 	# 	"disable_right_click.tasks.monthly"
# 	# ],
# }

# Testing
# -------

# before_tests = "disable_right_click.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "disable_right_click.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "disable_right_click.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["disable_right_click.utils.before_request"]
# after_request = ["disable_right_click.utils.after_request"]

# Job Events
# ----------
# before_job = ["disable_right_click.utils.before_job"]
# after_job = ["disable_right_click.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"disable_right_click.auth.validate"
# ]
