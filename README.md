# Oil derrik data calculation API

## Стек

* Django==4.0.6
* djangorestframework==3.13.1
* SQLlite==3.31.1
* celery==5.2.7
* redis==4.3.4
* django-celery-results==2.4.0

## Общее описание

API предоставляет функционал рассчёта данных по заданному алгоритму. Входные и выходные данные передаются в формате JSON. Реализованы валидация входных данных и очередь расчётов, основанная на `celery`.

## Установка и использование
### Docker

* Скачайте из репозитория [файл docker-compose.yml](https://github.com/Sharp-Mind/Oil_api_service/blob/dev/docker-compose.yml)
* Запустите в терминале сборку и запуск контейнеров:
  ```bash
  docker-compose up -d --build
  ```
* После запуска контейнеров POST и GET запросы можно будет передавать по адресу http://0.0.0.0:8585
  
### Из репозитория GIT

* в заранее созданную папку склонировать или распаковать данный репозиторий;
* создать виртуальное окружение рядом с папкой репозитория:

  ```bash
  python3 -m virtualenv -p python3 venv
  ```
* установить зависимости:

  ```bash
  pip install -r requirements.txt
  ```

* перейти в папку с проектом и запустить из терминала скрипт запуска сервиса `.../OIL_API_SERVICE/start_script.sh`:

  ```bash
  ./start_script.sh
  ```

  Скрипт запустит доступ к сервису по адресу http://0.0.0.0:8000.


## Использование, POST и GET запросы

* запустить задачу с пробными данными можно командой

  ```bash
  curl --header "Content-Type: application/json"   --request POST   --data '{"date_start": "2021-12-12","date_fin": "2022-12-12", "lag": "50"}'   http://<hostaddress:port>/api/v1/calculations
  ```

* запросить данные о расчётах:

   ```bash
   curl --request GET http://<hostaddress:port>/api/v1/calculations
   ```

* запрос данных о конкретном расчёте (необходимо передать параметр calculaton id `cid`)

  ```bash
  curl --request GET http://<hostaddress:port>/api/v1/calculations/<cid>
  ```

  пример:

  ```bash
  curl --request GET http://<hostaddress:port>/api/v1/calculations/74b1a42e-562f-441d-a352-f384f4d0f504
  ```

* запрос данных с опциональными полями:

  ```bash
  curl --header "Content-Type: application/json"   --request POST   --data '{"fields": ["elapsed_time", "name"]}'   http://<hostaddress:port>/api/v1/calculations/<cid>
  ```

## Описание эндпоинтов

Реализовано два эндпоинта:

На запуск задачи и на выдачу списка запущенных задач:

```
https:/<hostaddress:port>/api/v1/calculations
```

На получение результатов конкретного запрошенного расчёта:

```
https:/<hostaddress:port>/api/v1/calculations/<str:cid>
```

## Формат входных данных

На вход принимается JSON вида

```json
 {
   "date_start": <str>, 
   "date_fin": <str>,
   "lag": <int>
 }
```

Пример:

```json
 {
   "date_start": "2020-12-12", 
   "date_fin": "2021-12-12",
   "lag": 50
 }
```

## Формат выходных данных

После добавления расчёта в очередь, на вывод будет передан JSON вида

```json
"root":{
  "cid": <str>
}
```

где в поле `cid` будет записан идентификатор добавленной в очередь задачи.

Пример:

```json
"root":{
  "cid":"1bd92554-16fb-4249-b5a6-4cac69cc2fc1"
}
```

## Запрос списка всех задач

Для запроса списка созданных задач достаточно передать GET-запрос. Для списка задач реализована пагинация, поэтому после первого запроса будет передан JSON c первыми десятью записями, указанием наличия следующей и предыдущей страницы и общим количеством записей.

В информации о задачах выводится идентификатор задачи `cid`, дата и время создания задачи `task_created` и текущий статус задачи `task_status`.

Пример:

```json
"root":{
  "count":109
  "next":True
  "previous":False
  "results":[
    0:{
      "cid":"edcb410c-ee58-4c48-bdca-c18daee73125"
      "task_created":"2022-08-07T13:37:29.157894"
      "task_status":"SUCCESS"
    }
    1:{
      "cid":"d816f7c4-0fb6-4edf-a98c-01c3fe67d426"
      "task_created":"2022-08-07T14:21:24.116015"
      "task_status":"SUCCESS"
    }
    2:
      {<etc>}
    ]
}
```

## Запрос результатов одного конкретного запуска расчёта

Чтобы запросить результаты конкретного расчёта, необходимо в адрес GET запроса передать параметр идентификатора задачи `cid`. Пример:

```
http://<hostaddress:port>/api/v1/calculations/74b1a42e-562f-441d-a352-f384f4d0f504
```

Если расчёт ещё не окончен, ответом будет JSON со строкой `None`. Если задача не найдена в списке всех задач, ответом будет JSON со строкой `Does not exist`.

Пример успешного ответа:

```json
"root":{
  "result":{
  "cid":"74b1a42e-562f-441d-a352-f384f4d0f504"
  "task_created":"2022-08-08T06:56:56.120707"
  "date":"{0: Timestamp('2020-12-12 00:00:00'), 1: Timestamp('2021-01-31 00:00:00'), 2: Timestamp('2021-03-22 00:00:00'), 3: Timestamp('2021-05-11 00:00:00'), 4: Timestamp('2021-06-30 00:00:00'), 5: Timestamp('2021-08-19 00:00:00'), 6: Timestamp('2021-10-08 00:00:00'), 7: Timestamp('2021-11-27 00:00:00')}"
  "liquid":"{0: 69.136584196136, 1: 67.00657004665307, 2: 74.15636881156234, 3: 74.09089640381751, 4: 61.383132584314964, 5: 60.45732971225061, 6: 62.30917297346143, 7: 61.64005566554937}"
  "oil":"{0: 59.83504760672463, 1: 53.07338934852999, 2: 47.06142647051125, 3: 40.957233693025366, 4: 32.507084307408284, 5: 27.168736944886273, 6: 21.472120956977246, 7: 14.145847434473781}"
  "water":"{0: 9.30153658941137, 1: 13.933180698123074, 2: 27.094942341051095, 3: 33.133662710792144, 4: 28.87604827690668, 5: 33.288592767364335, 6: 40.83705201648418, 7: 47.49420823107559}"
  "wct":"{0: 0.13453856156710772, 1: 0.20793753043055554, 2: 0.3653757967828988, 3: 0.44720288617111326, 4: 0.470423177527523, 5: 0.5506130179054036, 6: 0.6553939021767693, 7: 0.7705088471816567}"
  "task_status":"SUCCESS"
  }
}
```
