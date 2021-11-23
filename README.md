# filter_py

1) Я создал свой репозиторий на github. Создал файл README.md. Загрузил два файла: старый фильтр(old_filter.py) и новый(filter.py).

2) Создал новый проект. Загрузил файлы к себе.

3) Добавил в папку с проектом тестовое изображение.

![image](https://github.com/smileman0001/filter_py/blob/main/test.jpg)

4) Добавил изображение в репозиторий 

5) Запустил filter.py с помощью cProfile.

![image](https://github.com/smileman0001/filter_py/blob/main/screenshots/filter_time.png)

6) Запустил old_filter.py с помощью cProfile.

![image](https://github.com/smileman0001/filter_py/blob/main/screenshots/old_filter_time.png)

Файл old_filter.py работает быстрее, потому что большую часть времени занимает ручной ввод данных.

7) Создадим новый файл filter_with_filename.py, в котором уберем ручной ввод с клавиатуры. Добавим его в репозиторий.

8) Запустил filter_with_filename.py с помощью cProfile.

![image](https://github.com/smileman0001/filter_py/blob/main/screenshots/filter_with_filename_time.png)

Время выполнения составило 490 мс
Обновленный фильтр работает быстрее из-за использования NumPy и рефакторинга кода.

<<Изначальная картинка>>

![image](https://github.com/smileman0001/filter_py/blob/main/test.jpg)

<<Картинка, полученная работой old_filter.py>>

![image](https://github.com/smileman0001/filter_py/blob/main/res.jpg)

<<Картинка, полученная работой filter.py>>

![image](https://github.com/smileman0001/filter_py/blob/main/result.jpg)

9) К выделенной функций написал описание и док-тесты.

![image](https://github.com/smileman0001/filter_py/blob/main/screenshots/doc.png)

10) Доктесты попытался запустить вместе с -v, но ничего толком не вышло

11) К сожалению, нечего прикреплять

12) Проинспектировал код, исправил все предупреждения относительно PEP8 

13) Через отладчик вывел на экран ширину и высоту изоражения, его тип. Также вывел значение ширины блока и количество градаций серого.

![image](https://github.com/smileman0001/filter_py/blob/main/screenshots/img.png)

![image](https://github.com/smileman0001/filter_py/blob/main/screenshots/step%26size.png)

14) Cкриншоты результата работы отладчика: 

![image](https://github.com/smileman0001/filter_py/blob/main/screenshots/debugger.png)
