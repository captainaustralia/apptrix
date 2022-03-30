<h1> Test proj for APPTRIX</h1>
<p>Start 29.03.22 21:30 (Vladivostok time)</p>

<p>1.Создать модель участников. У участника должна быть аватарка, пол, имя и фамилия, почта. (DONE)</p>
<p>2.Создать эндпоинт регистрации нового участника: /api/clients/create (не забываем о пароле и совместимости с авторизацией модели участника). (DONE)</p>
<p>3.При регистрации нового участника необходимо обработать его аватарку: наложить на него водяной знак (в качестве водяного знака можете взять любую картинку).(DONE)</p>
<p>4.Создать эндпоинт оценивания участником другого участника: /api/clients/{id}/match. В случае, если возникает взаимная симпатия, то ответом выдаем почту клиенту и отправляем на почты участников: Вы понравились имя! Почта участника: почта(DONE)</p>
<p>5.Создать эндпоинт списка участников: /api/list. Должна быть возможность фильтрации списка по полу, имени, фамилии. Советую использовать библиотеку Django-filters.(DONE)</p>
<p>6.Реализовать определение дистанции между участниками. Добавить поля долготы и широты. В api списка добавить дополнительный фильтр, который показывает участников в пределах заданной дистанции относительно авторизованного пользователя. Не забывайте об оптимизации запросов к базе данных<a href="https://en.wikipedia.org/wiki/Great-circle_distance"> link</a>(DONE)</p>
<p>7.Задеплоить проект на любом удобном для вас хостинге, сервисах PaaS (Heroku) и т.п. Должна быть возможность просмотреть реализацию всех задач. Если есть какие-то особенности по тестированию, написать в Readme. Там же оставить ссылку/ссылки на АПИ проекта(DONE)</p>
<hr>
<h2> API endpoints :</h2>
<ul>
    <li><a>https://apptrix-alexeev.herokuapp.com/api/clients/create/</a> Create user endpoint </li>
    <li><a>https://apptrix-alexeev.herokuapp.com/api/auth/login</a> Login endpoint </li>
    <li><a>https://apptrix-alexeev.herokuapp.com/api/auth/logout</a> Logout endpoint </li>
    <li><a>https://apptrix-alexeev.herokuapp.com/api/list</a> Users list endpoint (with filters name/lastname/gender) if add &distance=num you can filter by distance  </li>
    <li><a>https://apptrix-alexeev.herokuapp.com/api/list/?distance=500</a> Users list (filter distance) endpoint </li>
    <li><a>https://apptrix-alexeev.herokuapp.com/api/clients/1/match</a> Like endpoint (Instead of ID -> add some number,  field is set, you will like some user If he likes you too, you will receive an email </li>
    <li><a>https://apptrix-alexeev.herokuapp.com</a> Mainpage endpoint , if u are login , u can go , else site redirect to login page </li>
</ul>
<p> Работу по наложения водяного знака можно проверить в drf, кликнув на фото после создания своего пользователя клацнув по юрлу, либо залогинившись произойдет редирект на мейн страницу с вашим фото. </p>
<p> В базе специально сгенерировано 20 пользователей с какими-то рандомными координатами, можно проверить работу фильтра (если проверяете все фильтры вместе , добавьте &distance).По дефолту у нового пользователя широта - 0 , долгота - 0, но всё таки на дистанции distance=300 и более можно увидеть работу фильтра</p>
<p> Также в Вашем таске было установлено добавить филды в модель пользователя, но при этом не сказано, есть ли необходимость в добавление API по созданию пользователя данные филды. Поэтому, если они все же необходимы, можете оставить issues , я добавлю</p>
<p> Время начала выполнения таска - 29.03.22 21:30 , конец выполнения 30.03.22 22.00 </p>
<p> P.s просьба оставить какой-то коммент в issues с оценкой работы </p>
