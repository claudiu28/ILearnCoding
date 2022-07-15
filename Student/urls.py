from django.urls import path

from . import views as vw

urlpatterns = [
	path('studenthome/',vw.studenthome,name='studenthome'),
	path('authfstudent/',vw.authfstudent,name='authfstudent'),
	path('settings/',vw.settings,name='settings'),
	path('displaycourseasstudent/',vw.displaycourseasstudent,name='displaycourseasstudent'),
	
	path('c++/',vw.ctutorial,name='ctutorial'),
	path('python/',vw.python,name='python'),
	path('java/',vw.java,name='java'),
	path('library/',vw.library,name='library'),
	path('editor/',vw.editor,name='editor'),

]
 