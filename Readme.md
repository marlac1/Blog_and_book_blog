I made this Django structured blog during my formation on python and Django with Docstring organism. 
</br>
This consists in a simple CRUD exercise, for which you can create, read, update and delete blog articles. 
</br>
The user space has not been implemented yet but the signup form is already coded.
</br>
</br>
To run this program :
<ol>
<li>Install project dependencies mentioned in <i>requirements.txt</i></li>
<li>Source the project environment : <i>$ source venv/Scripts/activate</i></li>
<li>Execute <i>$python manage.py runserver</i></li>
</ol>

Urls :
<ul>
<li> <i>/</i> (main index) </li>
<li> <i>about/</i> </li>
<li> <i>customadmin/</i> (admin interface)</li>
<li> <i>blog/</i> (blog index)</li>
<li> <i>create-article/</i> (article creation form)</li>
<li> <i>blog/< str:slug >/</i> (article view)</li>
<li> <i>blog/< str:slug >/edit/</i> (article modification form)</li>
<li> <i>blog/< str:slug >/delete/</i> (article deletion)</li>
<li> <i>signup/</i> (to be implemented)</li>
</ul>



